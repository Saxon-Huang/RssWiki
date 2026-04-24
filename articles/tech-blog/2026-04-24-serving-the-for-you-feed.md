---
category: tech-blog
date: '2026-04-24'
fetched_at: '2026-04-24T01:52:20Z'
source: Simon Willison
tags:
- go
- scaling
- sqlite
- software-architecture
- tailscale
- bluesky
title: Serving the For You feed
url: https://simonwillison.net/2026/Apr/24/serving-the-for-you-feed/#atom-everything
---

24th April 2026 - Link Blog
Serving the For You feed. One of Bluesky's most interesting features is that anyone can run their own custom "feed" implementation and make it available to other users - effectively enabling custom algorithms that can use any mechanism they like to recommend posts.
spacecowboy runs the For You Feed, used by around 70,000 people. This guest post on the AT Protocol blog explains how it works.
The architecture is fascinating. The feed is served by a single Go process running on SQLite on a "gaming" PC in spacecowboy's living room - 16 cores, 96GB of RAM and 4TB of attached NVMe storage.
Recommendations are based on likes: what else are the people who like the same things as you liking on the platform?
That Go server consumes the Bluesky firehouse and stores the relevant details in SQLite, keeping the last 90 days of relevant data which currently uses around 419GB of SQLite storage.
Public internet traffic is handled by a $7/month VPS on OVH, which talks to the living room server via Tailscale.
Total cost is now $30/month: $20 in electricity, $7 in VPS and $3 for the two domain names. spacecowboy estimates that the existing system could handle all ~1 million daily active Bluesky users if they were to switch to the cheapest algorithm they have found to work.
Recent articles
- Extract PDF text in your browser with LiteParse for the web - 23rd April 2026
- A pelican for GPT-5.5 via the semi-official Codex backdoor API - 23rd April 2026
- Is Claude Code going to cost $100/month? Probably not - it's all very confusing - 22nd April 2026
