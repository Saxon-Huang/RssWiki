---
category: tech-blog
date: '2026-04-15'
fetched_at: '2026-04-23T18:57:23Z'
source: Simon Willison
tags:
- zig
title: 'Zig 0.16.0 release notes: "Juicy Main"'
url: https://simonwillison.net/2026/Apr/15/juicy-main/#atom-everything
---

15th April 2026 - Link Blog
Zig 0.16.0 release notes: "Juicy Main" (via) Zig has really good release notes - comprehensive, detailed, and with relevant usage examples for each of the new features.
Of particular note in the newly released Zig 0.16.0 is what they are calling "Juicy Main" - a dependency injection feature for your program's main()
function where accepting a process.Init
parameter grants access to a struct of useful properties:
const std = @import("std");
pub fn main(init: std.process.Init) !void {
/// general purpose allocator for temporary heap allocations:
const gpa = init.gpa;
/// default Io implementation:
const io = init.io;
/// access to environment variables:
std.log.info("{d} env vars", .{init.environ_map.count()});
/// access to CLI arguments
const args = try init.minimal.args.toSlice(
init.arena.allocator()
);
}
Recent articles
- Is Claude Code going to cost $100/month? Probably not - it's all very confusing - 22nd April 2026
- Where's the raccoon with the ham radio? (ChatGPT Images 2.0) - 21st April 2026
- Changes in the system prompt between Claude Opus 4.6 and 4.7 - 18th April 2026
