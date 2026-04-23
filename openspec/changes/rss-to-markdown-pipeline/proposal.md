## Why

RssWiki 项目需要一个零运维的自动 RSS 采集管道，定时从技术博客和论文源抓取文章全文并存储为 Markdown 文件。这是整个知识库的数据入口——没有稳定的内容采集，后续的 LLM 知识图谱（Graphify）和可视化都无从谈起。

选择纯脚本 + GitHub Actions 方案（参考 garss 模式），不需要本地/服务器常驻任何服务，完全在 GitHub Actions 内完成抓取、转换和提交。

## What Changes

- 新增 Python 抓取脚本：feedparser 解析 RSS → trafilatura 提取全文 → 生成带 frontmatter 的 Markdown → 写入 `articles/` 目录
- 新增 RSS 信源配置文件 `feeds.yml`：YAML 格式，支持 name/url/category/via 字段
- 新增去重状态文件 `data/state.json`：基于 URL 去重，增量抓取
- 新增 GitHub Actions workflow：定时运行抓取脚本，自动 commit 新文章到仓库
- 新增文章存储目录结构：按 category 组织，每篇文章一个 Markdown 文件

## Capabilities

### New Capabilities
- `feed-config`: RSS 信源配置管理，YAML 格式定义 feeds（name/url/category/via）
- `article-fetch`: RSS 解析 + 全文提取 + Markdown 生成管道（feedparser + trafilatura）
- `state-tracking`: 基于 URL 的去重状态追踪，增量抓取避免重复
- `ci-automation`: GitHub Actions cron 定时工作流，自动抓取并 commit 结果

### Modified Capabilities
（无，这是全新项目）

## Impact

- **新增依赖**: feedparser, trafilatura, PyYAML; 运行时依赖 GitHub Actions 环境
- **文件结构**: 新增 `scripts/fetch.py`, `feeds.yml`, `data/state.json`, `articles/`, `.github/workflows/fetch.yml`
- **CI/CD**: 新增 GitHub Actions workflow，需要 `contents: write` 权限
- **存储**: 文章以 Markdown 文件形式存储在 git 仓库中，仓库体积随时间增长（每篇文章几 KB，可接受）
- **外部依赖**: 使用 RSSHub 公共实例作为无原生 RSS 站点的信源补充，依赖其可用性