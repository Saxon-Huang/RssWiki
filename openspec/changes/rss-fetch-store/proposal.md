## Why

RssWiki 项目需要一个自动化的 RSS 信息采集管道，定时从技术博客和论文源抓取文章，提取全文并存储为 Markdown 文件。这是整个知识库的数据入口——没有稳定的内容采集，后续的 LLM 知识图谱（Graphify）和可视化都无从谈起。

选择 Miniflux 作为 RSS 聚合引擎，复用其成熟的 feed 解析、全文抓取、去重、调度能力，我们只写一层薄胶水代码将新文章导出为 Markdown 文件。这符合"多复用、少造轮子"的原则。

## What Changes

- 新增 Miniflux 服务部署配置（Docker Compose），含 PostgreSQL 和 Miniflux 容器
- 新增 Python 导出脚本：通过 Miniflux REST API 拉取未导出的新文章 → 转换为带 frontmatter 的 Markdown → 写入 `articles/` 目录
- 新增导出状态追踪（JSON 文件），记录已导出文章的 Miniflux entry ID，避免重复导出
- 新增 GitHub Actions workflow，定时运行导出脚本并自动 commit 新文章到仓库
- 新增文章存储目录结构（按来源和日期组织）

## Capabilities

### New Capabilities
- `miniflux-setup`: Miniflux + PostgreSQL 的 Docker Compose 部署配置与初始化
- `article-export`: 通过 Miniflux API 拉取新文章并转换为 Markdown 文件的导出管道
- `export-tracking`: 已导出文章的状态追踪，基于 Miniflux entry ID 去重
- `ci-automation`: GitHub Actions cron 定时工作流，自动导出并 commit 结果

### Modified Capabilities
（无，这是全新项目）

## Impact

- **新增依赖**: miniflux (Python client), PyYAML; 运行时依赖 Docker + Docker Compose
- **文件结构**: 新增 `docker-compose.yml`, `scripts/export_articles.py`, `articles/`, `data/`, `.github/workflows/fetch.yml`
- **CI/CD**: 新增 GitHub Actions workflow，需要 `contents: write` 权限；Miniflux 需要在本地或服务器持续运行
- **存储**: 文章以 Markdown 文件形式存储在 git 仓库中，仓库体积会随时间增长
