"""RssWiki RSS fetch pipeline.

Reads feeds.yml, fetches RSS feeds, extracts full article text with
trafilatura, and saves articles as Markdown files with YAML frontmatter.
Uses state.json for URL-based deduplication.
"""

import hashlib
import json
import logging
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import feedparser
import trafilatura
import yaml

ROOT_DIR = Path(__file__).resolve().parent.parent
FEEDS_PATH = ROOT_DIR / "feeds.yml"
STATE_PATH = ROOT_DIR / "data" / "state.json"
ARTICLES_DIR = ROOT_DIR / "articles"

FEED_RETRIES = 2
EXTRACT_RETRIES = 1
MIN_CONTENT_LENGTH = 50

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("rsswiki")


# ---------------------------------------------------------------------------
# Run summary tracker
# ---------------------------------------------------------------------------
class RunSummary:
    """Collects metrics for the run summary output."""

    def __init__(self):
        self.feeds_processed = 0
        self.entries_per_feed: dict[str, int] = {}
        self.articles_added = 0
        self.articles_skipped = 0
        self.articles_failed = 0

    def print_summary(self):
        log.info("=" * 50)
        log.info("Run summary")
        log.info("=" * 50)
        log.info("Feeds processed: %d", self.feeds_processed)
        for name, count in self.entries_per_feed.items():
            log.info("  %-30s %d entries", name, count)
        log.info("New articles added:   %d", self.articles_added)
        log.info("Articles skipped:     %d", self.articles_skipped)
        log.info("Articles failed:       %d", self.articles_failed)
        log.info("=" * 50)


summary = RunSummary()


def load_feeds(path: Path) -> list[dict]:
    """Load feeds.yml, validate required fields, skip invalid entries."""
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    feeds = data.get("feeds", []) if data else []
    valid = []
    for entry in feeds:
        missing = [k for k in ("name", "url", "category") if k not in entry]
        if missing:
            log.warning(
                "Skipping feed entry missing %s: %s",
                ", ".join(missing),
                entry,
            )
            continue
        valid.append(entry)
    return valid


def fetch_feed(url: str, name: str) -> feedparser.FeedParserDict | None:
    """Fetch and parse an RSS/Atom feed. Returns parsed feed or None on failure."""
    for attempt in range(1, FEED_RETRIES + 2):  # 1-based, total = FEED_RETRIES+1
        try:
            log.info(
                "Fetching feed %s (attempt %d/%d)", url, attempt, FEED_RETRIES + 1
            )
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
                time.sleep(2 ** attempt)
    return None


def load_state(path: Path) -> dict:
    """Load state.json. Returns {"seen_urls": []} if missing or invalid."""
    if path.exists():
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict) and "seen_urls" in data:
                return data
        except (json.JSONDecodeError, OSError):
            log.warning("Invalid state.json, starting fresh")
    return {"seen_urls": []}


def save_state(path: Path, state: dict) -> None:
    """Persist state.json to disk."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def extract_content(url: str) -> str | None:
    """Extract main text content from a URL using trafilatura.

    Returns extracted text or None on failure / too-short content.
    """
    for attempt in range(1, EXTRACT_RETRIES + 2):
        try:
            downloaded = trafilatura.fetch_url(url)
            if downloaded is None:
                log.warning("trafilatura fetch returned None for %s", url)
                if attempt < EXTRACT_RETRIES + 1:
                    time.sleep(2)
                continue

            result = trafilatura.extract(
                downloaded,
                include_comments=False,
                include_tables=True,
                favor_precision=True,
            )
            if result and len(result.strip()) >= MIN_CONTENT_LENGTH:
                return result.strip()
            else:
                log.warning(
                    "Content too short or empty for %s (attempt %d)", url, attempt
                )
                if attempt < EXTRACT_RETRIES + 1:
                    time.sleep(2)
                continue
        except Exception as exc:
            log.warning(
                "Extraction attempt %d/%d failed for %s: %s",
                attempt,
                EXTRACT_RETRIES + 1,
                url,
                exc,
            )
            if attempt < EXTRACT_RETRIES + 1:
                time.sleep(2)

    return None


def slugify(title: str) -> str:
    """Convert a title to a filesystem-safe slug."""
    slug = title.lower().strip()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    return slug[:80] if len(slug) > 80 else slug


def build_filepath(category: str, date_str: str, title: str, state_urls: set) -> Path:
    slug = slugify(title)
    filename = f"{date_str}-{slug}.md"
    filepath = ARTICLES_DIR / category / filename

    if filepath.exists():
        short_hash = hashlib.md5(title.encode()).hexdigest()[:6]
        filename = f"{date_str}-{slug}-{short_hash}.md"
        filepath = ARTICLES_DIR / category / filename

    return filepath


def generate_markdown(
    title: str,
    url: str,
    date: str,
    source: str,
    category: str,
    tags: list[str],
    fetched_at: str,
    content: str,
) -> str:
    """Generate a Markdown string with YAML frontmatter and content."""
    frontmatter = {
        "title": title,
        "url": url,
        "date": date,
        "source": source,
        "category": category,
        "tags": tags if tags else [],
        "fetched_at": fetched_at,
    }
    fm_str = yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False).strip()
    return f"---\n{fm_str}\n---\n\n{content}\n"


def write_article(filepath: Path, markdown: str) -> None:
    """Write a Markdown file to disk, creating parent dirs as needed."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(markdown)


