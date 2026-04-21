## ADDED Requirements

### Requirement: 本地 cron 定时导出
系统 SHALL 提供本地 cron 配置示例，定时执行 `python scripts/export_articles.py`。默认频率为每 6 小时一次。

#### Scenario: Cron 定时执行
- **WHEN** 到达配置的 cron 时间
- **THEN** 系统 SHALL 自动执行导出脚本，从本地 Miniflux 拉取新文章

### Requirement: GitHub Actions 工作流（可选）
系统 SHALL 提供 GitHub Actions workflow 文件（`.github/workflows/export.yml`），当 Miniflux 部署在公网可访问的服务器时使用。配置 cron schedule + workflow_dispatch 手动触发。

#### Scenario: 手动触发
- **WHEN** 用户在 GitHub Actions 页面点击 "Run workflow"
- **THEN** 工作流 SHALL 立即执行导出脚本

### Requirement: 自动提交结果
导出完成后 SHALL 自动将新增的文章文件和更新的 `data/export_state.json` commit 并 push 到仓库。commit message MUST 包含 `[skip ci]` 以避免触发循环。仅在有实际变更时才提交。

#### Scenario: 有新文章时自动 commit
- **WHEN** 导出运行产生了新的 Markdown 文件
- **THEN** 工作流/脚本 SHALL 自动 commit 变更，message 格式为 `chore: export N new articles [skip ci]`

#### Scenario: 无新文章时不 commit
- **WHEN** 所有文章均已导出
- **THEN** SHALL 跳过 commit 步骤，不产生空 commit

### Requirement: Python 环境配置
`requirements.txt` SHALL 锁定依赖版本：miniflux（官方 Python client）、markdownify（HTML→Markdown）、PyYAML。

#### Scenario: 依赖安装
- **WHEN** 执行 `pip install -r requirements.txt`
- **THEN** SHALL 安装指定版本的 miniflux、markdownify、PyYAML
