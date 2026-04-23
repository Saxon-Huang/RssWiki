## Context

RssWiki 是一个个人知识管理项目，目标是自动采集技术博客和论文，通过 LLM 构建知识图谱（后续使用 Graphify）。本 change 聚焦第一阶段：零运维的 RSS 抓取与 Markdown 存储管道。

当前状态：空仓库（仅有 .gitignore）。

约束条件：
- 个人项目，以学习和实用为目的
- 优先复用成熟开源组件，减少自造轮子
- 完全在 GitHub Actions 内运行，不依赖本地/服务器常驻进程
- 存储在 git 仓库中，Markdown 文件作为后续 Graphify 的输入

## Goals / Non-Goals

**Goals:**
- 用 feedparser 解析 RSS/Atom feed，用 trafilatura 提取全文内容
- 增量抓取：基于 URL 去重，只处理新文章
- 每篇文章输出一个带 frontmatter 的 Markdown 文件
- GitHub Actions cron 定时运行，自动 commit 新文章
- RSSHub 公共实例作为无原生 RSS 站点的信源补充，按普通 feed URL 接入

**Non-Goals:**
- 不做 LLM 摘要/分类（后续迭代）
- 不做 Web UI 或阅读器界面
- 不做知识图谱可视化（后续 change）
- 不做 Miniflux 或任何常驻服务
- 不自建 RSS 解析器或全文提取器
- 不做 RSSHub 自托管或专用抽象层
- 不做路由级别的过滤/变换规则引擎
- 正文提取失败时不回退保存 RSS 摘要

## Decisions

### D1: 纯脚本 vs 常驻服务

**选择：纯脚本 + GitHub Actions**

| 方案 | 优点 | 缺点 |
|---|---|---|
| 纯脚本（feedparser + trafilatura） | 零运维，GitHub Actions 直接跑，无依赖 | 需要自己写去重和状态管理（~200-300行） |
| Miniflux 常驻服务 | 成熟全栈（解析+全文+去重+调度+API） | 需要 Docker + PostgreSQL 常驻，与 GitHub Actions 模式冲突 |

理由：用户明确要求"在 GitHub Actions 上运行，不需要本地/服务器常驻"。纯脚本方案完全满足。

### D2: RSS 解析库

**选择：feedparser**

Python RSS/Atom 解析的事实标准库，garss 项目同款。稳定、成熟、无替代需要。

### D3: 全文提取库

**选择：trafilatura**

学术级网页正文提取质量，显著优于 newspaper4k。在 benchmark 中准确率领先。

### D4: 去重方案

**选择：JSON 文件记录已抓取 URL**

```json
{
  "seen_urls": ["https://example.com/post-1", "https://example.com/post-2"]
}
```

简单可读，适合个人项目规模。只在文章成功写入 Markdown 后才写入 state.json。

### D5: 配置格式

**选择：YAML（feeds.yml）**

```yaml
feeds:
  - name: Simon Willison
    url: https://simonwillison.net/atom/everything/
    category: tech-blog
```

必填：name, url, category。可选：via（用于标注 RSSHub 等来源）。脚本逻辑不依赖 via 字段。

### D6: 文件组织

```
articles/<category>/YYYY-MM-DD-<slug>.md
```

- category 来自 feeds.yml
- 日期优先用文章发布时间，无发布时间则用抓取日期
- slug 由标题生成
- 同名冲突时追加短 hash

### D7: Markdown frontmatter

```yaml
---
title: "Article Title"
url: "https://example.com/post"
date: "2026-04-23"
source: "Simon Willison"
category: "tech-blog"
tags:
  - llm
  - python
fetched_at: "2026-04-23T08:00:00Z"
---
```

### D8: CI 自动化方案

**选择：GitHub Actions cron + stefanzweifel/git-auto-commit-action@v5**

与 garss 项目的自动化模式一致。workflow 定义 cron 触发，Python 脚本执行抓取，git-auto-commit-action 负责提交变更。

### D9: RSSHub 集成方式

**选择：作为普通 feed URL 接入，无专用抽象层**

- 在 feeds.yml 中直接写 RSSHub 生成的 feed URL
- via 字段仅用于人类标注，脚本不依赖
- 优先使用原生 RSS；无原生 RSS 或原生 feed 质量不足时使用 RSSHub
- 第一版不做自托管 RSSHub、不做 route 级抽象、不做专用鉴权/缓存

### D10: 错误处理策略

- 单个 feed 失败：记录日志，跳过，继续处理其他 feed
- 单篇文章提取失败：跳过，不写入 state.json
- 空内容/过短内容：视为提取失败，跳过
- 只有在 entry 解析、正文提取、Markdown 写入全部成功后才写入 state.json
- 无新文章时不 commit

### D11: 超时与重试

- feed 拉取：15 秒超时，最多重试 2 次（共 3 次尝试）
- 正文提取：20 秒超时，最多重试 1 次

## Risks / Trade-offs

**[GitHub Actions 可用性]** → Actions 有执行时间限制和频率限制，个人项目 free tier 足够。缓解：控制 feed 数量和每次抓取量。

**[RSSHub 公共实例稳定性]** → rsshub.app 偶发不可用或限流。缓解：RSSHub 只做补充信源，失败时按普通 feed 失败处理，不影响整体。

**[仓库体积增长]** → 文章以 Markdown 存储，长期仓库会变大。缓解：每篇文章几 KB，个人项目可接受。

**[trafilatura 提取失败]** → 部分网站反爬或结构特殊导致提取失败。缓解：跳过该文章，不保存残缺内容。后续可考虑回退策略。

**[state.json 冲突]** → 多次运行可能产生并发写入冲突。缓解：GitHub Actions cron 不会并发运行同一 workflow。