def parse_entry_date(entry: dict) -> str:
    """Extract a date string (YYYY-MM-DD) from a feedparser entry.

    Tries published_parsed, then updated_parsed, falls back to today.
    """
    for date_field in ("published_parsed", "updated_parsed"):
        parsed = entry.get(date_field)
        if parsed:
            try:
                dt = datetime(*parsed[:6], tzinfo=timezone.utc)
                return dt.strftime("%Y-%m-%d")
            except (TypeError, ValueError):
                continue
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def parse_entry_tags(entry: dict) -> list[str]:
    """Extract tag labels from a feedparser entry's tags field."""
    tags = entry.get("tags", [])
    if isinstance(tags, list):
        return [t.get("term", "") for t in tags if isinstance(t, dict) and t.get("term")]
    return []


def process_feed(feed_config: dict, state: dict) -> int:
    """Process a single feed: fetch, deduplicate, extract, write.

    Returns the number of new articles successfully added.
    """
    name = feed_config["name"]
    url = feed_config["url"]
    category = feed_config["category"]

    parsed = fetch_feed(url, name)
    if parsed is None:
        log.error("All retries failed for feed: %s", name)
        return -1

    entries = parsed.entries or []
    summary.entries_per_feed[name] = len(entries)

    seen_urls = set(state["seen_urls"])
    new_count = 0

    for entry in entries:
        entry_url = entry.get("link")
        if not entry_url:
            continue

        if entry_url in seen_urls:
            summary.articles_skipped += 1
            continue

        title = entry.get("title", "Untitled")
        log.info("Processing: %s — %s", name, title)

        content = extract_content(entry_url)
        if content is None:
            summary.articles_failed += 1
            continue

        date_str = parse_entry_date(entry)
        filepath = build_filepath(category, date_str, title, seen_urls)

        tags = parse_entry_tags(entry)
        fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        markdown = generate_markdown(
            title=title,
            url=entry_url,
            date=date_str,
            source=name,
            category=category,
            tags=tags,
            fetched_at=fetched_at,
            content=content,
        )

        try:
            write_article(filepath, markdown)
            state["seen_urls"].append(entry_url)
            seen_urls.add(entry_url)
            new_count += 1
            summary.articles_added += 1
            log.info("Saved: %s", filepath.relative_to(ROOT_DIR))
        except OSError as exc:
            log.error("Failed to write %s: %s", filepath, exc)
            summary.articles_failed += 1

    return new_count


def main() -> None:
    log.info("RssWiki fetch pipeline starting")

    feeds = load_feeds(FEEDS_PATH)
    if not feeds:
        log.error("No valid feeds found in %s", FEEDS_PATH)
        sys.exit(1)

    # Load state
    state = load_state(STATE_PATH)

    feeds_succeeded = 0
    feeds_failed = 0

    for feed_config in feeds:
        summary.feeds_processed += 1
        result = process_feed(feed_config, state)
        if result >= 0:
            feeds_succeeded += 1
        else:
            feeds_failed += 1

    save_state(STATE_PATH, state)

    summary.print_summary()

    if feeds_succeeded == 0 and feeds_failed > 0:
        log.error("All feeds failed — exiting with error")
        sys.exit(1)

    log.info("Pipeline complete")
    sys.exit(0)


if __name__ == "__main__":
    main()