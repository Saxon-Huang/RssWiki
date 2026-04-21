## ADDED Requirements

### Requirement: Docker Compose 部署配置
系统 SHALL 提供 `docker-compose.yml` 文件，定义 Miniflux 和 PostgreSQL 两个服务。Miniflux MUST 配置管理员账号（通过环境变量 `MINIFLUX_ADMIN_USERNAME` 和 `MINIFLUX_ADMIN_PASSWORD`）。PostgreSQL 数据 MUST 使用 Docker volume 持久化。

#### Scenario: 一键启动 Miniflux
- **WHEN** 用户执行 `docker compose up -d`
- **THEN** Miniflux 和 PostgreSQL 容器 SHALL 启动，Miniflux 在端口 8080 提供服务

#### Scenario: 数据持久化
- **WHEN** Docker 容器重启
- **THEN** PostgreSQL 数据 SHALL 通过 volume 保留，所有 feed 配置和文章不丢失

### Requirement: 环境变量配置
Miniflux 连接信息（API endpoint、API key）SHALL 通过环境变量传入：`MINIFLUX_URL`、`MINIFLUX_API_KEY`。MUST NOT 硬编码到代码中。本地运行时通过 `.env` 文件加载，GitHub Actions 通过 Secrets 传入。

#### Scenario: 本地开发环境配置
- **WHEN** 用户创建 `.env` 文件并设置 `MINIFLUX_URL=http://localhost:8080` 和 `MINIFLUX_API_KEY=xxx`
- **THEN** 导出脚本 SHALL 从环境变量读取 Miniflux 连接信息

### Requirement: Feed 初始配置
系统 SHALL 提供 `config/initial_feeds.yaml` 示例文件，列出推荐的技术博客/论文 RSS 源（含 RSSHub 路由示例）。用户 SHALL 通过 Miniflux Web UI 或 API 添加 feed，YAML 文件仅作为参考配置，不被脚本自动加载。

#### Scenario: 手动添加 feed
- **WHEN** 用户通过 Miniflux Web UI 添加一个 RSS 源
- **THEN** Miniflux SHALL 自动开始抓取该 feed 的文章
