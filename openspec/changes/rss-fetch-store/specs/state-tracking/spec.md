## ADDED Requirements

### Requirement: 基于 Entry ID 去重
系统 SHALL 维护 `data/export_state.json`，记录已导出文章的 Miniflux entry ID。每次运行时 MUST 过滤掉已导出的 entry，仅导出新文章。

#### Scenario: 跳过已导出的文章
- **WHEN** Miniflux 返回的 unread entries 中某条目的 entry_id 已存在于 `export_state.json`
- **THEN** 系统 SHALL 跳过该条目，不重复导出

#### Scenario: 新文章加入导出记录
- **WHEN** 一篇新文章成功导出为 Markdown
- **THEN** 系统 SHALL 将该文章的 entry_id 写入 `export_state.json`

### Requirement: 导出状态文件格式
`data/export_state.json` SHALL 使用 JSON 格式，包含一个 `exported_ids` 数组（已导出的 entry ID 列表）和 `last_export_at`（ISO 8601 时间戳）。该文件 MUST 随文章一起 commit 到 git 仓库。

#### Scenario: 状态文件持久化
- **WHEN** 一次导出运行结束
- **THEN** `data/export_state.json` SHALL 包含本次及所有历史运行中已导出的 entry ID

#### Scenario: 状态文件不存在时的初始化
- **WHEN** 首次运行，`data/export_state.json` 不存在
- **THEN** 系统 SHALL 创建初始文件 `{"exported_ids": [], "last_export_at": null}`，并在导出完成后写入结果

### Requirement: 标记已导出文章为已读
系统 SHALL 在成功导出文章后，调用 Miniflux API 将对应 entry 标记为 read。这确保下次运行时 Miniflux 不会再返回这些文章。

#### Scenario: 导出后标记已读
- **WHEN** 一篇文章成功导出为 Markdown 并写入状态记录
- **THEN** 系统 SHALL 调用 Miniflux `update_entry(entry_id, status='read')` API

### Requirement: 运行日志
每次运行 SHALL 输出摘要日志：新导出数、跳过数、失败数。日志 MUST 输出到 stdout，供 cron 或 GitHub Actions 捕获。

#### Scenario: 运行摘要输出
- **WHEN** 一次导出运行完成
- **THEN** 系统 SHALL 输出格式化的摘要，例如 `Exported: 12 | Skipped: 38 | Failed: 1`
