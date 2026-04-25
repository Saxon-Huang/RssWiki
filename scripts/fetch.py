"""RssWiki metadata-first RSS pipeline."""

import hashlib
import json
import logging
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from html import escape
from pathlib import Path
from typing import Optional

import feedparser
import yaml

ROOT_DIR = Path(__file__).resolve().parent.parent
FEEDS_PATH = ROOT_DIR / "feeds.yml"
DISCOVERED_PATH = ROOT_DIR / "data" / "discovered_urls.json"
CANDIDATES_PATH = ROOT_DIR / "data" / "candidates.json"
LEGACY_STATE_PATH = ROOT_DIR / "data" / "state.json"
DOCS_PATH = ROOT_DIR / "docs" / "index.html"

FEED_RETRIES = 2
RECENT_DAYS = 7
MAX_ENTRIES_PER_FEED = 20
MAX_BATCHES = 3
SUMMARY_PREVIEW_LENGTH = 280

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("rsswiki")


class RunSummary:
    def __init__(self):
        self.feeds_processed = 0
        self.entries_per_feed: dict[str, int] = {}
        self.candidates_added = 0
        self.entries_skipped = 0
        self.feeds_failed = 0

    def print_summary(self):
        log.info("=" * 50)
        log.info("Run summary")
        log.info("=" * 50)
        log.info("Feeds processed: %d", self.feeds_processed)
        for name, count in self.entries_per_feed.items():
            log.info("  %-30s %d entries", name, count)
        log.info("New candidates added: %d", self.candidates_added)
        log.info("Entries skipped:      %d", self.entries_skipped)
        log.info("Feeds failed:         %d", self.feeds_failed)
        log.info("=" * 50)


summary = RunSummary()


