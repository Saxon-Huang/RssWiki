## 1. 项目初始化

- [ ] 1.1 创建 `requirements.txt`，锁定依赖版本：miniflux、markdownify、PyYAML
- [ ] 1.2 创建项目目录结构：`scripts/`、`data/`、`articles/`、`config/`
- [ ] 1.3 创建 `.gitignore`（排除 `__pycache__/`、`.venv/`、`*.pyc`、`.env`）
- [ ] 1.4 创建空目录占位：`articles/.gitkeep`、`data/.gitkeep`
- [ ] 1.5 创建 `.env.example`，列出所需环境变量（`MINIFLUX_URL`、`MINIFLUX_API_KEY`）

## 2. Miniflux 部署配置

- [ ] 2.1 创建 `docker-compose.yml`：Miniflux + PostgreSQL 服务，配置环境变量和 volume 持久化
- [ ] 2.2 创建 `config/initial_feeds.yaml`：推荐的技术博客/论文 RSS 源示例（含 RSSHub 路由示例）
- [ ] 2.3 本地启动 Miniflux：`docker compose up -d`，验证 Web UI 可访问，创建 API key
- [ ] 2.4 在 Miniflux 中添加 2-3 个测试 feed 源，确认自动抓取正常工作

## 3. Miniflux API 导出脚本

- [ ] 3.1 实现 `scripts/miniflux_client.py`：封装 Miniflux API 调用（连接、获取 unread entries、标记 read）
- [ ] 3.2 实现 `scripts/export_articles.py` 主入口：串联 API 拉取 → HTML→Markdown → 文件写入 → 状态更新 → 标记已读
- [ ] 3.3 实现 HTML→Markdown 转换：使用 markdownify，保留代码块、链接、标题层级
- [ ] 3.4 实现 YAML frontmatter 生成：title、url、source、feed_url、date、author、category、entry_id、fetched_at
- [ ] 3.5 实现 slug 生成：ASCII 安全、80 字符上限、处理中文和特殊字符
- [ ] 3.6 实现文件写入：按 `articles/<category>/YYYY-MM-DD-<slug>.md` 路径存储

## 4. 导出状态管理

- [ ] 4.1 实现 `scripts/export_state.py`：加载/保存 `data/export_state.json`，首次运行初始化
- [ ] 4.2 实现 entry ID 去重：过滤已导出的 entry，仅处理新文章
- [ ] 4.3 实现导出后标记已读：调用 Miniflux API 将已导出 entry 标记为 read

## 5. 日志与错误处理

- [ ] 5.1 实现运行摘要日志：`Exported: N | Skipped: N | Failed: N`
- [ ] 5.2 实现错误处理：Miniflux API 不可达时报错退出；单篇文章导出失败不中断整体流程

## 6. 定时自动化

- [ ] 6.1 创建本地 cron 配置示例：每 6 小时执行导出脚本 + git add/commit/push
- [ ] 6.2 创建 `.github/workflows/export.yml`（可选）：GitHub Actions cron + git-auto-commit-action@v5
- [ ] 6.3 配置 `contents: write` 权限和 Miniflux API Secrets

## 7. 端到端验证

- [ ] 7.1 本地手动运行 `python scripts/export_articles.py`，验证端到端导出流程
- [ ] 7.2 验证去重：重复运行确认不会重复导出
- [ ] 7.3 验证异常处理：Miniflux 停止时确认脚本优雅退出
- [ ] 7.4 验证 Miniflux 已读标记：导出后在 Web UI 确认文章已标为 read
