---
category: tech-blog
date: '2026-04-20'
fetched_at: '2026-04-23T18:57:23Z'
source: Simon Willison
tags:
- spreadsheets
- datasette
- google
title: SQL functions in Google Sheets to fetch data from Datasette
url: https://simonwillison.net/2026/Apr/20/datasette-sql/#atom-everything
---

20th April 2026
I put together some notes on patterns for fetching data from a Datasette instance directly into Google Sheets - using the importdata()
function, a "named function" that wraps it or a Google Apps Script if you need to send an API token in an HTTP header (not supported by importdata()
.)
Here's an example sheet demonstrating all three methods.
Recent articles
- Is Claude Code going to cost $100/month? Probably not - it's all very confusing - 22nd April 2026
- Where's the raccoon with the ham radio? (ChatGPT Images 2.0) - 21st April 2026
- Changes in the system prompt between Claude Opus 4.6 and 4.7 - 18th April 2026
