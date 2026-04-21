## Context

RssWiki 是一个个人知识管理项目，目标是自动采集技术博客和论文，通过 LLM 构建知识图谱。本 change 聚焦第一阶段：RSS 抓取与存储管道。

当前状态：空仓库，无任何基础设施。需要从零搭建 RSS 采集管道。

约束条件：
- 个人项目，以学习和实用为目的
- **优先复用成熟开源组件，减少自造轮子**
- 存储在 git 仓库中，Markdown 文件作为后续 Graphify 的输入
- 接受本地 Docker 常驻服务的运维成本，换取更完整的功能和更少的自造轮子

## Goals / Non-Goals

**Goals:**
- 复用 Miniflux 完成 RSS 抓取、全文提取、去重、调度
- 只写薄胶水层：Miniflux API → Markdown 导出
- Markdown 输出格式对 Graphify 友好
- GitHub Actions cron 定时导出并 commit

**Non-Goals:**
- 不做 LLM 摘要/分类（后续迭代，可直接用 miniflux-ai）
- 不做 Web UI 或阅读器界面（Miniflux 自带）
- 不做实时推送通知（Miniflux Webhook 已支持，后续按需启用）
- 不接入 Graphify（后续 change）
- 不自建 RSS 解析/全文提取/去重逻辑

## Decisions

### D1: Miniflux vs 纯 Python 脚本

**选择：Miniflux**

| 方案 | 优点 | 缺点 |
|---|---|---|
| **Miniflux** | 成熟的 RSS 全栈：解析+全文抓取+去重+调度+API+Webhook+搜索+Web UI；miniflux-ai 现成 LLM 集成；star 9.1k，活跃维护 | 需要 Docker + PostgreSQL 常驻 |
| 纯 Python 脚本 | 零运维、GitHub Actions 直接跑 | 需要自己写 feed 解析、全文提取、去重、状态管理（~400 行代码，13 个实现任务） |

理由：用户明确"更注重复用+轻量开发"。Miniflux 替我们完成了 feed 解析（feedparser 级别）、全文抓取（Readability）、去重（PostgreSQL）、定时刷新（内置 scheduler）。我们只需写 ~100 行导出胶水代码。

### D2: Miniflux Python Client 选择

**选择：官方 `miniflux` PyPI 包**

Miniflux 提供了官方 Python client（`miniflux` on PyPI），封装了完整的 REST API。支持 `get_entries(status='unread')` 等查询，直接获取文章内容、元数据和全文。

### D3: 导出状态管理

**选择：JSON 文件记录已导出的 entry ID**

Miniflux 内部管理了文章的已读/未读状态，但"已导出为 Markdown"是我们的业务状态，Miniflux 不知道。用一个 `data/export_state.json` 记录已导出文章的 Miniflux entry ID。

流程：
1. 调用 Miniflux API 获取 unread entries
2. 与 `export_state.json` 中的已导出 ID 对比，过滤出未导出的
3. 导出新文章为 Markdown
4. 将新 entry ID 追加到 `export_state.json`
5. （可选）将已导出文章标记为 read

### D4: 文件组织结构

```
RssWiki/
├── docker-compose.yml       # Miniflux + PostgreSQL
├── scripts/
│   └── export_articles.py   # 导出胶水脚本
├── data/
│   └── export_state.json    # 已导出状态
├── articles/
│   ├── tech-blog/
│   │   ├── 2026-04-21-some-article.md
│   │   └── ...
│   ├── paper/
│   │   └── ...
│   └── uncategorized/
│       └── ...
├── requirements.txt
└── .github/
    └── workflows/
        └── export.yml
```

按 `category/YYYY-MM-DD-slug.md` 组织。category 来自 Miniflux 的 feed category 名称。

### D5: CI 自动化方案

**选择：GitHub Actions cron + stefanzweifel/git-auto-commit-action@v5**

与纯脚本方案相同，但脚本从"fetch_rss"变为"export_articles"——从 Miniflux API 拉，而不是从原始 feed 拉。

关键区别：Miniflux API 需要网络访问。如果 Miniflux 跑在本地 Docker，GitHub Actions 无法直接访问。需要：
- Miniflux 部署在可访问的服务器（VPS / Tailscale / 内网穿透），或者
- 本地 cron 代替 GitHub Actions

### D6: 本地 cron vs GitHub Actions

**选择：双模式支持**

- **本地 cron**：Miniflux 在本地 Docker 运行时，用系统 cron 或 Miniflux Webhook 触发导出脚本
- **GitHub Actions**：Miniflux 部署在公网可访问的服务器时，用 GitHub Actions cron

在 tasks 中先实现本地 cron 模式（更简单），GitHub Actions 作为可选配置。

## Risks / Trade-offs

**[Miniflux 常驻运维]** → 需要维护 Docker + PostgreSQL 容器。缓解：Docker Compose 一键启停，Miniflux 本身非常轻量（单 Go binary，~30MB Docker image，~50MB RAM idle）。个人电脑休眠时服务暂停，醒来后 Miniflux 自动补抓。

**[GitHub Actions 无法访问本地 Miniflux]** → Actions 云端无法访问 localhost 的 Miniflux。缓解：先走本地 cron 模式；如需 Actions 模式，用 Tailscale Serve 或部署 Miniflux 到 VPS。

**[仓库体积增长]** → 文章以 Markdown 存储在 git 中，长期运行仓库会变大。缓解：每篇文章几 KB，1000 篇也就几 MB，个人项目可接受。

**[Miniflux API 密钥管理]** → 导出脚本需要 Miniflux API endpoint + API key。缓解：环境变量传入，不硬编码到代码中。本地 cron 通过 `.env` 文件，GitHub Actions 通过 Secrets。

## Open Questions

- **miniflux-ai 集成时机**：miniflux-ai 可以为文章自动生成 LLM 摘要和分类，结果写回 Miniflux entry。如果先启用 miniflux-ai，导出脚本可以直接获取 LLM 摘要作为 frontmatter 字段。是否在本 change 中纳入？
- **RSSHub 配合**：RSSHub（⭐43.5k）可以把没有 RSS 的网站（ArXiv、HN 等）生成 feed，作为 Miniflux 的信源补充。是否在 feeds 初始化时配置 RSSHub 路由？
- **Graphify 对接**：当前 `articles/` 目录结构是否与 Graphify 输入格式兼容，需要实际对接验证。Graphify 期望输入是文件夹内的 Markdown 文件，理论上可以直接指向 `articles/` 目录。
