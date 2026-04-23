## ADDED Requirements

### Requirement: GitHub Actions workflow
The system SHALL use a GitHub Actions workflow (`.github/workflows/fetch.yml`) to run the fetch script on a scheduled basis using cron triggers.

#### Scenario: Scheduled execution
- **WHEN** the cron schedule triggers
- **THEN** the workflow SHALL check out the repository, install Python dependencies, run the fetch script, and commit any changes

#### Scenario: Manual trigger
- **WHEN** a user manually triggers the workflow via `workflow_dispatch`
- **THEN** the workflow SHALL run the same fetch process as the scheduled execution

### Requirement: Automatic commit of changes
The workflow SHALL use `stefanzweifel/git-auto-commit-action@v5` (or equivalent) to commit new articles and updated state.

#### Scenario: New articles fetched
- **WHEN** the fetch script produces new Markdown files and updates `state.json`
- **THEN** the workflow SHALL commit all changes with the message `chore(rss): fetch new articles`

#### Scenario: No new articles
- **WHEN** the fetch script produces no new files and `state.json` is unchanged
- **THEN** the workflow SHALL NOT create an empty commit

### Requirement: Workflow failure conditions
The workflow SHALL fail (exit with error) ONLY in the following cases:
1. The Python script itself crashes (unhandled exception)
2. ALL feeds fail to process (indicating a system-level issue)

#### Scenario: Individual feed failure does not fail the workflow
- **WHEN** one or more feeds fail but at least one succeeds
- **THEN** the workflow SHALL still exit successfully

#### Scenario: All feeds fail
- **WHEN** every feed in the configuration fails to process
- **THEN** the workflow SHALL exit with an error status

### Requirement: Python dependency installation
The workflow SHALL install Python dependencies from `requirements.txt` before running the fetch script.

#### Scenario: Dependencies installed
- **WHEN** the workflow runs
- **THEN** it SHALL install all packages listed in `requirements.txt` (feedparser, trafilatura, PyYAML) using pip

### Requirement: Run summary logging
The fetch script SHALL output a summary of each run to stdout, including:
- Number of feeds processed
- Per-feed: count of entries found
- Number of new articles added
- Number of articles skipped (already seen)
- Number of articles that failed extraction

#### Scenario: Normal run summary
- **WHEN** the fetch script completes a run
- **THEN** it SHALL print a summary with all 5 metrics listed above to stdout