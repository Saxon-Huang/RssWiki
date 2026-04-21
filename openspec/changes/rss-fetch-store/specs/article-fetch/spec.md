## ADDED Requirements

### Requirement: 从 Miniflux API 拉取未导出文章
系统 SHALL 使用 Miniflux Python client 调用 `get_entries(status='unread')` API 获取未读文章列表。每篇文章 SHALL 提取以下字段：entry_id、title、url、content（HTML 正文）、published_at、feed title、feed category。

#### Scenario: 成功拉取未读文章
- **WHEN** Miniflux 中存在未读文章
- **THEN** 系统 SHALL 返回所有未读文章的完整信息列表

#### Scenario: Miniflux API 不可达
- **WHEN** Miniflux 服务未启动或网络不通
- **THEN** 系统 SHALL 报错退出，输出连接错误信息，不继续执行

### Requirement: HTML 转 Markdown
系统 SHALL 将 Miniflux 返回的文章 HTML 正文转换为 Markdown 格式。MUST 保留段落结构、标题层级、代码块、链接等语义元素。去除广告、导航等非正文内容（Miniflux 的 Readability 已预处理，正文 HTML 通常是干净的）。

#### Scenario: 标准 HTML 转 Markdown
- **WHEN** 文章正文包含 `<h2>`、`<p>`、`<pre><code>`、`<a>` 等 HTML 元素
- **THEN** 系统 SHALL 输出对应的 Markdown 格式（`##`、段落、代码块、链接）

### Requirement: Markdown 输出格式
每篇文章 SHALL 存储为一个 Markdown 文件，文件名格式为 `YYYY-MM-DD-<slug>.md`。文件 MUST 包含 YAML frontmatter：title、url、source（feed title）、feed_url（feed URL）、date、author（如有）、category、entry_id（Miniflux entry ID）、fetched_at（导出时间戳）。

#### Scenario: 标准文章输出
- **WHEN** 系统成功导出一篇文章
- **THEN** 系统 SHALL 生成一个带完整 frontmatter 的 Markdown 文件，存储在 `articles/<category>/` 目录下

#### Scenario: 文件名 slug 生成
- **WHEN** 文章标题包含特殊字符、中文或超长文本
- **THEN** 系统 SHALL 生成 URL-safe 的 slug（ASCII 字母+数字+连字符），长度不超过 80 字符

### Requirement: Category 映射
系统 SHALL 使用 Miniflux 中 feed 的 category 名称作为文章存储的子目录名。未分类的 feed SHALL 使用 `uncategorized` 作为目录名。

#### Scenario: 按分类组织文章存储
- **WHEN** 一篇文章来自 Miniflux category 为 `tech-blog` 的 feed
- **THEN** 该文章 SHALL 存储在 `articles/tech-blog/` 目录下
