## 1. 项目骨架

- [ ] 1.1 创建目录结构：`scripts/`, `data/`, `articles/`, `.github/workflows/`
- [ ] 1.2 创建 `requirements.txt`：feedparser, trafilatura, PyYAML
- [ ] 1.3 创建 `feeds.yml` 初始种子信源配置（4个源：Simon Willison, OpenAI News, HN Frontpage, arXiv cs.AI）
- [ ] 1.4 创建 `data/state.json` 初始空状态文件（`{"seen_urls": []}`）

## 2. RSS 解析与配置

- [ ] 2.1 实现 `feeds.yml` 加载逻辑：读取 YAML 配置，验证必填字段（name, url, category），跳过无效条目并记录日志
- [ ] 2.2 实现 feed 解析逻辑：用 feedparser 解析每个 feed URL，提取 title/link/date/tags，15 秒超时，最多重试 2 次
- [ ] 2.3 实现 feed 失败隔离：单个 feed 解析失败不影响其他 feed 处理

## 3. 全文提取与 Markdown 生成

- [ ] 3.1 实现去重检查：读取 `state.json` 中的 `seen_urls`，过滤已抓取的 URL
- [ ] 3.2 实现 trafilatura 全文提取：对每个新文章 URL 提取正文，20 秒超时，最多重试 1 次
- [ ] 3.3 实现提取失败处理：空内容/过短内容/提取失败时跳过文章，不写入 state.json，不回退保存 RSS 摘要
- [ ] 3.4 实现 slug 生成和文件命名：`articles/<category>/YYYY-MM-DD-<slug>.md`，同名冲突时追加短 hash
- [ ] 3.5 实现 Markdown 文件写入：YAML frontmatter（title/url/date/source/category/tags/fetched_at）+ 正文内容

## 4. 状态管理

- [ ] 4.1 实现 state.json 更新逻辑：仅在文章成功写入 Markdown 后才将 URL 追加到 `seen_urls`
- [ ] 4.2 确保 state.json 在脚本结束时持久化到磁盘

## 5. GitHub Actions 自动化

- [ ] 5.1 创建 `.github/workflows/fetch.yml`：cron 触发 + workflow_dispatch 手动触发
- [ ] 5.2 配置 workflow 步骤：checkout → 安装 Python → pip install requirements.txt → 运行脚本 → git-auto-commit-action 提交变更
- [ ] 5.3 实现无变更不提交逻辑：没有新文章时不创建空 commit
- [ ] 5.4 配置 commit message 为 `chore(rss): fetch new articles`

## 6. 日志与错误处理

- [ ] 6.1 实现运行总结日志输出：feed 数量、每 feed entries 数、新增文章数、跳过数、失败数
- [ ] 6.2 实现整体失败条件：仅当脚本自身崩溃或所有 feed 都失败时 workflow 才失败

## 7. 首批验证

- [ ] 7.1 手动运行脚本验证：至少 1 个原生 RSS 源和 1 个 RSSHub 源能成功抓取
- [ ] 7.2 验证 Markdown 文件生成正确：frontmatter 字段完整，正文不为空
- [ ] 7.3 验证 state.json 去重：重复运行不产生重复文章
- [ ] 7.4 验证 GitHub Actions workflow：cron 和手动触发均能正常运行