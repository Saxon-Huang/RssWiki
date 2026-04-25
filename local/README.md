# Local Review Workflow

## 1. Configure the knowledge-base repository

Copy the example config and fill in your local knowledge-base repo path:

```bash
cp config/local_settings.example.json config/local_settings.json
```

Required field:

- `knowledge_base_repo_path`: absolute path to your local knowledge-base repository

Optional field:

- `knowledge_base_articles_dir`: subdirectory inside the repo for imported articles (default: `rss-imports`)

## 2. Install local-only dependencies

```bash
pip install -r requirements-local.txt
```

## 3. Start the local review server

```bash
python3 local/review_server.py
```

Then open:

```text
http://127.0.0.1:8765
```

## 4. Actions

- `下载到知识库`: immediately fetches the full article and writes a Markdown file into the configured knowledge-base repo
- `忽略`: marks the candidate as ignored in local state

Local review state is stored in `data/local_review_state.json`.
