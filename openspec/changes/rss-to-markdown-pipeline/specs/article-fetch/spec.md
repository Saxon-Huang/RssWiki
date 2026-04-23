## ADDED Requirements

### Requirement: RSS feed parsing
The system SHALL use `feedparser` to parse each feed URL and extract article entries. From each entry the system SHALL extract: title, link (URL), published date, and tags (if available).

#### Scenario: Successful feed parsing
- **WHEN** a feed URL returns valid RSS or Atom content
- **THEN** the system SHALL parse all entries and extract title, URL, date, and tags for each

#### Scenario: Feed URL unreachable
- **WHEN** a feed URL is unreachable or times out (15 seconds)
- **THEN** the system SHALL retry up to 2 additional times (3 total attempts)
- **THEN** if all retries fail, the system SHALL log the error and continue to the next feed without stopping

### Requirement: Full article text extraction
For each new article URL, the system SHALL use `trafilatura` to fetch and extract the main text content from the article's web page.

#### Scenario: Successful text extraction
- **WHEN** trafilatura successfully extracts content from an article URL
- **THEN** the extracted text SHALL be used as the Markdown body

#### Scenario: Extraction returns empty or very short content
- **WHEN** trafilatura returns empty content or content shorter than a reasonable threshold (very short or clearly incomplete)
- **THEN** the system SHALL skip this article
- **THEN** the system SHALL NOT write this URL to state.json

#### Scenario: Extraction fails
- **WHEN** trafilatura fails to extract content (network error, timeout, or extraction error)
- **THEN** the system SHALL retry once (2 total attempts, 20 seconds timeout each)
- **THEN** if retry also fails, the system SHALL skip this article
- **THEN** the system SHALL NOT write this URL to state.json

#### Scenario: Fallback to RSS summary is NOT allowed
- **WHEN** full text extraction fails
- **THEN** the system SHALL NOT save the RSS feed summary as a substitute
- **THEN** the system SHALL skip the article entirely

### Requirement: Markdown file generation
The system SHALL generate one Markdown file per successfully fetched article.

Each file SHALL have:
- YAML frontmatter with: `title`, `url`, `date`, `source`, `category`, `tags`, `fetched_at`
- Article body as the full extracted text content

#### Scenario: Markdown file with complete frontmatter
- **WHEN** an article is successfully fetched and extracted
- **THEN** the system SHALL generate a Markdown file with frontmatter containing all 7 fields
- **THEN** `source` SHALL match the `name` field of the feed in `feeds.yml`
- **THEN** `category` SHALL match the `category` field from `feeds.yml`
- **THEN** `tags` SHALL come from the RSS entry's tags, defaulting to an empty list if none exist
- **THEN** `fetched_at` SHALL be the UTC timestamp of when the article was processed

### Requirement: File naming and path
Article files SHALL be stored at `articles/<category>/YYYY-MM-DD-<slug>.md`.

- `category` SHALL match the feed's category field
- `YYYY-MM-DD` SHALL be the article's published date; if unavailable, the fetch date SHALL be used
- `slug` SHALL be derived from the article title

#### Scenario: Normal file naming
- **WHEN** an article titled "RAG is Not a Database" is published on 2026-04-23 in category `tech-blog`
- **THEN** the file SHALL be stored at `articles/tech-blog/2026-04-23-rag-is-not-a-database.md`

#### Scenario: Filename collision
- **WHEN** two articles produce the same filename
- **THEN** the system SHALL append a short hash to the second filename to avoid collision

### Requirement: Individual feed failure isolation
A failure in processing one feed SHALL NOT prevent the system from processing other feeds.

#### Scenario: One feed fails, others succeed
- **WHEN** feed A fails but feeds B, C, D are valid
- **THEN** the system SHALL process B, C, D normally
- **THEN** feed A's failure SHALL be logged but SHALL NOT cause the entire run to fail