## ADDED Requirements

### Requirement: URL-based deduplication
The system SHALL maintain a `data/state.json` file containing a `seen_urls` array of all article URLs that have been successfully processed.

#### Scenario: State file structure
- **WHEN** the system initializes or reads state
- **THEN** `data/state.json` SHALL contain a JSON object with a `seen_urls` key mapped to an array of URL strings

#### Scenario: New article detected
- **WHEN** an article URL is not present in `seen_urls`
- **THEN** the system SHALL process the article (fetch, extract, generate Markdown)

#### Scenario: Already-seen article detected
- **WHEN** an article URL is already present in `seen_urls`
- **THEN** the system SHALL skip this article without fetching or processing

### Requirement: State written only on success
A URL SHALL be added to `seen_urls` only after ALL of the following succeed:
1. Feed entry parsing
2. Full text extraction by trafilatura
3. Markdown file generation and writing to disk

#### Scenario: Successful processing adds URL
- **WHEN** an article is fully processed (parsed, extracted, and written to disk)
- **THEN** its URL SHALL be appended to `seen_urls`

#### Scenario: Failed extraction does NOT add URL
- **WHEN** trafilatura fails to extract content for an article
- **THEN** its URL SHALL NOT be added to `seen_urls`
- **THEN** the article MAY be retried on a subsequent run

#### Scenario: Markdown write failure does NOT add URL
- **WHEN** the Markdown file cannot be written to disk
- **THEN** its URL SHALL NOT be added to `seen_urls`

### Requirement: State file persistence
The `state.json` file SHALL be persisted to disk and committed alongside new articles.

#### Scenario: State file updated after processing
- **WHEN** new articles are successfully processed
- **THEN** `data/state.json` SHALL be updated with the new URLs before the workflow commits changes