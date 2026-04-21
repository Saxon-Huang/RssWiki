# rss wiki brainstorm

**Session ID:** ses_254839dd3ffeoBeWFdlZl8SQW5
**Created:** 4/20/2026, 11:22:28 PM
**Updated:** 4/21/2026, 9:53:15 PM

---

## User

我准备做一个rss订阅信源+llmWiki知识库的项目

---

## Assistant (​Sisyphus - Ultraworker · opus 4.6 · 12.5s)

_Thinking:_


The user is telling me about a project they're preparing to do - an RSS subscription feed source + LLM Wiki knowledge base project. This is in Chinese.

Let me analyze the intent:
- Surface form: "我准备做一个..." (I'm preparing to do a...)
- True intent: This is exploratory/planning - they're sharing an idea, not asking me to implement yet
- Classification: This is either seeking feedback, wanting to brainstorm, or just informing me

According to my instructions:
1. I must reply in the exact same language as the user's input (Chinese)
2. I need to check if any skills apply BEFORE responding
3. The brainstorming skill description says: "You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation."

This is clearly a case where brainstorming applies - the user is at the very beginning of a project concept. Even though they haven't explicitly asked me to implement, they're sharing a project idea which suggests they want to explore it.

According to the skill priority rules: "Let's build X" → brainstorming first, then implementation skills.

I should invoke the brainstorming skill to help explore their intent, requirements, and design before any implementation.



我看到你想做一个RSS订阅信源结合LLM Wiki知识库的项目。在我们深入讨论之前，让我先加载brainstorming技能来帮助我们更好地探索这个想法。

**Tool: skill**

**Input:**
```json
{
  "name": "brainstorming",
  "user_message": "我准备做一个rss订阅信源+llmWiki知识库的项目"
}
```

**Error:**
```
Skill or command "brainstorming" not found. Available: playwright, frontend-ui-ux, git-master, dev-browser, review-work, ai-slop-remover, /init-deep, /ralph-loop, /ulw-loop, /cancel-ralph, /refactor, /start-work, /stop-continuation, /remove-ai-slops, /handoff
```

---

## Assistant (​Sisyphus - Ultraworker · opus 4.6 · 6.7s)

你想做一个 RSS 订阅信源 + LLM Wiki 知识库的项目，这个方向很有意思。让我问几个关键问题来理解你的真实需求：

**核心问题：**

1. **数据流向** - 你的设想是：RSS 抓取文章 → LLM 处理 → 沉淀成 Wiki？还是 RSS 作为知识库的实时更新来源？

2. **Wiki 的形态** - 是类似 Obsidian 的个人知识库？还是多人协作的公开 Wiki？还是纯粹的 RAG 检索系统？

3. **LLM 的角色** -

---

## User

我先说明一下llm wiki的部分，准备使用这个项目，你可以看下他的readme 。最终的形式至少有抓取的原文档+llm知识库+可视化结构图等，这部分我们后续再讨论扩展。https://github.com/safishamsi/graphify

---

## Assistant (​Sisyphus - Ultraworker · opus 4.6 · 43.1s)

_Thinking:_

The user wants me to look at the Graphify project on GitHub to understand what it does, before we continue discussing the RSS + LLM Wiki project architecture.

I detect research/investigation intent - the user wants me to understand an external tool before proceeding with design discussions. My approach: librarian → fetch README → synthesize understanding.

Let me fetch the README from the GitHub repo.

I detect研究意图——先了解 Graphify 这个项目，再继续讨论架构。

**Tool: webfetch**

**Input:**
```json
{
  "url": "https://github.com/safishamsi/graphify",
  "format": "markdown"
}
```

**Output:**
```
                     GitHub - safishamsi/graphify: AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph · GitHub                                             

[Skip to content](#start-of-content)   

## Navigation Menu

Toggle navigation

[](/)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Fsafishamsi%2Fgraphify)

Appearance settings

  

-   Platform
    
    -   AI CODE CREATION
        
        -   [
            
            GitHub CopilotWrite better code with AI
            
            ](https://github.com/features/copilot)
        -   [
            
            GitHub SparkBuild and deploy intelligent apps
            
            ](https://github.com/features/spark)
        -   [
            
            GitHub ModelsManage and compare prompts
            
            ](https://github.com/features/models)
        -   [
            
            MCP RegistryNewIntegrate external tools
            
            ](https://github.com/mcp)
        
    -   DEVELOPER WORKFLOWS
        
        -   [
            
            ActionsAutomate any workflow
            
            ](https://github.com/features/actions)
        -   [
            
            CodespacesInstant dev environments
            
            ](https://github.com/features/codespaces)
        -   [
            
            IssuesPlan and track work
            
            ](https://github.com/features/issues)
        -   [
            
            Code ReviewManage code changes
            
            ](https://github.com/features/code-review)
        
    -   APPLICATION SECURITY
        
        -   [
            
            GitHub Advanced SecurityFind and fix vulnerabilities
            
            ](https://github.com/security/advanced-security)
        -   [
            
            Code securitySecure your code as you build
            
            ](https://github.com/security/advanced-security/code-security)
        -   [
            
            Secret protectionStop leaks before they start
            
            ](https://github.com/security/advanced-security/secret-protection)
        
    -   EXPLORE
        
        -   [Why GitHub](https://github.com/why-github)
        -   [Documentation](https://docs.github.com)
        -   [Blog](https://github.blog)
        -   [Changelog](https://github.blog/changelog)
        -   [Marketplace](https://github.com/marketplace)
        
    
    [View all features](https://github.com/features)
    
-   Solutions
    
    -   BY COMPANY SIZE
        
        -   [Enterprises](https://github.com/enterprise)
        -   [Small and medium teams](https://github.com/team)
        -   [Startups](https://github.com/enterprise/startups)
        -   [Nonprofits](https://github.com/solutions/industry/nonprofits)
        
    -   BY USE CASE
        
        -   [App Modernization](https://github.com/solutions/use-case/app-modernization)
        -   [DevSecOps](https://github.com/solutions/use-case/devsecops)
        -   [DevOps](https://github.com/solutions/use-case/devops)
        -   [CI/CD](https://github.com/solutions/use-case/ci-cd)
        -   [View all use cases](https://github.com/solutions/use-case)
        
    -   BY INDUSTRY
        
        -   [Healthcare](https://github.com/solutions/industry/healthcare)
        -   [Financial services](https://github.com/solutions/industry/financial-services)
        -   [Manufacturing](https://github.com/solutions/industry/manufacturing)
        -   [Government](https://github.com/solutions/industry/government)
        -   [View all industries](https://github.com/solutions/industry)
        
    
    [View all solutions](https://github.com/solutions)
    
-   Resources
    
    -   EXPLORE BY TOPIC
        
        -   [AI](https://github.com/resources/articles?topic=ai)
        -   [Software Development](https://github.com/resources/articles?topic=software-development)
        -   [DevOps](https://github.com/resources/articles?topic=devops)
        -   [Security](https://github.com/resources/articles?topic=security)
        -   [View all topics](https://github.com/resources/articles)
        
    -   EXPLORE BY TYPE
        
        -   [Customer stories](https://github.com/customer-stories)
        -   [Events & webinars](https://github.com/resources/events)
        -   [Ebooks & reports](https://github.com/resources/whitepapers)
        -   [Business insights](https://github.com/solutions/executive-insights)
        -   [GitHub Skills](https://skills.github.com)
        
    -   SUPPORT & SERVICES
        
        -   [Documentation](https://docs.github.com)
        -   [Customer support](https://support.github.com)
        -   [Community forum](https://github.com/orgs/community/discussions)
        -   [Trust center](https://github.com/trust-center)
        -   [Partners](https://github.com/partners)
        
    
    [View all resources](https://github.com/resources)
    
-   Open Source
    
    -   COMMUNITY
        
        -   [
            
            GitHub SponsorsFund open source developers
            
            ](https://github.com/sponsors)
        
    -   PROGRAMS
        
        -   [Security Lab](https://securitylab.github.com)
        -   [Maintainer Community](https://maintainers.github.com)
        -   [Accelerator](https://github.com/accelerator)
        -   [GitHub Stars](https://stars.github.com)
        -   [Archive Program](https://archiveprogram.github.com)
        
    -   REPOSITORIES
        
        -   [Topics](https://github.com/topics)
        -   [Trending](https://github.com/trending)
        -   [Collections](https://github.com/collections)
        
    
-   Enterprise
    
    -   ENTERPRISE SOLUTIONS
        
        -   [
            
            Enterprise platformAI-powered developer platform
            
            ](https://github.com/enterprise)
        
    -   AVAILABLE ADD-ONS
        
        -   [
            
            GitHub Advanced SecurityEnterprise-grade security features
            
            ](https://github.com/security/advanced-security)
        -   [
            
            Copilot for BusinessEnterprise-grade AI features
            
            ](https://github.com/features/copilot/copilot-business)
        -   [
            
            Premium SupportEnterprise-grade 24/7 support
            
            ](https://github.com/premium-support)
        
    
-   [Pricing](https://github.com/pricing)

Search or jump to...

# Search code, repositories, users, issues, pull requests...

Search

Clear

[Search syntax tips](https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax)

# Provide feedback

We read every piece of feedback, and take your input very seriously.

 Include my email address so I can be contacted

Cancel Submit feedback

# Saved searches

## Use saved searches to filter your results more quickly

Name  

Query 

To see all available qualifiers, see our [documentation](https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax).

Cancel Create saved search

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Fsafishamsi%2Fgraphify)

[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo&source_repo=safishamsi%2Fgraphify)

Appearance settings

Resetting focus

You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert

[safishamsi](/safishamsi) / **[graphify](/safishamsi/graphify)** Public

-   ### Uh oh!
    
    There was an error while loading. Please reload this page.
    
-   [Notifications](/login?return_to=%2Fsafishamsi%2Fgraphify) You must be signed in to change notification settings
-   [Fork 3.5k](/login?return_to=%2Fsafishamsi%2Fgraphify)
-   [Star 31.8k](/login?return_to=%2Fsafishamsi%2Fgraphify)
    

-   [Code](/safishamsi/graphify)
-   [Issues 62](/safishamsi/graphify/issues)
-   [Pull requests 101](/safishamsi/graphify/pulls)
-   [Discussions](/safishamsi/graphify/discussions)
-   [Actions](/safishamsi/graphify/actions)
-   [Projects](/safishamsi/graphify/projects)
-   [Security and quality 0](/safishamsi/graphify/security)
-   [Insights](/safishamsi/graphify/pulse)

Additional navigation options

-   [Code](/safishamsi/graphify)
-   [Issues](/safishamsi/graphify/issues)
-   [Pull requests](/safishamsi/graphify/pulls)
-   [Discussions](/safishamsi/graphify/discussions)
-   [Actions](/safishamsi/graphify/actions)
-   [Projects](/safishamsi/graphify/projects)
-   [Security and quality](/safishamsi/graphify/security)
-   [Insights](/safishamsi/graphify/pulse)

 [](/safishamsi/graphify)

# safishamsi/graphify

 v4

[Branches](/safishamsi/graphify/branches)[Tags](/safishamsi/graphify/tags)

[](/safishamsi/graphify/branches)[](/safishamsi/graphify/tags)

Go to file

Code

Open more actions menu

## Folders and files

Name

Name

Last commit message

Last commit date

## Latest commit

## History

[174 Commits](/safishamsi/graphify/commits/v4/)

[](/safishamsi/graphify/commits/v4/)174 Commits

[.github](/safishamsi/graphify/tree/v4/.github ".github")

[.github](/safishamsi/graphify/tree/v4/.github ".github")

[docs](/safishamsi/graphify/tree/v4/docs "docs")

[docs](/safishamsi/graphify/tree/v4/docs "docs")

[graphify](/safishamsi/graphify/tree/v4/graphify "graphify")

[graphify](/safishamsi/graphify/tree/v4/graphify "graphify")

[tests](/safishamsi/graphify/tree/v4/tests "tests")

[tests](/safishamsi/graphify/tree/v4/tests "tests")

[worked](/safishamsi/graphify/tree/v4/worked "worked")

[worked](/safishamsi/graphify/tree/v4/worked "worked")

[.gitignore](/safishamsi/graphify/blob/v4/.gitignore ".gitignore")

[.gitignore](/safishamsi/graphify/blob/v4/.gitignore ".gitignore")

[AGENTS.md](/safishamsi/graphify/blob/v4/AGENTS.md "AGENTS.md")

[AGENTS.md](/safishamsi/graphify/blob/v4/AGENTS.md "AGENTS.md")

[ARCHITECTURE.md](/safishamsi/graphify/blob/v4/ARCHITECTURE.md "ARCHITECTURE.md")

[ARCHITECTURE.md](/safishamsi/graphify/blob/v4/ARCHITECTURE.md "ARCHITECTURE.md")

[CHANGELOG.md](/safishamsi/graphify/blob/v4/CHANGELOG.md "CHANGELOG.md")

[CHANGELOG.md](/safishamsi/graphify/blob/v4/CHANGELOG.md "CHANGELOG.md")

[LICENSE](/safishamsi/graphify/blob/v4/LICENSE "LICENSE")

[LICENSE](/safishamsi/graphify/blob/v4/LICENSE "LICENSE")

[README.ja-JP.md](/safishamsi/graphify/blob/v4/README.ja-JP.md "README.ja-JP.md")

[README.ja-JP.md](/safishamsi/graphify/blob/v4/README.ja-JP.md "README.ja-JP.md")

[README.ko-KR.md](/safishamsi/graphify/blob/v4/README.ko-KR.md "README.ko-KR.md")

[README.ko-KR.md](/safishamsi/graphify/blob/v4/README.ko-KR.md "README.ko-KR.md")

[README.md](/safishamsi/graphify/blob/v4/README.md "README.md")

[README.md](/safishamsi/graphify/blob/v4/README.md "README.md")

[README.zh-CN.md](/safishamsi/graphify/blob/v4/README.zh-CN.md "README.zh-CN.md")

[README.zh-CN.md](/safishamsi/graphify/blob/v4/README.zh-CN.md "README.zh-CN.md")

[SECURITY.md](/safishamsi/graphify/blob/v4/SECURITY.md "SECURITY.md")

[SECURITY.md](/safishamsi/graphify/blob/v4/SECURITY.md "SECURITY.md")

[pyproject.toml](/safishamsi/graphify/blob/v4/pyproject.toml "pyproject.toml")

[pyproject.toml](/safishamsi/graphify/blob/v4/pyproject.toml "pyproject.toml")

View all files

## Repository files navigation

-   [README](#)
-   [MIT license](#)
-   [Security](#)

[![Graphify](https://raw.githubusercontent.com/safishamsi/graphify/v4/docs/logo-text.svg)](https://raw.githubusercontent.com/safishamsi/graphify/v4/docs/logo-text.svg)

[English](/safishamsi/graphify/blob/v4/README.md) | [简体中文](/safishamsi/graphify/blob/v4/README.zh-CN.md) | [日本語](/safishamsi/graphify/blob/v4/README.ja-JP.md) | [한국어](/safishamsi/graphify/blob/v4/README.ko-KR.md)

[![CI](https://github.com/safishamsi/graphify/actions/workflows/ci.yml/badge.svg?branch=v4)](https://github.com/safishamsi/graphify/actions/workflows/ci.yml) [![PyPI](https://camo.githubusercontent.com/889bc0c00c7b4d8b4af52910911e493ac6227804b15c289351631da47b5b903e/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f677261706869667979)](https://pypi.org/project/graphifyy/) [![Downloads](https://camo.githubusercontent.com/ffa2eeff3579fb956412851e23f1594e1f6444c2e5dd24077bd0b0cad3ed45ad/68747470733a2f2f7374617469632e706570792e746563682f62616467652f677261706869667979)](https://pepy.tech/project/graphifyy) [![Sponsor](https://camo.githubusercontent.com/678dddb61d8d32c4d44036397538125c36d6b220dcd6fe31aff786df14b5dfb6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f73706f6e736f722d736166697368616d73692d6561346161613f6c6f676f3d6769746875622d73706f6e736f7273)](https://github.com/sponsors/safishamsi) [![LinkedIn](https://camo.githubusercontent.com/ec82efd07da8573d39ac2bbc7b396f42aaabf435f56b812a3eb1750b380225fa/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c696e6b6564496e2d536166692532305368616d73692d3030373742353f6c6f676f3d6c696e6b6564696e)](https://www.linkedin.com/in/safi-shamsi)

**An AI coding assistant skill.** Type `/graphify` in Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro, or Google Antigravity - it reads your files, builds a knowledge graph, and gives you back structure you didn't know was there. Understand a codebase faster. Find the "why" behind architectural decisions.

Fully multimodal. Drop in code, PDFs, markdown, screenshots, diagrams, whiteboard photos, images in other languages, or video and audio files - graphify extracts concepts and relationships from all of it and connects them into one graph. Videos are transcribed with Whisper using a domain-aware prompt derived from your corpus. 25 languages supported via tree-sitter AST (Python, JS, TS, Go, Rust, Java, C, C++, Ruby, C#, Kotlin, Scala, PHP, Swift, Lua, Zig, PowerShell, Elixir, Objective-C, Julia, Verilog, SystemVerilog, Vue, Svelte, Dart).

> Andrej Karpathy keeps a `/raw` folder where he drops papers, tweets, screenshots, and notes. graphify is the answer to that problem - 71.5x fewer tokens per query vs reading the raw files, persistent across sessions, honest about what it found vs guessed.

```
/graphify .                        # works on any folder - your codebase, notes, papers, anything
```

```
graphify-out/
├── graph.html       interactive graph - open in any browser, click nodes, search, filter by community
├── GRAPH_REPORT.md  god nodes, surprising connections, suggested questions
├── graph.json       persistent graph - query weeks later without re-reading
└── cache/           SHA256 cache - re-runs only process changed files
```

Add a `.graphifyignore` file to exclude folders you don't want in the graph:

```
# .graphifyignore
vendor/
node_modules/
dist/
*.generated.py
```

Same syntax as `.gitignore`. You can keep a single `.graphifyignore` at your repo root — patterns work correctly even when graphify is run on a subfolder.

## How it works

[](#how-it-works)

graphify runs in three passes. First, a deterministic AST pass extracts structure from code files (classes, functions, imports, call graphs, docstrings, rationale comments) with no LLM needed. Second, video and audio files are transcribed locally with faster-whisper using a domain-aware prompt derived from corpus god nodes — transcripts are cached so re-runs are instant. Third, Claude subagents run in parallel over docs, papers, images, and transcripts to extract concepts, relationships, and design rationale. The results are merged into a NetworkX graph, clustered with Leiden community detection, and exported as interactive HTML, queryable JSON, and a plain-language audit report.

**Clustering is graph-topology-based — no embeddings.** Leiden finds communities by edge density. The semantic similarity edges that Claude extracts (`semantically_similar_to`, marked INFERRED) are already in the graph, so they influence community detection directly. The graph structure is the similarity signal — no separate embedding step or vector database needed.

Every relationship is tagged `EXTRACTED` (found directly in source), `INFERRED` (reasonable inference, with a confidence score), or `AMBIGUOUS` (flagged for review). You always know what was found vs guessed.

## Install

[](#install)

**Requires:** Python 3.10+ and one of: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli), [VS Code Copilot Chat](https://code.visualstudio.com/docs/copilot/overview), [Aider](https://aider.chat), [OpenClaw](https://openclaw.ai), [Factory Droid](https://factory.ai), [Trae](https://trae.ai), [Kiro](https://kiro.dev), Hermes, or [Google Antigravity](https://antigravity.google)

pip install graphifyy && graphify install
# or with pipx (keeps the CLI isolated from your project environments)
pipx install graphifyy && graphify install

> **Official package:** The PyPI package is named `graphifyy` (install with `pip install graphifyy`). Other packages named `graphify*` on PyPI are not affiliated with this project. The only official repository is [safishamsi/graphify](https://github.com/safishamsi/graphify). The CLI and skill command are still `graphify`.

> **`graphify: command not found`?** On Windows, pip user scripts land in `%APPDATA%\Python\PythonXY\Scripts` — add that to your PATH or use `python -m graphify` instead. On macOS with pipx, run `pipx ensurepath` then restart your terminal.

### Platform support

[](#platform-support)

Platform

Install command

Claude Code (Linux/Mac)

`graphify install`

Claude Code (Windows)

`graphify install` (auto-detected) or `graphify install --platform windows`

Codex

`graphify install --platform codex`

OpenCode

`graphify install --platform opencode`

GitHub Copilot CLI

`graphify install --platform copilot`

VS Code Copilot Chat

`graphify vscode install`

Aider

`graphify install --platform aider`

OpenClaw

`graphify install --platform claw`

Factory Droid

`graphify install --platform droid`

Trae

`graphify install --platform trae`

Trae CN

`graphify install --platform trae-cn`

Gemini CLI

`graphify install --platform gemini`

Hermes

`graphify install --platform hermes`

Kiro IDE/CLI

`graphify kiro install`

Cursor

`graphify cursor install`

Google Antigravity

`graphify antigravity install`

Codex users also need `multi_agent = true` under `[features]` in `~/.codex/config.toml` for parallel extraction. Factory Droid uses the `Task` tool for parallel subagent dispatch. OpenClaw and Aider use sequential extraction (parallel agent support is still early on those platforms). Trae uses the Agent tool for parallel subagent dispatch and does **not** support PreToolUse hooks — AGENTS.md is the always-on mechanism. Codex supports PreToolUse hooks — `graphify codex install` installs one in `.codex/hooks.json` in addition to writing AGENTS.md.

Then open your AI coding assistant and type:

```
/graphify .
```

Note: Codex uses `$` instead of `/` for skill calling, so type `$graphify .` instead.

### Make your assistant always use the graph (recommended)

[](#make-your-assistant-always-use-the-graph-recommended)

After building a graph, run this once in your project:

Platform

Command

Claude Code

`graphify claude install`

Codex

`graphify codex install`

OpenCode

`graphify opencode install`

GitHub Copilot CLI

`graphify copilot install`

VS Code Copilot Chat

`graphify vscode install`

Aider

`graphify aider install`

OpenClaw

`graphify claw install`

Factory Droid

`graphify droid install`

Trae

`graphify trae install`

Trae CN

`graphify trae-cn install`

Cursor

`graphify cursor install`

Gemini CLI

`graphify gemini install`

Hermes

`graphify hermes install`

Kiro IDE/CLI

`graphify kiro install`

Google Antigravity

`graphify antigravity install`

**Claude Code** does two things: writes a `CLAUDE.md` section telling Claude to read `graphify-out/GRAPH_REPORT.md` before answering architecture questions, and installs a **PreToolUse hook** (`settings.json`) that fires before every Glob and Grep call. If a knowledge graph exists, Claude sees: *"graphify: Knowledge graph exists. Read GRAPH\_REPORT.md for god nodes and community structure before searching raw files."* — so Claude navigates via the graph instead of grepping through every file.

**Codex** writes to `AGENTS.md` and also installs a **PreToolUse hook** in `.codex/hooks.json` that fires before every Bash tool call — same always-on mechanism as Claude Code.

**OpenCode** writes to `AGENTS.md` and also installs a **`tool.execute.before` plugin** (`.opencode/plugins/graphify.js` + `opencode.json` registration) that fires before bash tool calls and injects the graph reminder into tool output when the graph exists.

**Cursor** writes `.cursor/rules/graphify.mdc` with `alwaysApply: true` — Cursor includes it in every conversation automatically, no hook needed.

**Gemini CLI** copies the skill to `~/.gemini/skills/graphify/SKILL.md`, writes a `GEMINI.md` section, and installs a `BeforeTool` hook in `.gemini/settings.json` that fires before file-read tool calls — same always-on mechanism as Claude Code.

**Aider, OpenClaw, Factory Droid, Trae, and Hermes** write the same rules to `AGENTS.md` in your project root and copy the skill to the platform's global skill directory. These platforms don't support tool hooks, so AGENTS.md is the always-on mechanism.

**Kiro IDE/CLI** writes the skill to `.kiro/skills/graphify/SKILL.md` (invoked via `/graphify`) and a steering file to `.kiro/steering/graphify.md` with `inclusion: always` — Kiro injects this into every conversation automatically, no hook needed.

**Google Antigravity** writes `.agent/rules/graphify.md` (always-on rules) and `.agent/workflows/graphify.md` (registers `/graphify` as a slash command). No hook equivalent exists in Antigravity — rules are the always-on mechanism.

**GitHub Copilot CLI** copies the skill to `~/.copilot/skills/graphify/SKILL.md`. Run `graphify copilot install` to set it up.

**VS Code Copilot Chat** installs a Python-only skill (works on Windows PowerShell and macOS/Linux alike) and writes `.github/copilot-instructions.md` in your project root — VS Code reads this automatically every session, making graph context always-on without any hook mechanism. Run `graphify vscode install`. Note: this configures the chat panel in VS Code, not the Copilot CLI terminal tool.

Uninstall with the matching uninstall command (e.g. `graphify claude uninstall`).

**Always-on vs explicit trigger — what's the difference?**

The always-on hook surfaces `GRAPH_REPORT.md` — a one-page summary of god nodes, communities, and surprising connections. Your assistant reads this before searching files, so it navigates by structure instead of keyword matching. That covers most everyday questions.

`/graphify query`, `/graphify path`, and `/graphify explain` go deeper: they traverse the raw `graph.json` hop by hop, trace exact paths between nodes, and surface edge-level detail (relation type, confidence score, source location). Use them when you want a specific question answered from the graph rather than a general orientation.

Think of it this way: the always-on hook gives your assistant a map. The `/graphify` commands let it navigate the map precisely.

### Team workflows

[](#team-workflows)

`graphify-out/` is designed to be committed to git so every teammate starts with a fresh map.

**Recommended `.gitignore` additions:**

```
# commit graph outputs, ignore the extraction cache
graphify-out/cache/
```

**Shared setup:**

1.  One person runs `/graphify .` to build the initial graph and commits `graphify-out/`.
2.  Everyone else pulls — their assistant reads `GRAPH_REPORT.md` immediately with no extra steps.
3.  Install the post-commit hook (`graphify hook install`) so the graph rebuilds automatically after code changes — no LLM calls needed for code-only updates.
4.  For doc/paper changes, whoever edits the files runs `/graphify --update` to refresh semantic nodes.

**Excluding paths** — create `.graphifyignore` in your project root (same syntax as `.gitignore`). Files matching those patterns are skipped during detection and extraction.

## Using `graph.json` with an LLM

[](#using-graphjson-with-an-llm)

`graph.json` is not meant to be pasted into a prompt all at once. The useful workflow is:

1.  Start with `graphify-out/GRAPH_REPORT.md` for the high-level overview.
2.  Use `graphify query` to pull a smaller subgraph for the specific question you want to answer.
3.  Give that focused output to your assistant instead of dumping the full raw corpus.

For example, after running graphify on a project:

graphify query "show the auth flow" --graph graphify-out/graph.json
graphify query "what connects DigestAuth to Response?" --graph graphify-out/graph.json

The output includes node labels, edge types, confidence tags, source files, and source locations. That makes it a good intermediate context block for an LLM:

```
Use this graph query output to answer the question. Prefer the graph structure
over guessing, and cite the source files when possible.
```

If your assistant supports tool calling or MCP, use the graph directly instead of pasting text. graphify can expose `graph.json` as an MCP server:

python -m graphify.serve graphify-out/graph.json

That gives the assistant structured graph access for repeated queries such as `query_graph`, `get_node`, `get_neighbors`, and `shortest_path`.

> **WSL / Linux note:** Ubuntu ships `python3`, not `python`. Install into a project venv to avoid PEP 668 conflicts, and use the full venv path in your `.mcp.json`:
> 
> python3 -m venv .venv && .venv/bin/pip install "graphifyy\[mcp\]"
> 
> { "mcpServers": { "graphify": { "type": "stdio", "command": ".venv/bin/python3", "args": \["\-m", "graphify.serve", "graphify-out/graph.json"\] } } }
> 
> Also note: the PyPI package is `graphifyy` (double-y) — `pip install graphify` installs an unrelated package.

Manual install (curl)

mkdir -p ~/.claude/skills/graphify
curl -fsSL https://raw.githubusercontent.com/safishamsi/graphify/v4/graphify/skill.md \\
  \> ~/.claude/skills/graphify/SKILL.md

Add to `~/.claude/CLAUDE.md`:

```
- **graphify** (`~/.claude/skills/graphify/SKILL.md`) - any input to knowledge graph. Trigger: `/graphify`
When the user types `/graphify`, invoke the Skill tool with `skill: "graphify"` before doing anything else.
```

## Usage

[](#usage)

```
/graphify                          # run on current directory
/graphify ./raw                    # run on a specific folder
/graphify ./raw --mode deep        # more aggressive INFERRED edge extraction
/graphify ./raw --update           # re-extract only changed files, merge into existing graph
/graphify ./raw --directed          # build directed graph (preserves edge direction: source→target)
/graphify ./raw --cluster-only     # rerun clustering on existing graph, no re-extraction
/graphify ./raw --no-viz           # skip HTML, just produce report + JSON
/graphify ./raw --obsidian                          # also generate Obsidian vault (opt-in)
/graphify ./raw --obsidian --obsidian-dir ~/vaults/myproject  # write vault to a specific directory

/graphify add https://arxiv.org/abs/1706.03762        # fetch a paper, save, update graph
/graphify add https://x.com/karpathy/status/...       # fetch a tweet
/graphify add <video-url>                              # download audio, transcribe, add to graph
/graphify add https://... --author "Name"             # tag the original author
/graphify add https://... --contributor "Name"        # tag who added it to the corpus

/graphify query "what connects attention to the optimizer?"
/graphify query "what connects attention to the optimizer?" --dfs   # trace a specific path
/graphify query "what connects attention to the optimizer?" --budget 1500  # cap at N tokens
/graphify path "DigestAuth" "Response"
/graphify explain "SwinTransformer"

/graphify ./raw --watch            # auto-sync graph as files change (code: instant, docs: notifies you)
/graphify ./raw --wiki             # build agent-crawlable wiki (index.md + article per community)
/graphify ./raw --svg              # export graph.svg
/graphify ./raw --graphml          # export graph.graphml (Gephi, yEd)
/graphify ./raw --neo4j            # generate cypher.txt for Neo4j
/graphify ./raw --neo4j-push bolt://localhost:7687    # push directly to a running Neo4j instance
/graphify ./raw --mcp              # start MCP stdio server

# git hooks - platform-agnostic, rebuild graph on commit and branch switch
graphify hook install
graphify hook uninstall
graphify hook status

# always-on assistant instructions - platform-specific
graphify claude install            # CLAUDE.md + PreToolUse hook (Claude Code)
graphify claude uninstall
graphify codex install             # AGENTS.md + PreToolUse hook in .codex/hooks.json (Codex)
graphify opencode install          # AGENTS.md + tool.execute.before plugin (OpenCode)
graphify cursor install            # .cursor/rules/graphify.mdc (Cursor)
graphify cursor uninstall
graphify gemini install            # GEMINI.md + BeforeTool hook (Gemini CLI)
graphify gemini uninstall
graphify copilot install           # skill file (GitHub Copilot CLI)
graphify copilot uninstall
graphify aider install             # AGENTS.md (Aider)
graphify aider uninstall
graphify claw install              # AGENTS.md (OpenClaw)
graphify droid install             # AGENTS.md (Factory Droid)
graphify trae install              # AGENTS.md (Trae)
graphify trae uninstall
graphify trae-cn install           # AGENTS.md (Trae CN)
graphify trae-cn uninstall
graphify hermes install             # AGENTS.md + ~/.hermes/skills/ (Hermes)
graphify hermes uninstall
graphify kiro install               # .kiro/skills/ + .kiro/steering/graphify.md (Kiro IDE/CLI)
graphify kiro uninstall
graphify antigravity install       # .agent/rules + .agent/workflows (Google Antigravity)
graphify antigravity uninstall

# query and navigate the graph directly from the terminal (no AI assistant needed)
graphify query "what connects attention to the optimizer?"
graphify query "show the auth flow" --dfs
graphify query "what is CfgNode?" --budget 500
graphify query "..." --graph path/to/graph.json
graphify path "DigestAuth" "Response"       # shortest path between two nodes
graphify explain "SwinTransformer"           # plain-language explanation of a node

# add content and update the graph from the terminal
graphify add https://arxiv.org/abs/1706.03762          # fetch paper, save to ./raw, update graph
graphify add https://... --author "Name" --contributor "Name"

# incremental update and maintenance
graphify watch ./src                         # auto-rebuild on code changes
graphify update ./src                        # re-extract code files, no LLM needed
graphify cluster-only ./my-project           # rerun clustering on existing graph.json
```

Works with any mix of file types:

Type

Extensions

Extraction

Code

`.py .ts .js .jsx .tsx .mjs .go .rs .java .c .cpp .rb .cs .kt .scala .php .swift .lua .zig .ps1 .ex .exs .m .mm .jl .vue .svelte`

AST via tree-sitter + call-graph (cross-file for all languages) + docstring/comment rationale

Docs

`.md .mdx .html .txt .rst`

Concepts + relationships + design rationale via Claude

Office

`.docx .xlsx`

Converted to markdown then extracted via Claude (requires `pip install graphifyy[office]`)

Papers

`.pdf`

Citation mining + concept extraction

Images

`.png .jpg .webp .gif`

Claude vision - screenshots, diagrams, any language

Video / Audio

`.mp4 .mov .mkv .webm .avi .m4v .mp3 .wav .m4a .ogg`

Transcribed locally with faster-whisper, transcript fed into Claude extraction (requires `pip install graphifyy[video]`)

YouTube / URLs

any video URL

Audio downloaded via yt-dlp, then same Whisper pipeline (requires `pip install graphifyy[video]`)

## Video and audio corpus

[](#video-and-audio-corpus)

Drop video or audio files into your corpus folder alongside your code and docs — graphify picks them up automatically:

pip install 'graphifyy\[video\]'   # one-time setup
/graphify ./my-corpus            # transcribes any video/audio files it finds

Add a YouTube video (or any public video URL) directly:

/graphify add <video-url\>

yt-dlp downloads audio-only (fast, small), Whisper transcribes it locally, and the transcript is fed into the same extraction pipeline as your other docs. Transcripts are cached in `graphify-out/transcripts/` so re-runs skip already-transcribed files.

For better accuracy on technical content, use a larger model:

/graphify ./my-corpus --whisper-model medium

Audio never leaves your machine. All transcription runs locally.

## What you get

[](#what-you-get)

**God nodes** - highest-degree concepts (what everything connects through)

**Surprising connections** - ranked by composite score. Code-paper edges rank higher than code-code. Each result includes a plain-English why.

**Suggested questions** - 4-5 questions the graph is uniquely positioned to answer

**The "why"** - docstrings, inline comments (`# NOTE:`, `# IMPORTANT:`, `# HACK:`, `# WHY:`), and design rationale from docs are extracted as `rationale_for` nodes. Not just what the code does - why it was written that way.

**Confidence scores** - every INFERRED edge has a `confidence_score` (0.0-1.0). You know not just what was guessed but how confident the model was. EXTRACTED edges are always 1.0.

**Semantic similarity edges** - cross-file conceptual links with no structural connection. Two functions solving the same problem without calling each other, a class in code and a concept in a paper describing the same algorithm.

**Hyperedges** - group relationships connecting 3+ nodes that pairwise edges can't express. All classes implementing a shared protocol, all functions in an auth flow, all concepts from a paper section forming one idea.

**Token benchmark** - printed automatically after every run. On a mixed corpus (Karpathy repos + papers + images): **71.5x** fewer tokens per query vs reading raw files. The first run extracts and builds the graph (this costs tokens). Every subsequent query reads the compact graph instead of raw files — that's where the savings compound. The SHA256 cache means re-runs only re-process changed files.

**Auto-sync** (`--watch`) - run in a background terminal and the graph updates itself as your codebase changes. Code file saves trigger an instant rebuild (AST only, no LLM). Doc/image changes notify you to run `--update` for the LLM re-pass.

**Git hooks** (`graphify hook install`) - installs post-commit and post-checkout hooks. Graph rebuilds automatically after every commit and every branch switch. If a rebuild fails, the hook exits with a non-zero code so git surfaces the error instead of silently continuing. No background process needed.

**Wiki** (`--wiki`) - Wikipedia-style markdown articles per community and god node, with an `index.md` entry point. Point any agent at `index.md` and it can navigate the knowledge base by reading files instead of parsing JSON.

## Worked examples

[](#worked-examples)

Corpus

Files

Reduction

Output

Karpathy repos + 5 papers + 4 images

52

**71.5x**

[`worked/karpathy-repos/`](/safishamsi/graphify/blob/v4/worked/karpathy-repos)

graphify source + Transformer paper

4

**5.4x**

[`worked/mixed-corpus/`](/safishamsi/graphify/blob/v4/worked/mixed-corpus)

httpx (synthetic Python library)

6

~1x

[`worked/httpx/`](/safishamsi/graphify/blob/v4/worked/httpx)

Token reduction scales with corpus size. 6 files fits in a context window anyway, so graph value there is structural clarity, not compression. At 52 files (code + papers + images) you get 71x+. Each `worked/` folder has the raw input files and the actual output (`GRAPH_REPORT.md`, `graph.json`) so you can run it yourself and verify the numbers.

## Privacy

[](#privacy)

graphify sends file contents to your AI coding assistant's underlying model API for semantic extraction of docs, papers, and images — Anthropic (Claude Code), OpenAI (Codex), or whichever provider your platform uses. Code files are processed locally via tree-sitter AST — no file contents leave your machine for code. Video and audio files are transcribed locally with faster-whisper — audio never leaves your machine. No telemetry, usage tracking, or analytics of any kind. The only network calls are to your platform's model API during extraction, using your own API key.

## Tech stack

[](#tech-stack)

NetworkX + Leiden (graspologic) + tree-sitter + vis.js. Semantic extraction via Claude (Claude Code), GPT-4 (Codex), or whichever model your platform runs. Video transcription via faster-whisper + yt-dlp (optional, `pip install graphifyy[video]`). No Neo4j required, no server, runs entirely locally.

## Built on graphify — Penpax

[](#built-on-graphify--penpax)

[**Penpax**](https://safishamsi.github.io/penpax.ai) is the enterprise layer on top of graphify. Where graphify turns a folder of files into a knowledge graph, Penpax applies the same graph to your entire working life — continuously.

graphify

Penpax

Input

A folder of files

Browser history, meetings, emails, files, code — everything

Runs

On demand

Continuously in the background

Scope

[140 more lines truncated due to context window limit]
```

**Tool: task**

**Input:**
```json
{
  "prompt": "\nCONTEXT: A user wants to build an RSS feed + LLM Wiki knowledge base project, and plans to use \"Graphify\" (https://github.com/safishamsi/graphify) as the Wiki/knowledge graph component.\n\nGOAL: Deeply understand what Graphify does, its architecture, tech stack, API surface, and how it could integrate with an RSS feed system.\n\nREQUEST: \n1. Search the Graphify GitHub repo thoroughly - README, source code structure, key modules\n2. Understand: What input formats does it accept? What does it output? How does it process documents?\n3. Identify: Tech stack (Python? Node?), database/storage, LLM provider, graph visualization approach\n4. Look for: API endpoints, CLI commands, configuration options, extension points\n5. Return a structured summary covering: purpose, architecture, tech stack, input/output, integration points, limitations\n",
  "subagent_type": "librarian",
  "load_skills": [],
  "run_in_background": true,
  "description": "Research Graphify project"
}
```

**Output:**
```
Background task launched.

Background Task ID: bg_4d18a8b6
Description: Research Graphify project
Agent: librarian
Status: pending

System notifies on completion. Use `background_output` with task_id="bg_4d18a8b6" to check.

Do NOT call background_output now. Wait for <system-reminder> notification first.

<task_metadata>
session_id: ses_24fcf700bffewsr0iJKu22iR3B
task_id: bg_4d18a8b6
background_task_id: bg_4d18a8b6
</task_metadata>

to continue: task(session_id="ses_24fcf700bffewsr0iJKu22iR3B", load_skills=[], run_in_background=false, prompt="...")
```

---

## Assistant (​Sisyphus - Ultraworker · opus 4.6 · 21.3s)

_Thinking:_

I got the README content from the webfetch. Let me also check the current state of the user's project to understand what they have so far.

同时看下你现有项目的状态：

**Tool: read**

**Input:**
```json
{
  "filePath": "/Users/huangzechen/Developer/github/RssWiki"
}
```

**Output:**
```
<path>/Users/huangzechen/Developer/github/RssWiki</path>
<type>directory</type>
<entries>
.git/

(1 entries)
</entries>
```

---

## Assistant (​Sisyphus - Ultraworker · opus 4.6 · 305.7s)

_Thinking:_

The project is basically empty - just a git repo with nothing in it. Now I have a good understanding of Graphify from the README. Let me synthesize what I know and ask the user the right questions.

Let me summarize Graphify:
- It's an AI coding assistant skill that turns any folder of files (code, docs, papers, images, videos) into a queryable knowledge graph
- Tech stack: Python, NetworkX + Leiden clustering + tree-sitter + vis.js
- Output: graph.html (interactive visualization), GRAPH_REPORT.md (report), graph.json (queryable data), cache
- It can generate wiki articles per community, Obsidian vaults, SVG exports, Neo4j compatible output


- Uses LLM for semantic extraction of documents and images while processing code locally through AST analysis
- Supports incremental updates, watch mode, and git hooks, with every relationship tagged by type (EXTRACTED, INFERRED, AMBIGUOUS) and confidence scores

Now the user wants to combine this with RSS feeds. I have enough context from the README to have a productive conversation, so let me ask some clarifying questions about how they envision integrating RSS into this knowledge graph system.

好，我已经对 Graphify 有了清晰的理解。让我先总结一下，然后我们讨论整体架构。

## Graphify 核心能力

| 能力 | 说明 |
|---|---|
| **输入** | 代码、Markdown、PDF、图片、视频/音频、URL（论文/推文/视频） |
| **处理** | 代码→tree-sitter AST 本地解析；文档/图片→LLM 语义提取；视频→Whisper 本地转录 |
| **输出** | `graph.html`（交互式可视化）、`GRAPH_REPORT.md`（报告）、`graph.json`（可查询图谱）、Wiki（Markdown 文章） |
| **关键特性** | Leiden 社区聚类、置信度标注（EXTRACTED/INFERRED/AMBIGUOUS）、增量更新、`--watch` 自动同步、MCP server 模式 |
| **Tech Stack** | Python, NetworkX, Leiden, tree-sitter, vis.js |

你的项目目前是空仓库。现在我需要理解你对 RSS + Graphify 整合的设想：

**Tool: question**

**Input:**
```json
{
  "questions": [
    {
      "header": "数据流设计",
      "options": [
        {
          "label": "RSS → 原文存档 → Graphify",
          "description": "RSS 抓取全文保存到本地文件夹（raw/），Graphify 定期扫描生成知识图谱"
        },
        {
          "label": "RSS → 筛选/分类 → Graphify",
          "description": "先经过 LLM 筛选和分类，只有符合条件的内容才存入并建图"
        },
        {
          "description": "RSS 新文章自动触发 Graphify 的 --update 增量构建，实时更新图谱",
          "label": "RSS → 实时增量更新"
        }
      ],
      "question": "RSS 抓取的内容要如何流入 Graphify？你设想的数据流是怎样的？"
    },
    {
      "header": "RSS 信源类型",
      "options": [
        {
          "label": "技术博客/论文",
          "description": "Hacker News、ArXiv、技术博客等开发者/研究向内容"
        },
        {
          "description": "行业新闻、时事动态等信息流",
          "label": "新闻资讯"
        },
        {
          "label": "混合型",
          "description": "技术+新闻+社交媒体等多种来源混合"
        }
      ],
      "question": "你关注的 RSS 信源主要是什么领域/类型？这会影响图谱的设计。"
    },
    {
      "question": "最终产品的用户形态是什么？",
      "header": "产品形态",
      "options": [
        {
          "label": "个人知识管理工具",
          "description": "类似 Obsidian + RSS 阅读器的个人工具，本地部署"
        },
        {
          "label": "可部署的 Web 应用",
          "description": "带前端界面的 Web 服务，可以分享给他人使用"
        },
        {
          "description": "命令行工具为主，结合 Graphify 的可视化输出",
          "label": "CLI + 本地知识库"
        }
      ]
    },
    {
      "options": [
        {
          "label": "全 Python",
          "description": "统一用 Python（FastAPI/Flask + feedparser 等）"
        },
        {
          "label": "Python 后端 + TS 前端",
          "description": "Python 处理 RSS 和 Graphify，TypeScript/React 做前端"
        },
        {
          "label": "待定，听建议",
          "description": "根据需求和 Graphify 的集成方式来决定"
        }
      ],
      "question": "技术栈偏好？Graphify 本身是 Python，你的 RSS 部分想用什么？",
      "header": "技术栈"
    }
  ]
}
```

**Output:**
```
User has answered your questions: "RSS 抓取的内容要如何流入 Graphify？你设想的数据流是怎样的？"="RSS每天抓取订阅源+根据主题过滤与分类+存储原文+llm wiki加工处理", "你关注的 RSS 信源主要是什么领域/类型？这会影响图谱的设计。"="技术博客/论文", "最终产品的用户形态是什么？"="RSS抓取的部分用git cron定时执行，llm wiki作为我本地的个人知识库使用", "技术栈偏好？Graphify 本身是 Python，你的 RSS 部分想用什么？"="待定，听建议". You can now continue with the user's answers in mind.
```

---

## User

<system-reminder>
[ALL BACKGROUND TASKS COMPLETE]

**Completed:**
- `bg_4d18a8b6`: Research Graphify project

Use `background_output(task_id="<id>")` to retrieve each result.
</system-reminder>
<!-- OMO_INTERNAL_INITIATOR -->

---

## Assistant (​Sisyphus - Ultraworker · opus 4.6 · 23.2s)

**Tool: background_output**

**Input:**
```json
{
  "task_id": "bg_4d18a8b6"
}
```

**Output:**
```
Task Result

Task ID: bg_4d18a8b6
Description: Research Graphify project
Duration: 3m 51s
Session ID: ses_24fcf700bffewsr0iJKu22iR3B

---

Now let me read the cloned repo's key files in parallel:

Now let me read the key source modules:

I now have a comprehensive picture of Graphify. Here is the full structured analysis:

---

# Graphify: Deep Analysis for RSS + LLM Wiki Integration

**Commit SHA**: `0ee7e8bf04a976e043a1d7d305963f88b0f26fec`  
**Source**: [safishamsi/graphify](https://github.com/safishamsi/graphify/tree/v4)

---

## 1. Purpose

Graphify is **not a traditional wiki** — it is an **AI coding assistant skill** that turns any folder of files into a queryable knowledge graph. It is designed to be invoked inside AI assistants (Claude Code, OpenCode, Cursor, etc.) via `/graphify .`, and it produces a persistent, structured graph that the assistant can navigate instead of grepping raw files.

The tagline: *"71.5x fewer tokens per query vs reading raw files."*

---

## 2. Architecture

The pipeline is a strict linear sequence of pure functions with no shared state:

```
detect() → extract() → build_graph() → cluster() → analyze() → report() → export()
```

**Evidence** ([ARCHITECTURE.md](https://github.com/safishamsi/graphify/blob/0ee7e8bf04a976e043a1d7d305963f88b0f26fec/ARCHITECTURE.md#L8)):
```
detect()  →  extract()  →  build_graph()  →  cluster()  →  analyze()  →  report()  →  export()
```

Each stage is a single function in its own module. They communicate through plain Python dicts and NetworkX graphs — no shared state, no side effects outside `graphify-out/`.

### Module Responsibilities

| Module | Function | Role |
|--------|----------|------|
| `detect.py` | `collect_files(root)` | Directory → filtered `[Path]` list |
| `extract.py` | `extract(path)` | File → `{nodes, edges}` dict (AST for code, LLM for docs/images) |
| `build.py` | `build_graph(extractions)` | List of extraction dicts → `nx.Graph` |
| `cluster.py` | `cluster(G)` | Graph → graph with `community` attr on each node |
| `analyze.py` | `analyze(G)` | Graph → analysis dict (god nodes, surprises, questions) |
| `report.py` | `render_report(G, analysis)` | Graph + analysis → `GRAPH_REPORT.md` string |
| `export.py` | `export(G, out_dir, ...)` | Graph → Obsidian vault, `graph.json`, `graph.html`, `graph.svg` |
| `ingest.py` | `ingest(url, ...)` | URL → file saved to corpus dir |
| `cache.py` | `check_semantic_cache / save_semantic_cache` | SHA256 cache for incremental re-runs |
| `serve.py` | `serve(graph_path)` | `graph.json` → MCP stdio server |
| `watch.py` | `watch(root, flag_path)` | Directory → writes flag file on change |
| `transcribe.py` | *(video/audio)* | faster-whisper transcription pipeline |

---

## 3. Tech Stack

**Evidence** ([pyproject.toml](https://github.com/safishamsi/graphify/blob/0ee7e8bf04a976e043a1d7d305963f88b0f26fec/pyproject.toml)):

| Layer | Technology |
|-------|-----------|
| **Language** | Python 3.10+ |
| **Graph engine** | NetworkX |
| **Community detection** | Leiden algorithm via `graspologic` |
| **Code parsing** | tree-sitter (25 languages) |
| **Graph visualization** | vis.js (interactive HTML) |
| **LLM provider** | Whichever AI assistant runs the skill (Claude, GPT-4, Gemini, etc.) — **no hardcoded API key** |
| **Video transcription** | faster-whisper + yt-dlp (optional) |
| **MCP server** | `mcp` package (optional) |
| **Storage** | Local filesystem only — `graphify-out/` directory |
| **Database** | None required (Neo4j optional export) |
| **Package name** | `graphifyy` (double-y) on PyPI |

**No vector database. No embeddings. No server.** Clustering is purely graph-topology-based (Leiden on edge density).

---

## 4. Input Formats

**Evidence** ([README.md](https://github.com/safishamsi/graphify/blob/0ee7e8bf04a976e043a1d7d305963f88b0f26fec/README.md)):

| Type | Extensions | Extraction Method |
|------|-----------|-------------------|
| **Code** | `.py .ts .js .jsx .tsx .mjs .go .rs .java .c .cpp .rb .cs .kt .scala .php .swift .lua .zig .ps1 .ex .exs .m .mm .jl .vue .svelte` | Deterministic AST via tree-sitter — **no LLM needed** |
| **Docs** | `.md .mdx .html .txt .rst` | Concepts + relationships via LLM |
| **Office** | `.docx .xlsx` | Converted to markdown → LLM (requires `pip install graphifyy[office]`) |
| **Papers** | `.pdf` | Citation mining + concept extraction via LLM |
| **Images** | `.png .jpg .webp .gif` | Claude vision (screenshots, diagrams, any language) |
| **Video/Audio** | `.mp4 .mov .mkv .webm .avi .m4v .mp3 .wav .m4a .ogg` | Local Whisper transcription → LLM |
| **URLs** | Any video URL, arXiv, tweets | `graphify add <url>` fetches and ingests |

**RSS feeds are not a native input format.** RSS XML would need to be pre-processed into `.md` or `.txt` files before graphify can consume them.

---

## 5. Output Formats

**Evidence** ([README.md](https://github.com/safishamsi/graphify/blob/0ee7e8bf04a976e043a1d7d305963f88b0f26fec/README.md)):

```
graphify-out/
├── graph.html       # Interactive vis.js graph — open in browser, click nodes, search, filter
├── GRAPH_REPORT.md  # God nodes, surprising connections, suggested questions (plain text)
├── graph.json       # Persistent NetworkX node-link JSON — queryable weeks later
└── cache/           # SHA256 cache — re-runs only process changed files
```

Optional exports:
- `graph.svg` — static SVG (`--svg`)
- `graph.graphml` — for Gephi/yEd (`--graphml`)
- `cypher.txt` — Neo4j import (`--neo4j`)
- `wiki/` — Wikipedia-style markdown articles per community (`--wiki`)
- Obsidian vault (`--obsidian`)

---

## 6. Extraction Output Schema

Every extractor returns a standardized dict:

**Evidence** ([ARCHITECTURE.md L36-L44](https://github.com/safishamsi/graphify/blob/0ee7e8bf04a976e043a1d7d305963f88b0f26fec/ARCHITECTURE.md#L36-L44)):
```json
{
  "nodes": [
    {"id": "unique_string", "label": "human name", "source_file": "path", "source_location": "L42"}
  ],
  "edges": [
    {"source": "id_a", "target": "id_b", "relation": "calls|imports|uses|...", "confidence": "EXTRACTED|INFERRED|AMBIGUOUS"}
  ]
}
```

Confidence labels:
- `EXTRACTED` — explicitly stated in source (import, direct call)
- `INFERRED` — reasonable deduction with `confidence_score` (0.0–1.0)
- `AMBIGUOUS` — uncertain, flagged for human review

---

## 7. API Surface

### CLI Commands

```bash
# Build graph
graphify .                          # current directory
graphify ./raw --mode deep          # aggressive INFERRED edge extraction
graphify ./raw --update             # incremental re-extract changed files only
graphify ./raw --directed           # directed graph
graphify ./raw --no-viz             # skip HTML, just JSON + report
graphify ./raw --wiki               # generate agent-crawlable wiki
graphify ./raw --obsidian           # generate Obsidian vault

# Ingest URLs
graphify add https://arxiv.org/abs/1706.03762
graphify add <video-url>

# Query
graphify query "what connects attention to the optimizer?"
graphify query "show the auth flow" --dfs
graphify path "DigestAuth" "Response"
graphify explain "SwinTransformer"

# Maintenance
graphify watch ./src                # auto-rebuild on code changes
graphify update ./src               # re-extract code (no LLM)
graphify cluster-only ./project     # rerun clustering only
graphify benchmark                  # measure token reduction

# Git hooks
graphify hook install               # post-commit + post-checkout hooks
```

### MCP Server API

**Evidence** ([serve.py L164-L235](https://github.com/safishamsi/graphify/blob/0ee7e8bf04a976e043a1d7d305963f88b0f26fec/graphify/serve.py#L164-L235)):

```bash
python -m graphify.serve graphify-out/graph.json
```

Exposes 7 MCP tools:

| Tool | Description |
|------|-------------|
| `query_graph` | BFS/DFS traversal with natural language question |
| `get_node` | Full details for a node by label/ID |
| `get_neighbors` | All direct neighbors with edge details, optional relation filter |
| `get_community` | All nodes in a community by ID |
| `god_nodes` | Top-N most connected nodes |
| `graph_stats` | Node count, edge count, communities, confidence breakdown |
| `shortest_path` | Shortest path between two concepts |

---

## 8. Configuration Options

- **`.graphifyignore`** — gitignore-syntax exclusion file (vendor/, node_modules/, etc.)
- **`--mode deep`** — more aggressive INFERRED edge extraction
- **`--directed`** — preserve edge direction
- **`--whisper-model medium`** — larger Whisper model for better accuracy
- **`--budget N`** — cap query output at N tokens
- **`--obsidian-dir ~/vaults/myproject`** — custom Obsidian vault path
- **`--graph path/to/graph.json`** — use a specific graph file

---

## 9. Integration Points for RSS + LLM Wiki

### What Graphify Does Well for This Use Case

| Capability | Relevance |
|-----------|-----------|
| **`--wiki` mode** | Generates Wikipedia-style markdown articles per community with `index.md` — directly usable as a wiki |
| **MCP server** | `query_graph`, `shortest_path`, `get_neighbors` give structured graph access to any LLM |
| **`graph.json`** | Persistent, queryable — survives across sessions without re-reading raw files |
| **`graphify add <url>`** | Can ingest URLs directly — RSS items could be fetched and added |
| **Incremental updates** | `--update` re-processes only changed files; `--watch` auto-rebuilds on code changes |
| **Confidence tagging** | Every edge is EXTRACTED/INFERRED/AMBIGUOUS — LLM knows what was found vs guessed |

### Integration Architecture for RSS + Graphify

```
RSS Feed → Parse items → Save as .md files in corpus/ → graphify update corpus/
                                                              ↓
                                                    graphify-out/graph.json
                                                    graphify-out/wiki/index.md
                                                              ↓
                                              MCP server → LLM queries graph
```

**Concrete steps:**
1. RSS poller fetches new items, saves each as `corpus/YYYY-MM-DD-title.md`
2. Run `graphify update ./corpus` (AST-free for markdown, uses LLM for concept extraction)
3. Serve `graphify-out/graph.json` via MCP: `python -m graphify.serve graphify-out/graph.json`
4. LLM queries via `query_graph`, `shortest_path`, `get_neighbors`
5. Optionally serve `graphify-out/wiki/` as a static wiki site

---

## 10. Limitations

| Limitation | Detail |
|-----------|--------|
| **No native RSS input** | RSS XML must be pre-converted to `.md`/`.txt` |
| **LLM dependency for docs** | Markdown/PDF/image extraction requires an AI assistant session — not a standalone API call |
| **No REST API** | Only MCP stdio server and CLI; no HTTP API |
| **Leiden requires Python < 3.13** | `graspologic` has a version constraint |
| **No built-in search** | `query_graph` is keyword-scored BFS/DFS, not semantic vector search |
| **No embeddings** | Clustering is topology-based; semantic similarity comes from LLM-extracted edges, not cosine similarity |
| **Single-user, local-first** | Designed for one developer's machine; team sharing requires committing `graphify-out/` to git |
| **Token cost on first run** | Initial extraction of docs/images costs LLM tokens; subsequent runs use SHA256 cache |
| **`graphify add` is sequential** | URL ingestion is one-at-a-time; no batch RSS import |

---

## Summary

Graphify is a **knowledge graph builder for AI assistants**, not a traditional wiki engine. Its strongest fit for an RSS + LLM Wiki project is:

1. **As the graph layer**: Convert RSS article text → `graph.json` → queryable knowledge graph
2. **As the wiki generator**: `--wiki` mode produces navigable markdown articles per topic cluster
3. **As an MCP server**: Expose the graph to any LLM via `query_graph`, `shortest_path`, etc.

The key gap: **RSS ingestion is not built-in**. You'd write a small RSS-to-markdown pipeline that feeds files into graphify's corpus directory, then trigger `graphify update` after each batch.
```

---

## Assistant (​Sisyphus - Ultraworker · opus 4.6 · 98.8s)

<thinking>
Now I have all the information I need. Let me synthesize everything and present a clear architecture proposal to the user.

The user wants:
1. RSS feeds → daily cron job to fetch tech blogs/papers
2. Filter by topic + classify
3. Store original text
4. LLM wiki processing via Graphify
5. Local personal knowledge base
6. Visualized structure graph

Key integration challenges:
- Graphify has no native RSS input → need an RSS-to-markdown pipeline
- Graphify's LLM extraction requires an AI assistant session, not standalone API call
- `graphify add <url>` is sequential, no batch import
- Need a filtering/classification step before feeding into Graphify

Architecture:
1. **RSS Fetcher** (Python, cron/GitHub Actions): feedparser + requests to fetch RSS, save raw articles
2. **Filter/Classifier**: LLM-based or keyword-based topic filtering
3. **Markdown Converter**: Convert articles to structured .md files in a corpus directory
4. **Graphify Integration**: Run `graphify update` on the corpus, generate wiki + graph
5. **Storage**: Git-based, `graphify-out/` committed to repo

Tech stack recommendation: All Python since Graphify is Python
- feedparser for RSS parsing
- newspaper3k or trafilatura for article extraction
- Python scripts for orchestration
- GitHub Actions or local cron for scheduling
- Graphify for knowledge graph + wiki

Let me present this cleanly to the user.
</thinking>

Librarian 的深度分析也回来了。现在我对全貌很清楚了，综合你的回答来聊架构。

---

## 你的需求画像

| 维度 | 你的选择 |
|---|---|
| **数据流** | RSS 每天抓取 → 按主题过滤分类 → 存储原文 → Graphify 生成知识图谱 |
| **信源** | 技术博客 / 论文 |
| **形态** | RSS 部分用 Git cron 自动化，Graphify 作为本地个人知识库 |
| **最终产出** | 原文档 + LLM 知识图谱 + 可视化结构图 |

## 关键发现（来自 Graphify 深度分析）

**Graphify 能做的：**
- `--wiki` 模式：按社区聚类自动生成 Wikipedia 风格的 Markdown 文章 ✅
- `graph.html`：交互式 vis.js 可视化图谱 ✅
- 增量更新 `--update`：只处理变化的文件，SHA256 缓存 ✅
- MCP server：暴露 `query_graph`、`shortest_path` 等结构化查询接口 ✅

**Graphify 做不到的（需要我们补的）：**
- ❌ 没有原生 RSS 输入能力 → 需要 RSS→Markdown 管道
- ❌ `graphify add <url>` 是逐条串行的 → 需要批量入库逻辑
- ❌ 没有过滤/分类能力 → 需要 LLM 或关键词预筛选
- ❌ LLM 提取依赖 AI assistant session → 自动化有限制

## 建议架构

```
┌─────────────────────────────────────────────────────────────────┐
│  GitHub Actions / local cron (每日定时)                          │
│                                                                 │
│  ┌──────────┐    ┌──────────────┐    ┌───────────────────┐      │
│  │ RSS 抓取  │───▶│ 过滤 & 分类   │───▶│ 存储为 Markdown   │      │
│  │feedparser │    │ 关键词/LLM   │    │ corpus/YYYY-MM-DD │      │
│  └──────────┘    └──────────────┘    └─────────┬─────────┘      │
│                                                │                │
│                                     ┌──────────▼──────────┐     │
│                                     │   graphify update    │     │
│                                     │   --wiki --update    │     │
│                                     └──────────┬──────────┘     │
│                                                │                │
└────────────────────────────────────────────────│────────────────┘
                                                 │
                                      ┌──────────▼──────────┐
                                      │   graphify-out/      │
                                      │  ├── graph.html      │  ← 交互式可视化
                                      │  ├── graph.json      │  ← 可查询图谱
                                      │  ├── GRAPH_REPORT.md │  ← 概览报告
                                      │  └── wiki/           │  ← 知识库文章
                                      └─────────────────────┘
```

## 技术栈建议

全 Python，理由：Graphify 本身是 Python，RSS 处理生态 Python 最成熟。

| 组件 | 库 | 作用 |
|---|---|---|
| RSS 解析 | `feedparser` | 解析 RSS/Atom feeds |
| 全文提取 | `trafilatura` | 从 URL 抓取正文（去广告/导航） |
| 过滤分类 | 关键词规则 + 可选 LLM | 按主题过滤不相关内容 |
| 定时任务 | GitHub Actions cron | 每天自动运行，结果 commit 回仓库 |
| 知识图谱 | `graphifyy` | 图谱构建 + Wiki 生成 + 可视化 |

## 一个关键问题

Graphify 的 LLM 提取（把 Markdown 变成知识图谱节点）**需要在 AI assistant session 里运行**（比如 Claude Code / OpenCode 里输入 `/graphify`），它不是一个能完全无人值守的 API。这意味着：

- **方案 A**：RSS 抓取 + 存储完全自动化（cron），Graphify 部分你定期手动触发 `/graphify --update`
- **方案 B**：用 Graphify 的 CLI + 配置 API key 做半自动化（需要看 Graphify 是否支持非交互模式调用 LLM）

你想先从哪部分开始？还有你对这个架构有什么想法或调整？

---

## User

你已经了解我的功能设想，在设计方案之前，你先做下调研，看看有哪些产品/组件可以参考。提醒下你，我们的重要原则是，以学习和个人使用为目的，多参考优秀的开源项目，减少自己造轮子

---

## Assistant (​Sisyphus - Ultraworker · opus 4.6 · 63.1s)



我检测到研究意图——在设计方案前先广泛调研现有开源项目和组件。启动多路并行调研。

**Tool: task**

**Input:**
```json
{
  "subagent_type": "librarian",
  "load_skills": [],
  "run_in_background": true,
  "description": "RSS聚合+知识管理开源项目",
  "prompt": "CONTEXT: I'm researching open-source projects for building a personal RSS feed aggregator + LLM-powered knowledge base system. The user wants to: 1) Subscribe to RSS feeds (tech blogs, papers), 2) Auto-fetch and filter/classify articles by topic, 3) Store original articles, 4) Build a knowledge graph with LLM processing, 5) Generate visual structure graphs and wiki-style pages.\n\nGOAL: Find the best existing open-source projects that solve parts of this problem, so we can compose them instead of building from scratch.\n\nREQUEST: Search for and analyze these categories of projects:\n\n1. **Self-hosted RSS readers/aggregators** - projects like Miniflux, FreshRSS, Tiny Tiny RSS, etc. Focus on:\n   - Which ones have good APIs for programmatic access?\n   - Which support filtering/classification features?\n   - Which are most actively maintained?\n   - Which are lightweight enough for personal use?\n\n2. **RSS + AI/LLM integration projects** - any project that combines RSS feeds with LLM processing (summarization, classification, knowledge extraction). Search GitHub for repos combining RSS with AI/LLM.\n\n3. **Personal knowledge management with LLM** - projects that use LLMs to build personal knowledge bases from collected content (not just note-taking apps, but ones that auto-process and structure knowledge).\n\nFor each project found, report: name, GitHub URL, stars, last update, tech stack, key features, and how it could fit into our architecture. Prioritize projects with 100+ stars and recent activity (2024-2025)."
}
```

**Output:**
```
Background task launched.

Background Task ID: bg_7057fef4
Description: RSS聚合+知识管理开源项目
Agent: librarian
Status: pending

System notifies on completion. Use `background_output` with task_id="bg_7057fef4" to check.

Do NOT call background_output now. Wait for <system-reminder> notification first.

<task_metadata>
session_id: ses_24fc12d56ffesPVEA2whNqyDGM
task_id: bg_7057fef4
background_task_id: bg_7057fef4
</task_metadata>

to continue: task(session_id="ses_24fc12d56ffesPVEA2whNqyDGM", load_skills=[], run_in_background=false, prompt="...")
```

**Tool: task**

**Input:**
```json
{
  "subagent_type": "librarian",
  "load_skills": [],
  "run_in_background": true,
  "description": "RSS全文提取和内容处理工具链",
  "prompt": "CONTEXT: I'm building an RSS feed aggregator that needs to fetch full article content from RSS feeds (which often only provide summaries), convert them to clean markdown, and store them for further LLM processing.\n\nGOAL: Find the best open-source tools and libraries for the RSS content pipeline: feed parsing → full article extraction → markdown conversion → storage.\n\nREQUEST: Research these specific areas:\n\n1. **RSS/Atom feed parsers** - Compare feedparser, atoma, reader (Python RSS reader), and any other modern alternatives. Which handles edge cases best? Which is most maintained?\n\n2. **Full article extraction / web scraping** - Compare trafilatura, newspaper3k/newspaper4k, readability-lxml, mozilla/readability, and similar tools. Focus on:\n   - Accuracy of content extraction (removing ads, nav, etc.)\n   - Markdown output quality\n   - Handling of tech blog formats\n   - Active maintenance status\n\n3. **RSS-to-markdown pipelines** - Any existing project that already does RSS → clean markdown conversion as a pipeline.\n\n4. **Content deduplication** - Tools or approaches for detecting duplicate/near-duplicate articles across RSS feeds.\n\n5. **Article metadata extraction** - Tools for extracting author, date, tags, categories from articles.\n\nFor each tool, report: name, GitHub URL/PyPI, stars, maintenance status, and a concrete assessment of whether we should use it."
}
```

**Output:**
```
Background task launched.

Background Task ID: bg_2814c26e
Description: RSS全文提取和内容处理工具链
Agent: librarian
Status: pending

System notifies on completion. Use `background_output` with task_id="bg_2814c26e" to check.

Do NOT call background_output now. Wait for <system-reminder> notification first.

<task_metadata>
session_id: ses_24fc1058dffegLYPTvlAr5zmRL
task_id: bg_2814c26e
background_task_id: bg_2814c26e
</task_metadata>

to continue: task(session_id="ses_24fc1058dffegLYPTvlAr5zmRL", load_skills=[], run_in_background=false, prompt="...")
```

**Tool: task**

**Input:**
```json
{
  "subagent_type": "librarian",
  "load_skills": [],
  "run_in_background": true,
  "description": "知识图谱可视化和LLM知识库方案",
  "prompt": "CONTEXT: I'm building a personal knowledge base from RSS feeds using Graphify (https://github.com/safishamsi/graphify) as the knowledge graph engine. Graphify outputs graph.json (NetworkX), graph.html (vis.js), wiki markdown, and has an MCP server. I need to research complementary tools for visualization, querying, and the overall knowledge management workflow.\n\nGOAL: Find open-source projects that complement Graphify or provide alternative/better approaches for specific parts of the knowledge pipeline.\n\nREQUEST: Research these areas:\n\n1. **Knowledge graph visualization** - Beyond vis.js (which Graphify uses), what other open-source graph visualization tools exist? Compare: Cytoscape.js, D3-force, Sigma.js, Gephi, Neo4j Browser, Obsidian graph view. Focus on interactive web-based options.\n\n2. **LLM-powered knowledge base builders** - Projects like:\n   - Khoj (https://github.com/khoj-ai/khoj) - AI personal assistant with knowledge base\n   - Quivr (https://github.com/QuivrHQ/quivr) - AI second brain\n   - Anything similar that auto-processes documents into structured knowledge\n\n3. **Graph-based note/knowledge tools** - Obsidian, Logseq, Foam, or any tool that uses graph structures for knowledge organization. Can any of these be programmatically fed from RSS?\n\n4. **Automated wiki generators** - Tools that auto-generate wiki pages from structured data or documents. Especially anything that works with markdown.\n\n5. **RSS + knowledge graph** - Any project specifically combining RSS feeds with knowledge graphs or semantic networks.\n\nFor each: name, URL, stars, tech stack, key differentiator, and how it fits (or doesn't) with our Graphify-based approach."
}
```

**Output:**
```
Background task launched.

Background Task ID: bg_82a676f9
Description: 知识图谱可视化和LLM知识库方案
Agent: librarian
Status: pending

System notifies on completion. Use `background_output` with task_id="bg_82a676f9" to check.

Do NOT call background_output now. Wait for <system-reminder> notification first.

<task_metadata>
session_id: ses_24fc0e1b1ffeA4RuB9e2IBfdYf
task_id: bg_82a676f9
background_task_id: bg_82a676f9
</task_metadata>

to continue: task(session_id="ses_24fc0e1b1ffeA4RuB9e2IBfdYf", load_skills=[], run_in_background=false, prompt="...")
```

**Tool: task**

**Input:**
```json
{
  "description": "GitHub Actions自动化RSS工作流",
  "prompt": "CONTEXT: The user wants to run RSS feed fetching on a cron schedule using GitHub Actions, commit results back to the repo, and trigger downstream processing (Graphify knowledge graph building). This is a git-based automation workflow.\n\nGOAL: Find existing open-source projects and GitHub Actions workflows that automate RSS fetching, content archival, or knowledge base updates via CI/CD.\n\nREQUEST: Research these areas:\n\n1. **GitHub Actions + RSS** - Search for repos/actions that use GitHub Actions to:\n   - Fetch RSS feeds on a schedule\n   - Archive articles to git\n   - Generate static content from RSS\n   - Examples: osmos::feed, RSSHub, RSS-to-Telegram-Bot, or similar\n\n2. **RSSHub** (https://github.com/DIYgod/RSSHub) - Deep dive:\n   - Can it be used as a library/component rather than a full service?\n   - Does it support custom output formats?\n   - How does its RSS route system work?\n\n3. **RSS archival projects** - Projects that archive RSS content for long-term storage (like ArchiveBox but RSS-focused).\n\n4. **Git-based knowledge management** - Projects that use git as the storage backend for a knowledge base (similar to how Graphify commits graphify-out/ to git).\n\n5. **Cron-based content pipelines** - Any project that demonstrates a good pattern for scheduled content fetching → processing → git commit workflow.\n\nFor each: name, URL, stars, tech stack, and specific assessment of how it fits our GitHub Actions cron + git storage approach.",
  "subagent_type": "librarian",
  "load_skills": [],
  "run_in_background": true
}
```

**Output:**
```
Background task launched.

Background Task ID: bg_29287ba8
Description: GitHub Actions自动化RSS工作流
Agent: librarian
Status: pending

System notifies on completion. Use `background_output` with task_id="bg_29287ba8" to check.

Do NOT call background_output now. Wait for <system-reminder> notification first.

<task_metadata>
session_id: ses_24fc0e1afffeJvV6VQkpjo1iIs
task_id: bg_29287ba8
background_task_id: bg_29287ba8
</task_metadata>

to continue: task(session_id="ses_24fc0e1afffeJvV6VQkpjo1iIs", load_skills=[], run_in_background=false, prompt="...")
```

---

## Assistant (​Sisyphus - Ultraworker · opus 4.6 · 18.7s)

已经派出 4 路 Librarian 并行调研：

1. **RSS 聚合 + 知识管理开源项目**（Miniflux、FreshRSS 等 + RSS+AI 整合项目）
2. **RSS 全文提取工具链**（feedparser、trafilatura、newspaper4k 等对比）
3. **知识图谱可视化 + LLM 知识库方案**（Khoj、Quivr、Obsidian 生态等）
4. **GitHub Actions 自动化 RSS 工作流**（RSSHub、ArchiveBox、git-based 方案）

等结果回来后我会整理一份完整的调研报告。

---

## User

<system-reminder>
[BACKGROUND TASK ERROR]
**ID:** `bg_7057fef4`
**Description:** RSS聚合+知识管理开源项目
**Duration:** 3m 6s
**Error:** 预扣费额度失败, 用户剩余额度: ＄0.289812, 需要预扣费额度: ＄0.309144 (request id: 202604211336265535638278268d9d6JdU0zN69)

**3 tasks still in progress.** You WILL be notified when ALL complete.
**ACTION REQUIRED:** This task failed. Check the error and decide whether to retry, cancel remaining tasks, or continue.

Use `background_output(task_id="bg_7057fef4")` to retrieve this result when ready.
</system-reminder>
<!-- OMO_INTERNAL_INITIATOR -->

---

## Assistant (​Sisyphus - Ultraworker · opus 4.6 · 59.7s)

---

## User

<system-reminder>
[BACKGROUND TASK ERROR]
**ID:** `bg_2814c26e`
**Description:** RSS全文提取和内容处理工具链
**Duration:** 4m 8s
**Error:** 预扣费额度失败, 用户剩余额度: ＄0.134688, 需要预扣费额度: ＄0.324774 (request id: 202604211337392217995178268d9d6HPqAwDtl)

**2 tasks still in progress.** You WILL be notified when ALL complete.
**ACTION REQUIRED:** This task failed. Check the error and decide whether to retry, cancel remaining tasks, or continue.

Use `background_output(task_id="bg_2814c26e")` to retrieve this result when ready.
</system-reminder>
<!-- OMO_INTERNAL_INITIATOR -->

---

## Assistant (​Sisyphus - Ultraworker · opus 4.6 · 4.1s)

---

## User

<system-reminder>
[BACKGROUND TASK COMPLETED]
**ID:** `bg_29287ba8`
**Description:** GitHub Actions自动化RSS工作流
**Duration:** 4m 30s

**1 task still in progress.** You WILL be notified when ALL complete.
Do NOT poll - continue productive work.

Use `background_output(task_id="bg_29287ba8")` to retrieve this result when ready.
</system-reminder>
<!-- OMO_INTERNAL_INITIATOR -->

---

## User

我充钱了，继续

---

## Assistant (​Sisyphus - Ultraworker · opus 4.6 · 45.4s)



<thinking>
The user has added more credits. Let me collect the results from the completed tasks and check the status of remaining ones. Two tasks failed due to insufficient credits, one completed successfully, and one is still in progress. Let me collect what's available and retry the failed ones.
</thinking>

先收已完成的结果，同时重试失败的两个任务。

**Tool: background_output**

**Input:**
```json
{
  "task_id": "bg_29287ba8"
}
```

**Output:**
```
Task Result

Task ID: bg_29287ba8
Description: GitHub Actions自动化RSS工作流
Duration: 4m 30s
Session ID: ses_24fc0e1afffeJvV6VQkpjo1iIs

---

I'll research these areas comprehensively. Let me run multiple searches in parallel.

Now let me get deeper details on the most relevant projects:

Here's the comprehensive research report:

---

# RSS + GitHub Actions Automation: Research Report

## TL;DR for Your Use Case

Your pattern — **cron → fetch RSS → process → git commit → trigger downstream** — is well-established. The canonical building block is `stefanzweifel/git-auto-commit-action` (2.5k ⭐) paired with a custom fetch script. The closest full-system analog to what you're building is **Pulsar** (RSS → LLM → Markdown → GitHub Contents API push).

---

## 1. GitHub Actions + RSS: Existing Actions & Patterns

### `stefanzweifel/git-auto-commit-action` ⭐ 2,519
**URL**: https://github.com/stefanzweifel/git-auto-commit-action  
**Tech**: Shell, Node.js  
**Last push**: March 2026 (actively maintained)

The de facto standard for the "fetch something → commit result back to repo" pattern. Used in virtually every RSS-to-git workflow found in the wild.

```yaml
- uses: stefanzweifel/git-auto-commit-action@v7
  with:
    commit_message: 'chore: update RSS feed data'
    file_pattern: 'data/*.json'
```

**Fit**: This is the commit-back primitive you'll use. Handles dirty-check (no empty commits), configurable file patterns, outputs `changes_detected` boolean you can use to conditionally trigger downstream jobs.

---

### `Promptly-Technologies-LLC/rss-fetch-action` 
**URL**: https://github.com/Promptly-Technologies-LLC/rss-fetch-action  
**Tech**: TypeScript  
**Pattern**: Fetch RSS → save to JSON → commit via `git-auto-commit-action`

```yaml
- uses: Promptly-Technologies-LLC/rss-fetch-action@v2
  with:
    feed_url: 'https://example.com/rss'
    file_path: './feed.json'
    remove_published: true  # deduplication
- uses: stefanzweifel/git-auto-commit-action@v4
  with:
    commit_message: 'Update RSS feed'
    file_pattern: '*.json'
```

**Fit**: Drop-in for single-feed fetch → JSON → commit. `remove_published: true` handles deduplication. Limited to one feed per step; you'd need multiple steps or a wrapper script for multi-feed.

---

### `robdel12/rss-checker@v1.0.0`
**URL**: https://github.com/robdel12/rss-checker  
**Pattern**: Multi-feed monitoring → commit `lastPublished.json` state → fail job on new content (for notification)

```yaml
- uses: robdel12/rss-checker@v1.0.0
  with:
    rss-feeds: |
      https://example.com/feed1
      https://example.com/feed2
    commit-directory: 'path/to/state/dir'
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

**Fit**: Designed for monitoring/alerting, not archival. Commits a state file to track "last seen" — useful pattern for deduplication logic.

---

### `llun/feeds` (FeedsFetcher Action) ⭐ 39
**URL**: https://github.com/llun/feeds  
**Tech**: TypeScript/JavaScript, Next.js, Node.js 24  
**Last push**: March 2026

GitHub Action that reads an OPML file, fetches all feeds, stores content in a `contents` branch (JSON tree or SQLite), and builds a static site via GitHub Pages.

```yaml
- uses: llun/feeds@4.0.0
  with:
    storageType: files   # or sqlite
    opmlFile: site.opml
    branch: public
```

**Fit**: Good reference for the OPML → multi-feed fetch → branch-commit pattern. The `storageType: files` mode stores everything as a JSON tree in git — directly analogous to your `graphify-out/` approach. **Not designed for downstream triggering**, but the branch-push naturally triggers `push` events.

---

### `osmoscraft/osmosfeed` ⭐ 994
**URL**: https://github.com/osmoscraft/osmosfeed  
**Tech**: TypeScript, Handlebars  
**Last release**: June 2022 (unmaintained since)

Full RSS reader running entirely from GitHub repo. Cron → fetch → build static HTML → push to `gh-pages`. Uses a `cache.json` in the `gh-pages` branch as persistent state across runs.

**Fit**: Good architecture reference for the caching pattern (how to avoid re-fetching already-seen items across cron runs). **Unmaintained** — don't depend on it directly, but the cache.json-in-branch pattern is worth stealing.

---

### `gautamkrishnar/blog-post-workflow` ⭐ ~4k
**URL**: https://github.com/gautamkrishnar/blog-post-workflow  
**Pattern**: Cron → fetch RSS → update README.md → commit

The most-used RSS-to-git action on GitHub Marketplace. Designed for profile READMEs but the pattern is identical to what you need.

**Fit**: Too narrow (README-focused), but widely battle-tested. Shows the `contents: write` permission pattern and `workflow_dispatch` alongside `schedule`.

---

## 2. RSSHub Deep Dive

**URL**: https://github.com/DIYgod/RSSHub  
**Stars**: ~44,000  
**Tech**: TypeScript (92%), Node.js, Koa  
**Last push**: April 2026 (very active)

### Can it be used as a library?

**Yes, experimentally.** The docs explicitly list npm package usage:

```js
import * as RSSHub from 'rsshub';

await RSSHub.init({
  CACHE_TYPE: null,  // disable Redis requirement
});

const result = await RSSHub.request('/github/trending/daily/javascript');
```

Install: `npm install rsshub`

**Caveats**:
- Marked "experimental" in docs
- The full package is enormous (5,000+ routes, all bundled)
- Custom routes **cannot** be mounted dynamically — they require rebuilding the route index. From [Issue #20769](https://github.com/DIYgod/RSSHub/issues/20769): *"The route loader only scans the internal routes directory... simply mounting files is not enough for them to be recognized at runtime"*
- Adding custom routes requires forking, adding to `lib/routes/`, and rebuilding

### Route System Architecture

Routes live in `lib/routes/<namespace>/` with three files:
- `router.ts` — registers the route path
- `maintainer.ts` — maintainer metadata  
- `radar.ts` — browser extension URL matching rules

Each route exports a `Route` object:

```typescript
export const route: Route = {
  path: '/trending/:lang?/:since?/:spoken_lang?',
  handler: async (ctx) => {
    // fetch, parse, return items
    return {
      title: 'GitHub Trending',
      link: 'https://github.com/trending',
      item: items,  // array of { title, link, description, pubDate }
    };
  },
};
```

RSSHub's middleware (`template.tsx`) then renders this to RSS 2.0, Atom, JSON Feed, or RSS3 based on the `?format=` parameter.

### Output Formats

Append `?format=rss`, `?format=atom`, `?format=json`, or `?format=rss3` to any route. Default is RSS 2.0. JSON Feed output is directly consumable without XML parsing.

### Assessment for Your Use Case

RSSHub as a **service** (self-hosted Docker) is excellent for generating feeds from sites that don't have them. As a **library** embedded in your GitHub Actions workflow, it's impractical — the package is massive, requires Redis for caching, and custom routes need a rebuild. 

**Better approach**: Run RSSHub as a sidecar service (Docker) or use the public instance `https://rsshub.app/` for standard routes, and fetch its JSON output in your Actions workflow.

---

## 3. RSS Archival Projects

### ArchiveBox ⭐ 27,200
**URL**: https://github.com/ArchiveBox/ArchiveBox  
**Tech**: Python, Django  
**Last wiki update**: March 2026

Full web archiving with built-in RSS scheduled import:

```bash
archivebox schedule --every=day --depth=1 'https://example.com/feed.xml'
archivebox schedule --every='0 */6 * * *' 'https://example.com/feed.xml'
```

Saves HTML, PDF, PNG, WARC, git clone (for code repos), readability article text, and more per URL. The new orchestrator (v0.9+) stores schedules in the database — no separate cron container needed.

**Fit**: Overkill for your use case if you just want article metadata/content in Markdown. ArchiveBox stores everything in a proprietary folder structure, not git-native Markdown. **Not a good fit for Graphify's git-native approach.** However, it's the gold standard if you need full-fidelity web archival (screenshots, WARC, etc.) alongside your knowledge graph.

---

### `pedramamini/RSSidian` 
**URL**: https://github.com/pedramamini/RSSidian  
**Tech**: Python, SQLite, Annoy vector index  
**Latest release**: Feb 2026

RSS → Obsidian Markdown pipeline with AI summarization, quality scoring (S/A/B/C/D tiers), and MCP service API. Stores article metadata in SQLite, generates Markdown notes.

**Fit**: The quality-scoring pattern (filter low-value content before processing) is directly applicable to your pipeline. The MCP service API is interesting for Graphify integration. **Not GitHub Actions native** — runs as a local/server process.

---

## 4. Git-Based Knowledge Management

### `sou350121/Pulsar` ⭐ 4 (new, Feb 2026)
**URL**: https://github.com/sou350121/Pulsar  
**Tech**: Python 3.9+, Node.js 22+, Moltbot (cron)

**This is the closest existing analog to what you're building.** Architecture:

```
RSS feeds → Rating engine (⚡/🔧/📖/❌) → LLM reasoning → Markdown → GitHub Contents API push
```

Key design decisions directly relevant to RssWiki:
- **All outputs pushed via GitHub Contents API** (`scripts/gh-contents-upload.py`) — handles create/update, auto-resolves SHA
- **Structured Markdown → git** as the knowledge store (full-text grep via `git log -S`)
- **Watchdog self-healing**: 15 health checks, 7 auto-recovery paths, DAG-ordered recovery
- **Deduplication**: state tracked in `memory/` JSON files
- **Cron via Moltbot** (not GitHub Actions — runs on a VPS)

**Fit**: Excellent reference implementation. The `gh-contents-upload.py` script pattern (push Markdown to a separate knowledge repo via Contents API) is exactly what you'd want for triggering Graphify. The watchdog pattern is worth studying for your pipeline reliability.

**Limitation**: Uses Moltbot for scheduling (not GitHub Actions), requires a persistent server. You'd adapt the pipeline scripts to run inside GitHub Actions instead.

---

### `ESJavadex/knowledge-forge` (April 2026)
**URL**: https://github.com/ESJavadex/knowledge-forge  
**Tech**: Node.js, Express, marked, gray-matter

LLM-driven wiki builder: drop Markdown sources in `raw/`, get an interlinked wiki out. Uses git as the storage backend with full history. Concept implementation, not production-ready.

**Fit**: Conceptually similar to Graphify. Shows the `raw/ → wiki/` pipeline pattern with git as the VCS backbone.

---

### `minhhungit/github-action-rss-crawler` 
**URL**: https://github.com/minhhungit/github-action-rss-crawler  
**Tech**: C# (.NET Core), LiteDB, GitHub Actions  
**Schedule**: Every 4 hours

Complete end-to-end example of the exact pattern you need:

```yaml
on:
  schedule:
    - cron: '0 */4 * * *'
  workflow_dispatch:

jobs:
  update-readme-with-blog:
    runs-on: windows-2019
    steps:
      - uses: actions/checkout@main
      - run: dotnet run  # fetches RSS, updates LiteDB, generates index.html
      - run: git config --local user.email "bot@example.com"
      - run: git config --local user.name "Bot"
      - run: git add .
      - run: git commit -m "Add changes"
      - run: git push
```

**Fit**: Direct reference for the cron → fetch → commit → push loop. Uses LiteDB (embedded) as state store committed to the repo — a simpler alternative to JSON state files.

---

## 5. Cron-Based Content Pipeline Patterns

### The Canonical Pattern (synthesized from all sources above)

```yaml
name: RSS Fetch Pipeline

on:
  schedule:
    - cron: '0 */6 * * *'   # every 6 hours
  workflow_dispatch:          # always add for manual testing

permissions:
  contents: write             # required for git push

jobs:
  fetch-and-commit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Fetch RSS feeds
        run: |
          # your fetch script here
          node scripts/fetch-rss.js

      - name: Commit results
        id: commit
        uses: stefanzweifel/git-auto-commit-action@v7
        with:
          commit_message: 'chore: update RSS feed data [skip ci]'
          file_pattern: 'data/**/*.json'

      - name: Trigger downstream (Graphify)
        if: steps.commit.outputs.changes_detected == 'true'
        uses: peter-evans/repository-dispatch@v3
        with:
          token: ${{ secrets.PAT }}
          repository: your-org/graphify-repo
          event-type: rss-updated
          client-payload: '{"sha": "${{ github.sha }}"}'
```

Key patterns from the research:
1. **`[skip ci]` in commit message** — prevents infinite loop when the commit triggers another workflow run
2. **`changes_detected` output** — only trigger downstream if something actually changed
3. **`workflow_dispatch` alongside `schedule`** — essential for testing without waiting for cron
4. **`contents: write` permission** — required for the commit-back pattern
5. **State file in repo** — commit a `last_fetched.json` or similar to track what's been processed; avoids re-processing on every
```

**Tool: background_output**

**Input:**
```json
{
  "task_id": "bg_7057fef4"
}
```

**Output:**
```
# Task Status

| Field | Value |
|-------|-------|
| Task ID | `bg_7057fef4` |
| Description | RSS聚合+知识管理开源项目 |
| Agent | librarian |
| Status | **error** |
| Duration | 3m 6s |
| Session ID | `ses_24fc12d56ffesPVEA2whNqyDGM` |
| Last tool | websearch_web_search_exa |


> **Failed**: The task encountered an error. Check the last message for details.
## Original Prompt

```
CONTEXT: I'm researching open-source projects for building a personal RSS feed aggregator + LLM-powered knowledge base system. The user wants to: 1) Subscribe to RSS feeds (tech blogs, papers), 2) Auto-fetch and filter/classify articles by topic, 3) Store original articles, 4) Build a knowledge graph with LLM processing, 5) Generate visual structure graphs and wiki-style pages.

GOAL: Find the best existing open-source projects that solve parts of this problem, so we can compose them instead of ...
```
```

**Tool: background_output**

**Input:**
```json
{
  "task_id": "bg_2814c26e"
}
```

**Output:**
```
# Task Status

| Field | Value |
|-------|-------|
| Task ID | `bg_2814c26e` |
| Description | RSS全文提取和内容处理工具链 |
| Agent | librarian |
| Status | **error** |
| Duration | 4m 8s |
| Session ID | `ses_24fc1058dffegLYPTvlAr5zmRL` |
| Last tool | websearch_web_search_exa |


> **Failed**: The task encountered an error. Check the last message for details.
## Original Prompt

```
CONTEXT: I'm building an RSS feed aggregator that needs to fetch full article content from RSS feeds (which often only provide summaries), convert them to clean markdown, and store them for further LLM processing.

GOAL: Find the best open-source tools and libraries for the RSS content pipeline: feed parsing → full article extraction → markdown conversion → storage.

REQUEST: Research these specific areas:

1. **RSS/Atom feed parsers** - Compare feedparser, atoma, reader (Python RSS reader), and...
```
```

**Tool: task**

**Input:**
```json
{
  "description": "RSS聚合+知识管理开源项目",
  "load_skills": [],
  "prompt": "CONTEXT: I'm researching open-source projects for building a personal RSS feed aggregator + LLM-powered knowledge base system. The user wants to: 1) Subscribe to RSS feeds (tech blogs, papers), 2) Auto-fetch and filter/classify articles by topic, 3) Store original articles, 4) Build a knowledge graph with LLM processing, 5) Generate visual structure graphs and wiki-style pages.\n\nGOAL: Find the best existing open-source projects that solve parts of this problem, so we can compose them instead of building from scratch.\n\nREQUEST: Search for and analyze these categories of projects:\n\n1. **Self-hosted RSS readers/aggregators** - projects like Miniflux, FreshRSS, Tiny Tiny RSS, etc. Focus on:\n   - Which ones have good APIs for programmatic access?\n   - Which support filtering/classification features?\n   - Which are most actively maintained?\n   - Which are lightweight enough for personal use?\n\n2. **RSS + AI/LLM integration projects** - any project that combines RSS feeds with LLM processing (summarization, classification, knowledge extraction). Search GitHub for repos combining RSS with AI/LLM.\n\n3. **Personal knowledge management with LLM** - projects that use LLMs to build personal knowledge bases from collected content (not just note-taking apps, but ones that auto-process and structure knowledge).\n\nFor each project found, report: name, GitHub URL, stars, last update, tech stack, key features, and how it could fit into our architecture. Prioritize projects with 100+ stars and recent activity (2024-2025).",
  "run_in_background": true,
  "subagent_type": "librarian"
}
```

**Output:**
```
Background task launched.

Background Task ID: bg_53d44ed8
Description: RSS聚合+知识管理开源项目
Agent: librarian
Status: pending

System notifies on completion. Use `background_output` with task_id="bg_53d44ed8" to check.

Do NOT call background_output now. Wait for <system-reminder> notification first.

<task_metadata>
session_id: ses_24fbb2d9affeLU77sY845c6OtM
task_id: bg_53d44ed8
background_task_id: bg_53d44ed8
</task_metadata>

to continue: task(session_id="ses_24fbb2d9affeLU77sY845c6OtM", load_skills=[], run_in_background=false, prompt="...")
```

**Tool: task**

**Input:**
```json
{
  "load_skills": [],
  "prompt": "CONTEXT: I'm building an RSS feed aggregator that needs to fetch full article content from RSS feeds (which often only provide summaries), convert them to clean markdown, and store them for further LLM processing.\n\nGOAL: Find the best open-source tools and libraries for the RSS content pipeline: feed parsing → full article extraction → markdown conversion → storage.\n\nREQUEST: Research these specific areas:\n\n1. **RSS/Atom feed parsers** - Compare feedparser, atoma, reader (Python RSS reader), and any other modern alternatives. Which handles edge cases best? Which is most maintained?\n\n2. **Full article extraction / web scraping** - Compare trafilatura, newspaper3k/newspaper4k, readability-lxml, mozilla/readability, and similar tools. Focus on:\n   - Accuracy of content extraction (removing ads, nav, etc.)\n   - Markdown output quality\n   - Handling of tech blog formats\n   - Active maintenance status\n\n3. **RSS-to-markdown pipelines** - Any existing project that already does RSS → clean markdown conversion as a pipeline.\n\n4. **Content deduplication** - Tools or approaches for detecting duplicate/near-duplicate articles across RSS feeds.\n\n5. **Article metadata extraction** - Tools for extracting author, date, tags, categories from articles.\n\nFor each tool, report: name, GitHub URL/PyPI, stars, maintenance status, and a concrete assessment of whether we should use it.",
  "run_in_background": true,
  "subagent_type": "librarian",
  "description": "RSS全文提取和内容处理工具链"
}
```

**Output:**
```
Background task launched.

Background Task ID: bg_2a25e0e9
Description: RSS全文提取和内容处理工具链
Agent: librarian
Status: pending

System notifies on completion. Use `background_output` with task_id="bg_2a25e0e9" to check.

Do NOT call background_output now. Wait for <system-reminder> notification first.

<task_metadata>
session_id: ses_24fbb2d83ffe0Qbtz4oNVmf1Fm
task_id: bg_2a25e0e9
background_task_id: bg_2a25e0e9
</task_metadata>

to continue: task(session_id="ses_24fbb2d83ffe0Qbtz4oNVmf1Fm", load_skills=[], run_in_background=false, prompt="...")
```

---

## Assistant (​Sisyphus - Ultraworker · opus 4.6 · 21.8s)

<thinking>
I got the GitHub Actions research results. Two tasks failed before and have been retried. Let me also check if bg_82a676f9 (知识图谱可视化) has completed.

Let me wait for the remaining tasks to complete before producing the full report. I have:
- ✅ bg_29287ba8: GitHub Actions自动化RSS工作流 - COMPLETED and collected
- ❌ bg_7057fef4: RSS聚合+知识管理开源项目 - FAILED, retried as bg_53d44ed8
- ❌ bg_2814c26e: RSS全文提取和内容处理工具链 - FAILED, retried as bg_2a25e0e9
- ⏳ bg_82a676f9: 知识图谱可视化和LLM知识库方案 - still in progress

I should wait for the remaining tasks to complete. Let me end my response and wait for notifications.
</thinking>

已收到 GitHub Actions 工作流的调研结果。两个失败的任务已重试，还有知识图谱可视化的任务也在进行中。等全部完成后整合报告。

---

## User

<system-reminder>
[BACKGROUND TASK COMPLETED]
**ID:** `bg_53d44ed8`
**Description:** RSS聚合+知识管理开源项目
**Duration:** 2m 50s

**2 tasks still in progress.** You WILL be notified when ALL complete.
Do NOT poll - continue productive work.

Use `background_output(task_id="bg_53d44ed8")` to retrieve this result when ready.
</system-reminder>
<!-- OMO_INTERNAL_INITIATOR -->

---

## User

<system-reminder>
[BACKGROUND TASK COMPLETED]
**ID:** `bg_2a25e0e9`
**Description:** RSS全文提取和内容处理工具链
**Duration:** 3m 5s

**1 task still in progress.** You WILL be notified when ALL complete.
Do NOT poll - continue productive work.

Use `background_output(task_id="bg_2a25e0e9")` to retrieve this result when ready.
</system-reminder>
<!-- OMO_INTERNAL_INITIATOR -->

---

## User

好了吗

---

## Assistant (​Sisyphus - Ultraworker · opus 4.6 · 21.8s)



<thinking>
The user is asking if the research is done. Let me collect the completed results. I have:
- ✅ bg_29287ba8: GitHub Actions - already collected
- ✅ bg_53d44ed8: RSS聚合+知识管理 - just completed
- ✅ bg_2a25e0e9: RSS全文提取工具链 - just completed
- ⏳ bg_82a676f9: 知识图谱可视化 - still in progress

Let me collect the two new results. The last one (知识图谱可视化) is still running but I have enough from the other three to start synthesizing. Let me collect what's ready.
</thinking>

还有一个知识图谱可视化的任务在跑，先收已完成的三个。

**Tool: background_output**

**Input:**
```json
{
  "task_id": "bg_53d44ed8"
}
```

**Output:**
```
Task Result

Task ID: bg_53d44ed8
Description: RSS聚合+知识管理开源项目
Duration: 2m 50s
Session ID: ses_24fbb2d9affeLU77sY845c6OtM

---

I'll research these three categories in parallel, searching for the best open-source projects across RSS aggregators, RSS+AI integrations, and LLM-powered knowledge bases.

Good data on categories 1 and 2. Let me now get GitHub stats for the key projects and search for knowledge base tools.

No `gh` CLI available. Let me fetch GitHub API directly and search for more projects.

The knowledge graph search returned weak results. Let me search for the major established projects in this space.

I now have comprehensive data. Let me compile the full analysis.

---

# Open-Source Projects for RSS + LLM Knowledge Base System

All data verified as of **April 21, 2026**.

---

## Category 1: Self-Hosted RSS Readers/Aggregators

### 🥇 Miniflux
| Field | Value |
|---|---|
| **GitHub** | [miniflux/v2](https://github.com/miniflux/v2) |
| **Stars** | ⭐ 9,101 |
| **Last Push** | April 20, 2026 (actively maintained) |
| **Tech Stack** | Go, PostgreSQL |
| **License** | Apache 2.0 |

**Key features for your use case:**
- **Full REST API** — the best API story of any self-hosted RSS reader. Full CRUD for feeds, categories, entries, users. Well-documented with client libraries in Go and Python.
- **Webhooks** — real-time push notifications when new articles arrive. This is the critical integration point for your LLM pipeline.
- **25+ integrations** — Notion, Telegram, Slack, Wallabag, Readwise, etc.
- **Built-in content scraper** — fetches full article text via Readability parser (not just feed summaries).
- **Fever + Google Reader API** — compatible with all mobile RSS apps.
- Single Go binary, ~30MB Docker image, ~50MB RAM idle.

**Architecture fit:** **Best choice as the RSS backbone.** Use Miniflux's REST API to poll new entries, and its webhook support to trigger your LLM processing pipeline in real-time. The Python client library makes integration trivial.

---

### 🥈 FreshRSS
| Field | Value |
|---|---|
| **GitHub** | [FreshRSS/FreshRSS](https://github.com/FreshRSS/FreshRSS) |
| **Stars** | ⭐ 14,824 |
| **Last Push** | April 20, 2026 (very active) |
| **Tech Stack** | PHP, MySQL/PostgreSQL/SQLite |
| **License** | AGPL-3.0 |

**Key features for your use case:**
- **Extension system** — can add custom processing logic directly in PHP.
- **Google Reader API + Fever API** — broad mobile app compatibility.
- **XPath-based content scraping** — more configurable than Miniflux's scraper.
- **WebSub support** — real-time feed updates without polling.
- Handles 1M+ articles, 50k+ feeds.

**Architecture fit:** Better if you want to extend the reader itself with custom PHP logic. The API is Google Reader-compatible (not a native REST API), which is slightly less ergonomic for programmatic access than Miniflux. Choose this if you need the extension ecosystem or SQLite (no PostgreSQL dependency).

---

### Bonus: RSSHub
| Field | Value |
|---|---|
| **GitHub** | [DIYgod/RSSHub](https://github.com/DIYgod/RSSHub) |
| **Stars** | ⭐ 43,564 |
| **Last Push** | April 21, 2026 (extremely active) |
| **Tech Stack** | TypeScript/Node.js |
| **License** | AGPL-3.0 |

**Not a reader** — it's an RSS feed *generator*. Converts 1,000+ websites that don't have RSS (Twitter/X, GitHub trending, Hacker News, arXiv, etc.) into RSS feeds. **Essential companion** to Miniflux/FreshRSS for subscribing to sources that don't natively publish RSS.

---

## Category 2: RSS + AI/LLM Integration Projects

### 🥇 miniflux-ai
| Field | Value |
|---|---|
| **GitHub** | [Qetesh/miniflux-ai](https://github.com/Qetesh/miniflux-ai) |
| **Stars** | ⭐ 231 |
| **Last Push** | March 27, 2026 |
| **Tech Stack** | Python |
| **License** | None specified |

**What it does:** Integrates directly with Miniflux via API or webhook. Sends article content to LLMs (Ollama, OpenAI, Gemini, LLaMA) to generate summaries, translations, and "AI morning/evening news" digests. Writes results back into Miniflux entries.

**Architecture fit:** **Drop-in sidecar for Miniflux.** If you pick Miniflux as your reader, this is the fastest path to LLM-enriched articles. Supports multithreading, configurable LLM endpoints. The code is simple enough to fork and extend with classification/tagging logic.

---

### 🥈 RSSbrew
| Field | Value |
|---|---|
| **GitHub** | [yinan-c/RSSbrew](https://github.com/yinan-c/RSSbrew) |
| **Stars** | ⭐ 284 |
| **Last Push** | September 12, 2025 |
| **Tech Stack** | Python |
| **License** | AGPL-3.0 |

**What it does:** Self-hosted RSS middleware layer. Aggregates multiple feeds, applies custom filters (keyword, regex, LLM-based), generates AI summaries (any OpenAI-compatible model), and produces daily/weekly digest feeds. Outputs processed content as new RSS feeds.

**Architecture fit:** Sits between your feed sources and your knowledge base. The "filter → summarize → re-publish as RSS" pipeline is exactly what you need for topic classification before storage. Slightly less active than miniflux-ai (last push Sep 2025).

---

### 🥉 UglyFeed
| Field | Value |
|---|---|
| **GitHub** | [fabriziosalmi/UglyFeed](https://github.com/fabriziosalmi/UglyFeed) |
| **Stars** | ⭐ 305 |
| **Last Push** | March 18, 2026 |
| **Tech Stack** | Python |
| **License** | AGPL-3.0 |

**What it does:** Retrieves RSS feeds, clusters articles by similarity, rewrites/summarizes them using LLMs (OpenAI, Ollama), evaluates content quality, and serves the result as new RSS feeds. Supports translation.

**Architecture fit:** Useful for the "aggregate by topic similarity" step. The clustering-before-LLM approach reduces API costs. More of a research/experimentation tool than production-grade.

---

### Notable: MorningDeck
| Field | Value |
|---|---|
| **GitHub** | [eschnou/morningdeck](https://github.com/eschnou/morningdeck) |
| **Stars** | ~50 (new, Jan 2026) |
| **Last Push** | March 24, 2026 |
| **Tech Stack** | Java/Spring Boot |
| **License** | Open source |

**What it does:** Full AI news intelligence platform — aggregates RSS + newsletters + Reddit + web scraping, scores content by relevance to your defined interests using LLM, delivers daily briefings. Self-hostable, any OpenAI-compatible LLM.

**Architecture fit:** The closest existing project to your full vision (minus the knowledge graph). Too new/low-stars to rely on, but worth watching as a reference implementation.

---

## Category 3: Personal Knowledge Management with LLM

### 🥇 Khoj
| Field | Value |
|---|---|
| **GitHub** | [khoj-ai/khoj](https://github.com/khoj-ai/khoj) |
| **Stars** | ⭐ 34,180 |
| **Last Push** | March 26, 2026 |
| **Tech Stack** | Python (Django), TypeScript |
| **License** | AGPL-3.0 |

**What it does:** Self-hostable AI "second brain." Ingests documents (Markdown, PDF, Org-mode, web pages), builds a semantic search index, and lets you chat with your knowledge base. Supports autonomous agents, scheduled automations, deep research mode. Works with any local or cloud LLM.

**Architecture fit:** **Best candidate for the knowledge base layer.** Khoj has a REST API for ingesting content programmatically — you can pipe processed articles from your RSS pipeline directly into it. It handles semantic search and Q&A over your stored articles. Does **not** natively build a visual knowledge graph, but handles the storage + retrieval + chat interface.

---

### 🥈 Microsoft GraphRAG
| Field | Value |
|---|---|
| **GitHub** | [microsoft/graphrag](https://github.com/microsoft/graphrag) |
| **Stars** | ⭐ 32,393 |
| **Last Push** | April 13, 2026 |
| **Tech Stack** | Python |
| **License** | MIT |

**What it does:** Modular graph-based RAG system. Extracts entities and relationships from text using LLMs, builds a knowledge graph, and uses graph traversal for retrieval (much better than naive vector search for "what connects X to Y" queries). Produces community summaries and visual graph outputs.

**Architecture fit:** **Best candidate for the knowledge graph layer.** Feed your stored articles into GraphRAG's indexing pipeline → it extracts entities/relationships → builds a queryable graph. The graph visualization output directly addresses your "visual structure graphs" requirement. Heavyweight (designed for large corpora), but MIT licensed and actively maintained.

---

### 🥉 PrivateGPT
| Field | Value |
|---|---|
| **GitHub** | [zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt) |
| **Stars** | ⭐ 57,192 |
| **Last Push** | February 26, 2026 |
| **Tech Stack** | Python |
| **License** | Apache 2.0 |

**What it does:** 100% local document Q&A. Ingests documents, builds vector embeddings, answers questions privately. REST API for programmatic ingestion and querying.

**Architecture fit:** Simpler than Khoj/GraphRAG — pure RAG without graph structure. Good if you want a lightweight "chat with your articles" layer without the complexity of knowledge graph construction. Note: development pace has slowed compared to Khoj.

---

### R2R (Reason to Retrieve)
| Field | Value |
|---|---|
| **GitHub** | [SciPhi-AI/R2R](https://github.com/SciPhi-AI/R2R) |
| **Stars** | ⭐ 7,769 |
| **Last Push** | November 7, 2025 |
| **Tech Stack** | Python |
| **License** | MIT |

**What it does:** Production-ready RAG system with REST API. Handles document ingestion, chunking, embedding, hybrid search (vector + keyword), and agentic retrieval. Has built-in knowledge graph support via GraphRAG integration.

**Architecture fit:** More production-oriented than PrivateGPT. The REST API makes it easy to integrate as a microservice. Development has slowed (last push Nov 2025).

---

## Recommended Architecture

```
┌─────────────────────────────────────────────────────────┐
│  FEED SOURCES                                           │
│  RSSHub (43.5k★) ──► generates RSS for non-RSS sites   │
└────────────────────────┬────────────────────────────────┘
                         │ RSS feeds
                         ▼
┌─────────────────────────────────────────────────────────┐
│  RSS AGGREGATOR                                         │
│  Miniflux (9.1k★) ──► stores articles, REST API,       │
│                        webhooks on new entries          │
└────────────────────────┬────────────────────────────────┘
                         │ webhook / API poll
                         ▼
┌─────────────────────────────────────────────────────────┐
│  LLM PROCESSING LAYER  (build thin, reuse components)  │
│  miniflux-ai (231★) ──► fork/extend for:               │
│    • topic classification                               │
│    • entity extraction                                  │
│    • summarization                                      │
│    • tagging                                            │
└──────────┬──────────────────────────┬───────────────────┘
           │ structured articles       │ raw text
           ▼                          ▼
┌──────────────────┐    ┌─────────────────────────────────┐
│  ARTICLE STORE   │    │  KNOWLEDGE GRAPH                │
│  Khoj (34.2k★)  │    │  GraphRAG (32.4k★)              │
│  • semantic Q&A  │    │  • entity/relation extraction   │
│  • chat UI       │    │  • graph visualization          │
│  • REST ingest   │    │  • community summaries          │
└──────────────────┘    └─────────────────────────────────┘
```

**What you'd build yourself:** The glue between Miniflux webhooks → LLM processing → Khoj ingest + GraphRAG indexing. This is a thin Python service (~200-400 lines), not a full system.

**What you don't build:** Feed fetching, article storage, semantic search, graph extraction, visualization — all covered by existing projects.
```

**Tool: background_output**

**Input:**
```json
{
  "task_id": "bg_2a25e0e9"
}
```

**Output:**
```
Task Result

Task ID: bg_2a25e0e9
Description: RSS全文提取和内容处理工具链
Duration: 3m 5s
Session ID: ses_24fbb2d83ffe0Qbtz4oNVmf1Fm

---

I'll research all five areas in parallel to give you a comprehensive comparison.

Now let me get more specific data on deduplication tools and the `lemon24/reader` library, plus check trafilatura's markdown output and maintenance status:

Now I have all the data needed. Here's the comprehensive assessment:

---

# RSS Content Pipeline: Tool Assessment (April 2026)

---

## 1. RSS/Atom Feed Parsers

### Comparison Table

| Library | Stars | Last Push | Verdict |
|---|---|---|---|
| **feedparser** | 2,357 | Apr 2026 | ✅ Use — battle-tested, most edge cases covered |
| **fastfeedparser** | 155 | Apr 2026 | ✅ Use if throughput matters |
| **atoma** | 118 | Oct 2022 | ❌ Skip — abandoned |
| **lemon24/reader** | 533 | Apr 2026 | ⚠️ Use only if you want full reader infra |

---

### [feedparser](https://github.com/kurtmckee/feedparser) — ⭐ 2,357 | PyPI: `feedparser`
**Maintenance**: Active (pushed Apr 14, 2026, v6.0.11)

The de-facto standard. Handles RSS 0.9x/1.0/2.0, Atom 0.3/1.0, RDF, JSON Feed. Key strengths:
- **Bozo detection**: gracefully parses malformed feeds (critical for real-world RSS)
- Relative link resolution, character encoding detection, namespace handling, date normalization
- Sanitizes HTML content (XSS protection)
- 107 open issues but actively triaged

**Weakness**: Slow (~62ms/feed), high memory. The `lemon24/reader` maintainer benchmarked it at 9s for 157 feeds vs atoma's 1.5s.

**Use it for**: Any production RSS pipeline. Its malformed-feed handling alone justifies it.

```python
import feedparser
feed = feedparser.parse("https://example.com/feed.xml")
for entry in feed.entries:
    print(entry.title, entry.link, entry.published)
```

---

### [fastfeedparser](https://github.com/kagisearch/fastfeedparser) — ⭐ 155 | PyPI: `fastfeedparser`
**Maintenance**: Very active (v0.6.0, Apr 6, 2026 — multiple releases per month)

Built by Kagi Search. **27x faster than feedparser** (0.46s vs 12.31s for 6,600 entries). Uses lxml under the hood. API is intentionally feedparser-compatible.

**Weakness**: Newer, less battle-tested on malformed feeds. In one benchmark it parsed 35 entries from a feed where feedparser got 0 — but that could go either way depending on the feed.

**Use it for**: High-volume pipelines (100s of feeds/minute). For an LLM aggregator processing many feeds, this is worth the tradeoff.

---

### [atoma](https://github.com/NicolasLM/atoma) — ⭐ 118 | PyPI: `atoma`
**Maintenance**: ❌ Dead. Last release v0.0.17 in July 2019, last push Oct 2022.

Supports RSS 2.0, Atom 1.0, JSON Feed, OPML. Typed Python objects (not dict-like). Faster and lower memory than feedparser. But: doesn't handle malformed feeds, no relative link resolution, no sanitization.

**Skip it.** The `lemon24/reader` maintainer evaluated it and decided against adopting it precisely because of the malformed feed handling gap.

---

### [lemon24/reader](https://github.com/lemon24/reader) — ⭐ 533 | PyPI: `reader`
**Maintenance**: Active (pushed Apr 20, 2026)

This is a **full feed reader library**, not just a parser. It manages feed storage (SQLite), update scheduling, entry filtering, search, and plugins. Uses its own internal parser (not feedparser).

**Use it for**: If you want a complete feed management layer with persistence built in. Overkill if you just need parsing.

---

**Recommendation**: Use **feedparser** as your primary parser. If you're processing >50 feeds/minute, swap to **fastfeedparser** (its API is compatible).

---

## 2. Full Article Extraction

### Benchmark Results (ScrapingHub article-extraction-benchmark, latest run)

| Tool | F1 Score | Precision | Recall | Speed |
|---|---|---|---|---|
| **trafilatura 2.0** | **0.958** | 0.938 | 0.978 | ~94ms/page |
| **go-trafilatura** | 0.957 | 0.940 | 0.974 | — |
| **newspaper4k** | 0.949 | 0.964 | 0.934 | — |
| **news_please** | 0.948 | 0.964 | 0.933 | — |
| **readability-lxml** | 0.922 | 0.913 | 0.931 | — |
| newspaper3k (dead) | 0.912 | — | — | — |

Source: [scrapinghub/article-extraction-benchmark](https://github.com/scrapinghub/article-extraction-benchmark)

A separate 2026 benchmark ([WCXB, 2,008 pages across 7 page types](https://murroughfoley.com/web-content-extraction-benchmark/)) shows trafilatura at F1=0.791 overall but 0.926 on articles specifically — and reveals that **all tools degrade significantly on non-article pages** (forums, product pages, etc.). For tech blogs (articles), the differences are small.

---

### [trafilatura](https://github.com/adbar/trafilatura) — ⭐ 5,756 | PyPI: `trafilatura`
**Maintenance**: Active (last push Sep 2025, actively starred/watched)

The clear winner for your use case. Key facts:
- **Native markdown output** (`output_format="markdown"`) — this is unique among the top tools
- Built-in deduplication via `trafilatura.deduplication.Simhash`
- Extracts metadata: title, author, date, tags, language, source URL
- Falls back to readability-lxml internally when its own heuristic fails
- Explicitly tagged `llm`, `rag`, `rss-feed` on GitHub — designed for this exact pipeline
- Apache 2.0 license

```python
from trafilatura import fetch_url, extract

html = fetch_url("https://example.com/article")
result = extract(html, output_format="markdown", with_metadata=True)
# Returns markdown string

# Or get structured data:
from trafilatura.core import bare_extraction
doc = bare_extraction(html, with_metadata=True)
print(doc.title, doc.author, doc.date, doc.text)
```

**Weakness**: 109 open issues. Doesn't handle JS-rendered pages (needs Playwright/Selenium for SPAs).

---

### [newspaper4k](https://github.com/AndyTheFactory/newspaper4k) — ⭐ 1,087 | PyPI: `newspaper4k`
**Maintenance**: Active (pushed Apr 11, 2026)

The maintained fork of the abandoned newspaper3k (15k stars but dead). F1=0.949, **highest precision** (0.964) of any open-source tool — it's conservative, rarely includes boilerplate. Extracts authors, dates, keywords, summary, top image.

**Weakness**: 155 open issues. No native markdown output (returns plain text). Slower than trafilatura. Requires NLTK data download.

```python
import newspaper
article = newspaper.Article("https://example.com/article")
article.download()
article.parse()
print(article.authors, article.publish_date, article.text)
```

**Use it for**: When you need high-precision extraction and don't mind converting text→markdown yourself.

---

### [readability-lxml](https://github.com/buriy/python-readability) — ⭐ 2,895 | PyPI: `readability-lxml`
**Maintenance**: Slow but alive (pushed Jan 2026)

Python port of Mozilla's Readability algorithm. F1=0.922. Returns cleaned HTML, not text/markdown — you need `html2text` or `markdownify` on top. Used internally by trafilatura as a fallback.

**Use it for**: When you need the cleaned HTML (e.g., to preserve structure for further processing). Don't use it as your primary extractor — trafilatura is strictly better.

---

### Mozilla Readability.js
The JS original. F1=0.947 in benchmarks. Only relevant if you're running a Node.js pipeline or using it via Playwright. For Python, use trafilatura instead.

---

**Recommendation**: **trafilatura** is the right choice. It has the best F1, native markdown output, built-in metadata extraction, and is explicitly designed for LLM/RAG pipelines. Use newspaper4k as a fallback for sites where trafilatura underperforms.

---

## 3. RSS-to-Markdown Pipelines

No mature, production-ready Python library exists that does the full pipeline (RSS fetch → full article → clean markdown). What exists:

| Project | Stars | Status | What it does |
|---|---|---|---|
| [keiranlovett/rss-feed-to-markdown](https://github.com/keiranlovett/rss-feed-to-markdown) | ~50 | Active (v1.2.0, Nov 2024) | GitHub Action: RSS entries → markdown files (feed summary only, not full article) |
| [whatrocks/rss2markdown](https://github.com/whatrocks/rss2markdown) | 1 | Dead (2022) | Toy project |
| [shouya/rss-funnel](https://github.com/shouya/rss-funnel) | 150 | Active (Feb 2026) | Rust: RSS pipeline with full-text fetch, JS transforms — not Python |

**The gap is real**: no Python library does RSS → full article → markdown as a first-class pipeline. You'll need to compose:

```python
# The pipeline you'll build:
import feedparser
from trafilatura import fetch_url, extract

feed = feedparser.parse(feed_url)
for entry in feed.entries:
    html = fetch_url(entry.link)
    markdown = extract(html, output_format="markdown", with_metadata=True)
    # store markdown
```

This is ~10 lines and works well. The only missing piece is async/concurrent fetching — use `httpx` + `asyncio` or `trafilatura`'s built-in `utils.fetch_url` with a thread pool.

---

## 4. Content Deduplication

### Approaches

**Option A: URL-based deduplication** (trivial, do this first)
Store canonical URLs in a set/DB. Catches exact reposts. Trafilatura normalizes URLs via `trafilatura.utils.normalize_url`.

**Option B: Simhash (near-duplicate detection)**

| Library | Stars | Last Push | Notes |
|---|---|---|---|
| [1e0ng/simhash](https://github.com/1e0ng/simhash) | 1,036 | Mar 2022 | Pure Python, works, unmaintained |
| **trafilatura.deduplication** | (built-in) | Sep 2025 | Simhash built into trafilatura |

Trafilatura ships its own Simhash implementation:

```python
from trafilatura.deduplication import Simhash

seen_hashes = []
for article_text in articles:
    h = Simhash(article_text)
    # Compare hamming distance to seen hashes
    if not any(h.distance(seen) < 3 for seen in seen_hashes):
        seen_hashes.append(h)
        process(article_text)
```

**Option C: MinHash/LSH (large-scale)**

For 100k+ articles, use [datasketch](https://github.com/ekzhu/datasketch) (3.4k stars, active). MinHash + LSH gives O(1) approximate duplicate lookup:

```python
from datasketch import MinHash, MinHashLSH

lsh = MinHashLSH(threshold=0.8, num_perm=128)
m = MinHash(num_perm=128)
for word in article_text.split():
    m.update(word.encode('utf8'))
lsh.insert(article_id, m)
```

**Recommendation**: 
- Small scale (<10k articles): use trafilatura's built-in Simhash
- Large scale: use [datasketch](https://github.com/ekzhu/datasketch) MinHash+LSH
- Always do URL deduplication first (free, catches 80% of duplicates)

---

## 5. Article Metadata Extraction

### What trafilatura already gives you (free)

```python
from trafilatura.core import bare_extraction
doc = bare_extraction(html, with_metadata=True)
# doc.title, doc.author, doc.date, doc.tags, doc.language, 
# doc.source, doc.hostname, doc.description
```

This covers 80% of cases. For the remaining 20%, use structured metadata:

---

### [extruct](https://github.com/scrapinghub/extruct) — ⭐ 962 | PyPI: `extruct`
**Maintenance**: Active (pushed Apr 1, 2026, by Zyte/ScrapingHub)

Extracts **all embedded structured metadata** from HTML: JSON-LD, OpenGraph, Twitter Cards, Microdata, RDFa, Microformats. This is the gold standard for structured metadata.

```python
import extruct
import requests

r = requests.get(url)
data = extruct.extract(r.text, base_url=url, 
                       syntaxes=['json-ld', 'opengraph', 'microdata'])
# data['json-ld'] → Schema.org Article with author, datePublished, etc.
# data['opengraph'] → og:title, og:author, og:published_time
```

Tech blogs commonly use JSON-LD with `Article` schema — extruct will pull `author`, `datePublished`, `keywords`, `articleSection` directly.

---

### [htmldate](https://github.com/adbar/htmldate) — ⭐ 148 | PyPI: `htmldate`
**Maintenance**: Active (same author as trafilatura, pushed Nov 2025)

Specialized date extraction. More accurate than trafilatura's date extraction alone — tries meta tags, JSON-LD, URL patterns, and page content heuristics.

```python
from htmldate import find_date
date = find_date("https://example.com/article")  # returns "2026-03-15"
```

---

### [mediacloud/metadata-lib](https://github.com/mediacloud/metadata-lib) — ⭐ 17 | PyPI: `mediacloud-metadata`
**Maintenance**: Active (v1.4.1, Dec 2024)

Wraps trafilatura + htmldate + tldextract into a single `extract(url)` call. Returns title, date, language, domain, normalized URL. Good if you want a single-call API, but adds a dependency layer you don't control.

---

## Recommended Stack

```
RSS parsing:     feedparser (or fastfeedparser for high volume)
Full-text fetch: trafilatura.fetch_url (with httpx for async)
Extraction:      trafilatura (output_format="markdown", with_metadata=True)
Fallback:        newspaper4k (for sites trafilatura misses)
Structured meta: extruct (JSON-LD/OpenGraph for author/tags/date)
Date fallback:   htmldate (when trafilatura date is None)
Deduplication:   trafilatura.deduplication.Simhash (small) / datasketch (large)
Storage:         SQLite via lemon24/reader OR your own schema
```

The core pipeline is essentially **feedparser + trafilatura**. Everything else is optional enrichment. Trafilatura's explicit LLM/RAG focus, native markdown output, and built-in deduplication make it the obvious center of this stack.
```

---

## Assistant (​Sisyphus - Ultraworker · opus 4.6 · 65.7s)

<thinking>
I now have comprehensive results from 3 out of 4 tasks. The last one (bg_82a676f9: 知识图谱可视化和LLM知识库方案) is still running. Let me check if it's still pending or if I missed a notification. The system said "1 task still in progress" last time, and I haven't received a notification yet.

I have enough data to compile a comprehensive research report now. Let me synthesize all findings. I'll wait for the last task if it comes, but I can present what I have.

Actually, let me just compile the report now with what I have. The three completed tasks give me:

1. **GitHub Actions自动化RSS工作流** - Patterns for cron-based RSS fetching + git commit workflows
2. **RSS聚合+知识管理开源项目** - Miniflux, FreshRSS, RSSHub, miniflux-ai, RSSbrew, Khoj, GraphRAG, etc.
3. **RSS全文提取和内容处理工具链** - feedparser, trafilatura, newspaper4k, deduplication, metadata extraction

The missing one is about knowledge graph visualization and LLM knowledge base tools, but the RSS聚合 task already covered Khoj and GraphRAG, so there's significant overlap.

Let me synthesize this into a clear, actionable report for the user.
</thinking>

4 个调研中 3 个已完成，最后一个（知识图谱可视化）还在跑，但已有足够信息。让我先整合报告。

---

## 调研报告：RssWiki 可复用的开源组件

### 一、RSS 聚合层

| 项目 | ⭐ | 技术栈 | 推荐理由 | 适配度 |
|---|---|---|---|---|
| **[Miniflux](https://github.com/miniflux/v2)** | 9.1k | Go, PostgreSQL | 最佳 REST API、Webhook 推送、内置全文抓取、单 binary 部署 | ⭐⭐⭐⭐⭐ |
| [FreshRSS](https://github.com/FreshRSS/FreshRSS) | 14.8k | PHP | 扩展丰富、支持 SQLite，但 API 是 Google Reader 兼容而非原生 REST | ⭐⭐⭐ |
| **[RSSHub](https://github.com/DIYgod/RSSHub)** | 43.5k | TypeScript | 把没有 RSS 的网站变成 RSS（Twitter、ArXiv、HN 等），作为信源补充 | ⭐⭐⭐⭐⭐ |

**结论**：Miniflux 做 RSS 聚合 + RSSHub 补充非标准信源，是最佳组合。

---

### 二、RSS + LLM 处理层

| 项目 | ⭐ | 做什么 | 适配度 |
|---|---|---|---|
| **[miniflux-ai](https://github.com/Qetesh/miniflux-ai)** | 231 | 直接对接 Miniflux API/Webhook，LLM 摘要+翻译+分类，结果写回 Miniflux | ⭐⭐⭐⭐⭐ |
| [RSSbrew](https://github.com/yinan-c/RSSbrew) | 284 | RSS 中间件：聚合→关键词/LLM 过滤→摘要→输出新 RSS Feed | ⭐⭐⭐⭐ |
| [UglyFeed](https://github.com/fabriziosalmi/UglyFeed) | 305 | 相似文章聚类→LLM 改写/摘要→输出新 Feed | ⭐⭐⭐ |

**结论**：miniflux-ai 是 Miniflux 的天然伴侣，可 fork 扩展分类/标签逻辑。

---

### 三、全文提取工具链

| 工具 | ⭐ | F1 | 核心优势 | 推荐 |
|---|---|---|---|---|
| **[trafilatura](https://github.com/adbar/trafilatura)** | 5.8k | **0.958** | 原生 Markdown 输出、内置去重（Simhash）、元数据提取、专为 LLM/RAG 设计 | ✅ **首选** |
| [newspaper4k](https://github.com/AndyTheFactory/newspaper4k) | 1.1k | 0.949 | 最高精度（0.964），保守提取 | 备选 |
| [feedparser](https://github.com/kurtmckee/feedparser) | 2.4k | — | RSS 解析事实标准，畸形 Feed 处理最好 | ✅ **首选** |
| [extruct](https://github.com/scrapinghub/extruct) | 962 | — | 提取 JSON-LD/OpenGraph 结构化元数据 | 可选增强 |

**结论**：`feedparser` + `trafilatura` 是核心管道，10 行代码完成 RSS→Markdown。

---

### 四、知识图谱 & 知识库层

| 项目 | ⭐ | 做什么 | 与 Graphify 的关系 |
|---|---|---|---|
| **[Graphify](https://github.com/safishamsi/graphify)** | 31.8k | 文件夹→知识图谱+Wiki+可视化 | 你选定的核心组件 |
| **[Khoj](https://github.com/khoj-ai/khoj)** | 34.2k | AI 第二大脑，文档→语义搜索→对话 | 可作为检索/对话层补充 |
| [Microsoft GraphRAG](https://github.com/microsoft/graphrag) | 32.4k | 大规模实体关系提取→图谱 RAG | Graphify 的替代/互补方案 |

**结论**：Graphify 做图谱构建+可视化+Wiki，后续可加 Khoj 做语义检索/对话。

---

### 五、自动化 & CI/CD

| 组件 | ⭐ | 用途 |
|---|---|---|
| **[git-auto-commit-action](https://github.com/stefanzweifel/git-auto-commit-action)** | 2.5k | GitHub Actions 里自动 commit 变更 |
| [rss-fetch-action](https://github.com/Promptly-Technologies-LLC/rss-fetch-action) | — | 单 Feed→JSON→commit 的 Action |
| **[Pulsar](https://github.com/sou350121/Pulsar)** | 4 | RSS→LLM 评分→Markdown→GitHub push，最接近我们整体架构的参考项目 |

---

### 六、关键参考项目

**[Pulsar](https://github.com/sou350121/Pulsar)** — 虽然 star 少，但架构和你的需求几乎一致：

```
RSS feeds → LLM 评分/分类(⚡/🔧/📖/❌) → Markdown → GitHub Contents API push
```

它的 dedup 状态管理、GitHub API 推送、自愈机制都值得参考。

---

## 推荐技术栈总结

```
信源生成:     RSSHub（补充非标准 RSS 的网站）
RSS 聚合:     Miniflux（REST API + Webhook + 内置全文抓取）
LLM 处理:     miniflux-ai（fork 扩展，加分类/标签）
全文提取:     feedparser + trafilatura（原生 Markdown 输出）
去重:         URL 去重 + trafilatura 内置 Simhash
知识图谱:     Graphify（--wiki --update 增量构建）
可视化:       Graphify graph.html（vis.js 交互图）
自动化:       GitHub Actions cron + git-auto-commit-action
存储:         Git 仓库本身（Markdown 文件 + graphify-out/）
```

**你需要自己写的部分**：Miniflux webhook → 调用 trafilatura 提取全文 → 存为 Markdown → 触发 `graphify update` 的胶水脚本，大约 200-400 行 Python。

---

有什么想调整的方向？或者可以开始写详细的实现计划了？

---

## User

[analyze-mode]
ANALYSIS MODE. Gather context before diving deep:
CONTEXT GATHERING (parallel):
- 1-2 explore agents (codebase patterns, implementations)
- 1-2 librarian agents (if external library involved)
- Direct tools: Grep, AST-grep, LSP for targeted searches

IF COMPLEX - DO NOT STRUGGLE ALONE. Consult specialists:
- **Oracle**: Conventional problems (architecture, debugging, complex logic)
- **Artistry**: Non-conventional problems (different approach needed)

SYNTHESIZE findings before proceeding.
---
MANDATORY delegate_task params: ALWAYS include load_skills=[] and run_in_background when calling delegate_task.
Example: delegate_task(subagent_type="explore", prompt="...", run_in_background=true, load_skills=[])

---

知识图谱可视化我们后续再考虑，先研究rss

---

## Assistant (​Sisyphus - Ultraworker · opus 4.6 · 42.6s)



<thinking>
The user wants to focus on the RSS part first and skip the knowledge graph visualization research for now. Let me cancel the remaining background task (bg_82a676f9 - 知识图谱可视化) since it's no longer needed.

The user said "先研究rss" - they want to dig deeper into the RSS part. Let me think about what specifically needs deeper research.

From our previous research, we have a good overview of the RSS ecosystem. The user wants to go deeper. Let me think about what questions remain:

1. Miniflux vs building a lightweight RSS fetcher ourselves - for a personal knowledge base, do we really need a full RSS reader service (Miniflux requires PostgreSQL)?
2. The actual data flow and architecture for the RSS pipeline
3. How to handle the cron-based workflow with GitHub Actions
4. How miniflux-ai works in practice
5. The feedparser + trafilatura pipeline in detail

Actually, the user said "analyze mode" - they want me to gather more context and analyze deeper. Let me think about what aspects of RSS need deeper analysis.

Key open questions for RSS:
1. **Miniflux deployment complexity** - requires PostgreSQL, Docker - is that appropriate for a personal project that's supposed to run via git cron? There might be a simpler approach.
2. **Lightweight alternative** - could we just use feedparser + trafilatura directly in a Python script, run via GitHub Actions, without needing Miniflux at all?
3. **miniflux-ai integration patterns** - how exactly does it hook into Miniflux?
4. **RSSbrew as middleware** - could this replace the need for Miniflux entirely?
5. **Pulsar's architecture** - the closest reference project, worth deeper analysis

Actually, I think there's a tension in the current architecture proposal:
- The user said "RSS抓取的部分用git cron定时执行" - they want RSS fetching as a cron job, not a running service
- But Miniflux is a full running service with a database
- For a personal knowledge base that uses GitHub Actions cron, a simpler approach might be better: just feedparser + trafilatura as a Python script

Let me raise this concern and dig deeper into the simpler pipeline approach vs the Miniflux approach.

Wait, the user said "先研究rss" - they want me to research RSS more. Let me do focused research on the RSS pipeline options. Let me fire some explore/librarian agents to look at specific projects more deeply.

Actually, looking at this more carefully - the user is in "analyze mode" and wants me to gather context. Let me do targeted research:

1. Look deeper at Pulsar's RSS pipeline (the closest reference)
2. Look at miniflux-ai's actual code and integration pattern
3. Look at RSSbrew's filter/classify workflow
4. Consider if we even need Miniflux or can just use a lightweight script

Let me fire parallel research tasks.
</thinking>

好，先聚焦 RSS。取消知识图谱可视化的任务，然后深入研究 RSS 管道的具体实现方案。

有个架构问题需要先澄清：你说"RSS 用 git cron 定时执行"，但之前推荐的 Miniflux 是一个需要 PostgreSQL 的常驻服务——这两者有冲突。我需要深入对比两条路线：

- **轻量路线**：纯 Python 脚本 (feedparser + trafilatura)，GitHub Actions cron 跑，无需任何服务
- **服务路线**：部署 Miniflux + miniflux-ai，功能更完整但运维更重

让我深入调研几个关键参考项目的实际实现。

**Tool: background_cancel**

**Input:**
```json
{
  "taskId": "bg_82a676f9"
}
```

**Output:**
```
Task cancelled successfully

Task ID: bg_82a676f9
Description: 知识图谱可视化和LLM知识库方案
Session ID: ses_24fc0e1b1ffeA4RuB9e2IBfdYf
Status: cancelled
```

---

## Assistant (​Sisyphus - Ultraworker · opus 4.6 · 50.5s)

**Tool: task**

**Input:**
```json
{
  "subagent_type": "librarian",
  "description": "Pulsar RSS架构深度分析",
  "load_skills": [],
  "prompt": "CONTEXT: I'm designing a personal RSS aggregator + LLM knowledge base. The project \"Pulsar\" (https://github.com/sou350121/Pulsar) is the closest existing reference to our architecture: RSS feeds → LLM rating/classification → Markdown → GitHub push.\n\nGOAL: Deep-dive into Pulsar's actual implementation to understand its RSS pipeline, data flow, state management, and what we can reuse or learn from.\n\nREQUEST:\n1. Clone/browse the Pulsar repo and analyze its source code structure\n2. Specifically find and analyze:\n   - How it fetches RSS feeds (what library, async or sync, rate limiting?)\n   - How it tracks which articles have already been processed (dedup/state management)\n   - How it classifies/rates articles with LLM (what prompts, what model, what criteria?)\n   - How it converts articles to Markdown (format, frontmatter, metadata)\n   - How it pushes to GitHub (Contents API pattern, error handling)\n   - Its cron/scheduling mechanism\n3. Assess: What parts are well-designed and reusable? What are the weaknesses?\n4. Return concrete code snippets and file paths for the most interesting patterns.",
  "run_in_background": true
}
```

**Output:**
```
Background task launched.

Background Task ID: bg_e864aef1
Description: Pulsar RSS架构深度分析
Agent: librarian
Status: pending

System notifies on completion. Use `background_output` with task_id="bg_e864aef1" to check.

Do NOT call background_output now. Wait for <system-reminder> notification first.

<task_metadata>
session_id: ses_24fb1b59dffe1MHWdrKNEKcyoU
task_id: bg_e864aef1
background_task_id: bg_e864aef1
</task_metadata>

to continue: task(session_id="ses_24fb1b59dffe1MHWdrKNEKcyoU", load_skills=[], run_in_background=false, prompt="...")
```

**Tool: task**

**Input:**
```json
{
  "load_skills": [],
  "prompt": "CONTEXT: I'm designing an RSS pipeline that needs to filter and classify articles by topic before storing them. RSSbrew (https://github.com/yinan-c/RSSbrew) is an RSS middleware that does exactly this: aggregate feeds → filter (keyword/regex/LLM) → summarize → output.\n\nGOAL: Understand RSSbrew's filter and classification architecture in detail, to decide if we should use it as-is, fork it, or just steal its patterns.\n\nREQUEST:\n1. Browse the RSSbrew repo source code\n2. Specifically analyze:\n   - How does its filter system work? (keyword matching, regex, LLM-based classification)\n   - What LLM integration does it use? (OpenAI API? Ollama? configurable?)\n   - How does it define filter rules? (config file format, DSL?)\n   - How does it handle the feed-in → process → feed-out pipeline?\n   - Can it output Markdown files instead of RSS feeds?\n   - What's its deployment model? (Docker? standalone Python?)\n3. Assess: Is it lightweight enough to embed in a GitHub Actions workflow, or does it need a running server?\n4. Return the config format examples and key architectural decisions.",
  "run_in_background": true,
  "subagent_type": "librarian",
  "description": "RSSbrew过滤分类机制分析"
}
```

**Output:**
```
Background task launched.

Background Task ID: bg_ef197af2
Description: RSSbrew过滤分类机制分析
Agent: librarian
Status: pending

System notifies on completion. Use `background_output` with task_id="bg_ef197af2" to check.

Do NOT call background_output now. Wait for <system-reminder> notification first.

<task_metadata>
session_id: ses_24fb19074ffetNjAVafNQvOR2f
task_id: bg_ef197af2
background_task_id: bg_ef197af2
</task_metadata>

to continue: task(session_id="ses_24fb19074ffetNjAVafNQvOR2f", load_skills=[], run_in_background=false, prompt="...")
```

**Tool: task**

**Input:**
```json
{
  "description": "轻量RSS脚本方案调研",
  "load_skills": [],
  "prompt": "CONTEXT: I'm considering building a lightweight RSS-to-Markdown pipeline as a pure Python script (no services, no databases), designed to run in GitHub Actions on a cron schedule. The pipeline: feedparser parse → trafilatura extract full text → save as Markdown → git commit.\n\nGOAL: Find the best existing lightweight RSS-to-Markdown scripts/projects on GitHub that follow this pattern, and understand best practices for state management without a database.\n\nREQUEST:\n1. Search GitHub for lightweight Python scripts that:\n   - Fetch RSS feeds and save articles as Markdown files\n   - Run as cron jobs (GitHub Actions or system cron)\n   - Use git as the storage/state backend\n   - Minimal dependencies\n\n2. Specifically research:\n   - How do people handle \"already seen\" state without a database? (JSON file in repo? git log? SQLite committed to repo?)\n   - What Markdown frontmatter format is common for archived articles? (title, date, source, tags, etc.)\n   - How to handle rate limiting and politeness when fetching full articles?\n   - How to organize the file structure (by date? by source? by topic?)\n   - Error handling patterns for flaky RSS feeds\n\n3. Also search for:\n   - osmosfeed (https://github.com/nicefact/osmosfeed or osmoscraft/osmosfeed) cache pattern\n   - Any \"digital garden\" or \"second brain\" projects that auto-ingest from RSS\n\n4. Return concrete examples of: state file format, Markdown frontmatter schema, file organization patterns.",
  "run_in_background": true,
  "subagent_type": "librarian"
}
```

**Output:**
```
Background task launched.

Background Task ID: bg_4279750f
Description: 轻量RSS脚本方案调研
Agent: librarian
Status: pending

System notifies on completion. Use `background_output` with task_id="bg_4279750f" to check.

Do NOT call background_output now. Wait for <system-reminder> notification first.

<task_metadata>
session_id: ses_24fb19061ffe1ExTYNZVswMSvy
task_id: bg_4279750f
background_task_id: bg_4279750f
</task_metadata>

to continue: task(session_id="ses_24fb19061ffe1ExTYNZVswMSvy", load_skills=[], run_in_background=false, prompt="...")
```

---

## Assistant (​Sisyphus - Ultraworker · opus 4.6 · 24.5s)

3 路 Librarian 并行深挖中：

1. **Pulsar** — 最接近的参考项目，分析其 RSS→LLM→Markdown→GitHub 全链路实现
2. **RSSbrew** — 分析其过滤/分类机制，看是否可直接复用
3. **轻量脚本方案** — 搜索纯 Python 脚本 + GitHub Actions cron 的最佳实践（状态管理、Markdown 格式、文件组织）

等结果回来后整合分析。

---