def load_feeds(path: Path) -> list[dict]:
    with open(path, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    feeds = data.get("feeds", []) if data else []
    valid = []
    for entry in feeds:
        missing = [key for key in ("name", "url", "category") if key not in entry]
        if missing:
            log.warning("Skipping feed entry missing %s: %s", ", ".join(missing), entry)
            continue
        valid.append(entry)
    return valid


def fetch_feed(url: str, name: str) -> Optional[feedparser.FeedParserDict]:
    for attempt in range(1, FEED_RETRIES + 2):
        try:
            log.info("Fetching feed %s (attempt %d/%d)", url, attempt, FEED_RETRIES + 1)
            parsed = feedparser.parse(url, request_headers={"User-Agent": "RssWiki/1.0"})
            if parsed.bozo and not parsed.entries:
                raise RuntimeError(f"Feed parse error: {parsed.bozo_exception}")
            return parsed
        except Exception as exc:
            log.warning(
                "Feed fetch attempt %d/%d failed for %s: %s",
                attempt,
                FEED_RETRIES + 1,
                name,
                exc,
            )
            if attempt < FEED_RETRIES + 1:
                time.sleep(2**attempt)
    return None


def load_discovered_urls() -> set[str]:
    if DISCOVERED_PATH.exists():
        try:
            with open(DISCOVERED_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
            urls = data.get("discovered_urls", []) if isinstance(data, dict) else []
            return {url for url in urls if isinstance(url, str)}
        except (json.JSONDecodeError, OSError):
            log.warning("Invalid discovered_urls.json, starting fresh")

    if LEGACY_STATE_PATH.exists():
        try:
            with open(LEGACY_STATE_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
            urls = data.get("seen_urls", []) if isinstance(data, dict) else []
            migrated = {url for url in urls if isinstance(url, str)}
            if migrated:
                log.info("Migrated %d legacy URLs from state.json", len(migrated))
            return migrated
        except (json.JSONDecodeError, OSError):
            log.warning("Invalid legacy state.json, starting fresh")

    return set()


def save_discovered_urls(discovered_urls: set[str]) -> None:
    DISCOVERED_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {"discovered_urls": sorted(discovered_urls)}
    with open(DISCOVERED_PATH, "w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2, ensure_ascii=False)


def load_candidates() -> dict:
    if CANDIDATES_PATH.exists():
        try:
            with open(CANDIDATES_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
            if isinstance(data, dict) and isinstance(data.get("batches"), list):
                data.setdefault("generated_at", None)
                return data
        except (json.JSONDecodeError, OSError):
            log.warning("Invalid candidates.json, starting fresh")
    return {"generated_at": None, "batches": []}


def save_candidates(candidates: dict) -> None:
    CANDIDATES_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CANDIDATES_PATH, "w", encoding="utf-8") as file:
        json.dump(candidates, file, indent=2, ensure_ascii=False)


def parse_entry_datetime(entry: dict) -> Optional[datetime]:
    for date_field in ("published_parsed", "updated_parsed"):
        parsed = entry.get(date_field)
        if parsed:
            try:
                return datetime(*parsed[:6], tzinfo=timezone.utc)
            except (TypeError, ValueError):
                continue
    return None


def parse_entry_tags(entry: dict) -> list[str]:
    tags = entry.get("tags", [])
    if isinstance(tags, list):
        return [tag.get("term", "") for tag in tags if isinstance(tag, dict) and tag.get("term")]
    return []


def strip_html(value: str) -> str:
    without_tags = re.sub(r"<[^>]+>", " ", value)
    normalized = re.sub(r"\s+", " ", without_tags)
    return normalized.strip()


def extract_summary(entry: dict) -> str:
    candidates = []
    for key in ("summary", "description"):
        value = entry.get(key)
        if isinstance(value, str) and value.strip():
            candidates.append(value)

    content_list = entry.get("content", [])
    if isinstance(content_list, list):
        for item in content_list:
            if isinstance(item, dict):
                value = item.get("value")
                if isinstance(value, str) and value.strip():
                    candidates.append(value)

    for value in candidates:
        summary_text = strip_html(value)
        if summary_text:
            return summary_text

    return "No summary available."


def candidate_id(url: str) -> str:
    return hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]


def preview_summary(summary_text: str) -> str:
    if len(summary_text) <= SUMMARY_PREVIEW_LENGTH:
        return summary_text
    return summary_text[: SUMMARY_PREVIEW_LENGTH - 1].rstrip() + "…"


def category_label(category: str) -> str:
    mapping = {
        "tech-blog": "Tech Blog",
        "ai-news": "AI / LLM",
        "tech-news": "Tech News",
        "paper": "Paper",
    }
    return mapping.get(category, category)


def build_candidate(entry: dict, feed_config: dict, entry_datetime: datetime, discovered_at: str) -> dict:
    url = entry["link"]
    title = entry.get("title", "Untitled").strip() or "Untitled"
    summary_text = extract_summary(entry)
    return {
        "id": candidate_id(url),
        "title": title,
        "url": url,
        "source": feed_config["name"],
        "category": feed_config["category"],
        "published_at": entry_datetime.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "summary": summary_text,
        "tags": parse_entry_tags(entry),
        "discovered_at": discovered_at,
    }


def process_feed(feed_config: dict, discovered_urls: set[str], batch_items: list[dict], discovered_at: str) -> int:
    name = feed_config["name"]
    parsed = fetch_feed(feed_config["url"], name)
    if parsed is None:
        log.error("All retries failed for feed: %s", name)
        summary.feeds_failed += 1
        return -1

    entries = parsed.entries or []
    summary.entries_per_feed[name] = len(entries)

    cutoff = datetime.now(timezone.utc) - timedelta(days=RECENT_DAYS)
    processed_recent_entries = 0
    added = 0

    for entry in entries:
        if processed_recent_entries >= MAX_ENTRIES_PER_FEED:
            break

        entry_url = entry.get("link")
        if not entry_url:
            summary.entries_skipped += 1
            continue

        entry_datetime = parse_entry_datetime(entry)
        if entry_datetime is None or entry_datetime < cutoff:
            summary.entries_skipped += 1
            continue

        processed_recent_entries += 1

        if entry_url in discovered_urls:
            summary.entries_skipped += 1
            continue

        batch_items.append(build_candidate(entry, feed_config, entry_datetime, discovered_at))
        discovered_urls.add(entry_url)
        added += 1
        summary.candidates_added += 1
        log.info("Discovered candidate: %s — %s", name, entry.get("title", "Untitled"))

    return added


def trim_batches(candidates: dict) -> None:
    candidates["batches"] = candidates.get("batches", [])[:MAX_BATCHES]


def build_html(candidates: dict) -> str:
    generated_at = candidates.get("generated_at") or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    batches = candidates.get("batches", [])

    parts = [
        "<!DOCTYPE html>",
        '<html lang="en">',
        "<head>",
        '  <meta charset="UTF-8">',
        '  <meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '  <title>RssWiki Inbox</title>',
        "  <style>",
        "    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; margin: 0; background: #0b1020; color: #e5e7eb; }",
        "    .container { max-width: 960px; margin: 0 auto; padding: 32px 20px 80px; }",
        "    h1, h2, h3 { margin: 0; }",
        "    .meta { color: #94a3b8; margin-top: 8px; margin-bottom: 24px; }",
        "    .batch { margin-top: 32px; }",
        "    .batch-header { padding-bottom: 10px; border-bottom: 1px solid #1f2937; margin-bottom: 20px; }",
        "    .category { margin-top: 24px; }",
        "    .cards { display: grid; gap: 16px; margin-top: 12px; }",
        "    .card { background: #111827; border: 1px solid #1f2937; border-radius: 12px; padding: 16px 18px; }",
        "    .card-title { font-size: 1.05rem; font-weight: 600; color: #f8fafc; text-decoration: none; }",
        "    .card-title:hover { color: #7dd3fc; }",
        "    .card-meta { color: #94a3b8; font-size: 0.9rem; margin-top: 8px; }",
        "    .tags { margin-top: 10px; display: flex; flex-wrap: wrap; gap: 8px; }",
        "    .tag { font-size: 0.75rem; padding: 2px 8px; border-radius: 999px; background: #1e293b; color: #93c5fd; }",
        "    .summary { margin-top: 12px; line-height: 1.65; color: #d1d5db; }",
        "    .original-link { display: inline-block; margin-top: 14px; color: #7dd3fc; text-decoration: none; }",
        "    .original-link:hover { text-decoration: underline; }",
        "    .empty { margin-top: 48px; color: #94a3b8; }",
        "  </style>",
        "</head>",
        "<body>",
        '  <div class="container">',
        "    <h1>RssWiki Inbox</h1>",
        f"    <div class=\"meta\">Metadata-only candidate inbox · Last updated {escape(generated_at)} · Recent {MAX_BATCHES} batches</div>",
    ]

    if not batches:
        parts.append('    <div class="empty">No candidates discovered yet.</div>')
    else:
        for batch in batches:
            batch_id = escape(batch.get("batch_id", "unknown"))
            batch_generated_at = escape(batch.get("generated_at", "unknown"))
            parts.extend(
                [
                    '    <section class="batch">',
                    '      <div class="batch-header">',
                    f"        <h2>Batch · {batch_generated_at}</h2>",
                    f"        <div class=\"meta\">ID: {batch_id} · {len(batch.get('items', []))} items</div>",
                    "      </div>",
                ]
            )

            grouped: dict[str, list[dict]] = {}
            for item in batch.get("items", []):
                grouped.setdefault(item.get("category", "other"), []).append(item)

            for category, items in sorted(grouped.items(), key=lambda pair: category_label(pair[0])):
                items.sort(key=lambda item: item.get("published_at", ""), reverse=True)
                parts.extend(
                    [
                        '      <div class="category">',
                        f"        <h3>{escape(category_label(category))}</h3>",
                        '        <div class="cards">',
                    ]
                )
                for item in items:
                    tags_html = "".join(
                        f'<span class="tag">{escape(tag)}</span>' for tag in item.get("tags", []) if tag
                    )
                    meta = " · ".join(
                        [
                            escape(item.get("source", "Unknown source")),
                            escape(item.get("category", "unknown")),
                            escape(item.get("published_at", "unknown")[:10]),
                        ]
                    )
                    parts.extend(
                        [
                            '          <article class="card">',
                            f'            <a class="card-title" href="{escape(item.get("url", "#"), quote=True)}" target="_blank" rel="noreferrer">{escape(item.get("title", "Untitled"))}</a>',
                            f'            <div class="card-meta">{meta}</div>',
                        ]
                    )
                    if tags_html:
                        parts.append(f'            <div class="tags">{tags_html}</div>')
                    parts.append(f'            <div class="summary">{escape(preview_summary(item.get("summary", "")))}</div>')
                    parts.append(
                        f'            <a class="original-link" href="{escape(item.get("url", "#"), quote=True)}" target="_blank" rel="noreferrer">Read original</a>'
                    )
                    parts.append("          </article>")
                parts.extend(["        </div>", "      </div>"])

            parts.append("    </section>")

    parts.extend(["  </div>", "</body>", "</html>"])
    return "\n".join(parts) + "\n"


def save_html(candidates: dict) -> None:
    DOCS_PATH.parent.mkdir(parents=True, exist_ok=True)
    DOCS_PATH.write_text(build_html(candidates), encoding="utf-8")


def main() -> None:
    log.info("RssWiki metadata pipeline starting")

    feeds = load_feeds(FEEDS_PATH)
    if not feeds:
        log.error("No valid feeds found in %s", FEEDS_PATH)
        sys.exit(1)

    discovered_urls = load_discovered_urls()
    candidates = load_candidates()

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    batch_items: list[dict] = []

    for feed_config in feeds:
        summary.feeds_processed += 1
        process_feed(feed_config, discovered_urls, batch_items, generated_at)

    if batch_items:
        candidates["batches"].insert(
            0,
            {
                "batch_id": generated_at,
                "generated_at": generated_at,
                "items": batch_items,
            },
        )
        trim_batches(candidates)

    candidates["generated_at"] = generated_at

    save_discovered_urls(discovered_urls)
    save_candidates(candidates)
    save_html(candidates)

    summary.print_summary()

    if summary.feeds_failed == summary.feeds_processed and summary.feeds_processed > 0:
        log.error("All feeds failed — exiting with error")
        sys.exit(1)

    log.info("Metadata pipeline complete")
    sys.exit(0)


if __name__ == "__main__":
    main()
