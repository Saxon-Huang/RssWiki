## ADDED Requirements

### Requirement: Feed configuration file format
The system SHALL use a YAML configuration file (`feeds.yml`) at the repository root to define all RSS feed sources.

The file SHALL contain a top-level `feeds` key with a list of feed entries. Each entry SHALL have:
- `name` (required): Human-readable name of the feed source
- `url` (required): The RSS/Atom feed URL
- `category` (required): Category name used as the output directory under `articles/`
- `via` (optional): Source type label (e.g., `rsshub`) for human annotation only; the system SHALL NOT use this field for logic branching

#### Scenario: Valid feeds.yml with all required fields
- **WHEN** `feeds.yml` contains entries with `name`, `url`, and `category` fields
- **THEN** the system SHALL load and process all entries without error

#### Scenario: Feeds.yml with RSSHub URLs
- **WHEN** `feeds.yml` contains entries with `via: rsshub` and RSSHub-generated URLs
- **THEN** the system SHALL treat them identically to regular RSS feed URLs with no special handling

#### Scenario: Missing required fields
- **WHEN** a feed entry is missing `name`, `url`, or `category`
- **THEN** the system SHALL log a warning and skip that entry, continuing with remaining feeds

### Requirement: Feed categories determine output structure
The `category` field in each feed entry SHALL be used as the subdirectory name under `articles/` for storing fetched articles.

#### Scenario: Articles stored by category
- **WHEN** an article is fetched from a feed with `category: tech-blog`
- **THEN** the article file SHALL be stored under `articles/tech-blog/`

### Requirement: First seed feeds
The initial `feeds.yml` SHALL include the following seed feeds:

1. Simon Willison — `https://simonwillison.net/atom/everything/` — category: `tech-blog`
2. OpenAI News — `https://openai.com/news/rss.xml` — category: `ai-news`
3. Hacker News Frontpage — `https://rsshub.app/hn/frontpage` — category: `tech-news` — via: `rsshub`
4. arXiv cs.AI — `https://rsshub.app/arxiv/category/cs.AI` — category: `paper` — via: `rsshub`

#### Scenario: Initial feeds.yml is provided
- **WHEN** the repository is first set up
- **THEN** `feeds.yml` SHALL contain at least these 4 seed feeds