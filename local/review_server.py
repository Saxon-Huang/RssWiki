import hashlib
import json
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

import requests
import trafilatura
import yaml


ROOT_DIR = Path(__file__).resolve().parent.parent
LOCAL_HTML_PATH = ROOT_DIR / "local" / "index.html"
CONFIG_PATH = ROOT_DIR / "config" / "local_settings.json"
CONFIG_EXAMPLE_PATH = ROOT_DIR / "config" / "local_settings.example.json"
STATE_PATH = ROOT_DIR / "data" / "local_review_state.json"
CANDIDATES_PATH = ROOT_DIR / "data" / "candidates.json"

DEFAULT_STATE = {
    "downloaded_urls": [],
    "ignored_urls": [],
    "failed_downloads": {},
}

BROWSER_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}


def load_json(path: Path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def save_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_state() -> dict:
    state = load_json(STATE_PATH, DEFAULT_STATE.copy())
    state.setdefault("downloaded_urls", [])
    state.setdefault("ignored_urls", [])
    state.setdefault("failed_downloads", {})
    return state


def save_state(state: dict) -> None:
    save_json(STATE_PATH, state)


def load_candidates() -> dict:
    data = load_json(CANDIDATES_PATH, {"generated_at": None, "batches": []})
    data.setdefault("generated_at", None)
    data.setdefault("batches", [])
    return data


def load_settings() -> dict:
    data = load_json(CONFIG_PATH, {})
    if not isinstance(data, dict):
        return {}
    return data


def candidate_lookup(candidates: dict) -> dict:
    lookup = {}
    for batch in candidates.get("batches", []):
        for item in batch.get("items", []):
            url = item.get("url")
            if isinstance(url, str):
                lookup[url] = item
    return lookup


def slugify(text: str) -> str:
    cleaned = "".join(char.lower() if char.isalnum() else "-" for char in text.strip())
    while "--" in cleaned:
        cleaned = cleaned.replace("--", "-")
    return cleaned.strip("-")[:80] or "untitled"


def file_hash(value: str) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()[:8]


def validate_repo_path(settings: dict) -> Path:
    repo_path = settings.get("knowledge_base_repo_path")
    if not isinstance(repo_path, str) or not repo_path.strip():
        raise ValueError("Missing config/local_settings.json: knowledge_base_repo_path")
    path = Path(repo_path).expanduser().resolve()
    if not path.exists():
        raise ValueError(f"Knowledge base repo path does not exist: {path}")
    return path


def article_output_dir(settings: dict) -> str:
    value = settings.get("knowledge_base_articles_dir", "rss-imports")
    if not isinstance(value, str) or not value.strip():
        return "rss-imports"
    return value.strip().strip("/")


def fetch_full_text(url: str) -> str:
    response = requests.get(url, headers=BROWSER_HEADERS, timeout=20)
    response.raise_for_status()
    content = trafilatura.extract(
        response.text,
        include_comments=False,
        include_tables=True,
        favor_precision=True,
    )
    if not content or len(content.strip()) < 50:
        raise ValueError("Failed to extract useful article content")
    return content.strip()


def build_markdown(item: dict, content: str) -> str:
    frontmatter = {
        "title": item.get("title", "Untitled"),
        "url": item.get("url"),
        "date": item.get("published_at", "")[:10],
        "source": item.get("source"),
        "category": item.get("category"),
        "tags": item.get("tags", []),
        "summary": item.get("summary", ""),
        "discovered_at": item.get("discovered_at"),
        "downloaded_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    yaml_text = yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False).strip()
    return f"---\n{yaml_text}\n---\n\n{content}\n"


def write_article_to_repo(item: dict, markdown: str, settings: dict) -> str:
    repo_path = validate_repo_path(settings)
    base_dir = repo_path / article_output_dir(settings) / item.get("category", "uncategorized")
    base_dir.mkdir(parents=True, exist_ok=True)

    date_text = (item.get("published_at") or datetime.now(timezone.utc).strftime("%Y-%m-%d"))[:10]
    slug = slugify(item.get("title", "Untitled"))
    path = base_dir / f"{date_text}-{slug}.md"
    if path.exists():
        path = base_dir / f"{date_text}-{slug}-{file_hash(item.get('url', slug))}.md"

    path.write_text(markdown, encoding="utf-8")
    return str(path)


class ReviewHandler(BaseHTTPRequestHandler):
    def _send_json(self, payload: dict, status: int = HTTPStatus.OK) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_json_body(self) -> dict:
        length = int(self.headers.get("Content-Length", "0"))
        if length <= 0:
            return {}
        body = self.rfile.read(length)
        return json.loads(body.decode("utf-8"))

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path in {"/", "/index.html"}:
            html = LOCAL_HTML_PATH.read_text(encoding="utf-8")
            body = html.encode("utf-8")
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        if parsed.path == "/api/bootstrap":
            settings = load_settings()
            candidates = load_candidates()
            state = load_state()
            payload = {
                "candidates": candidates,
                "state": state,
                "config": {
                    "configured": bool(settings.get("knowledge_base_repo_path")),
                    "knowledge_base_repo_path": settings.get("knowledge_base_repo_path", ""),
                    "knowledge_base_articles_dir": article_output_dir(settings),
                    "config_example": str(CONFIG_EXAMPLE_PATH.relative_to(ROOT_DIR)),
                },
            }
            self._send_json(payload)
            return

        self.send_error(HTTPStatus.NOT_FOUND)

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path not in {"/api/ignore", "/api/download"}:
            self.send_error(HTTPStatus.NOT_FOUND)
            return

        payload = {}
        url = None
        try:
            payload = self._read_json_body()
            url = payload.get("url")
            if not isinstance(url, str) or not url.strip():
                raise ValueError("Missing candidate url")

            candidates = load_candidates()
            lookup = candidate_lookup(candidates)
            item = lookup.get(url)
            if not item:
                raise ValueError("Candidate not found in candidates.json")

            state = load_state()
            if parsed.path == "/api/ignore":
                if url not in state["ignored_urls"]:
                    state["ignored_urls"].append(url)
                if url in state["failed_downloads"]:
                    del state["failed_downloads"][url]
                save_state(state)
                self._send_json({"ok": True, "status": "ignored", "url": url})
                return

            settings = load_settings()
            content = fetch_full_text(url)
            markdown = build_markdown(item, content)
            output_path = write_article_to_repo(item, markdown, settings)

            if url not in state["downloaded_urls"]:
                state["downloaded_urls"].append(url)
            if url in state["failed_downloads"]:
                del state["failed_downloads"][url]
            save_state(state)

            self._send_json({"ok": True, "status": "downloaded", "url": url, "output_path": output_path})
        except Exception as exc:
            if parsed.path == "/api/download":
                if isinstance(url, str) and url:
                    state = load_state()
                    state.setdefault("failed_downloads", {})[url] = str(exc)
                    save_state(state)
            self._send_json({"ok": False, "error": str(exc)}, status=HTTPStatus.BAD_REQUEST)


def main() -> None:
    server = ThreadingHTTPServer(("127.0.0.1", 8765), ReviewHandler)
    print("Local review server running at http://127.0.0.1:8765")
    server.serve_forever()


if __name__ == "__main__":
    main()
