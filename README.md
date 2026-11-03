# Fernway brain

Everything Fernway knows about how it works, in one versioned place. Plain Markdown, reviewed through pull requests, readable by a new colleague and by Claude.

If something here is wrong, do not work around it: open a pull request or an issue. A wrong doc in this repo is worse than a missing one.

## Start here

| If you want to know... | Read |
|---|---|
| What Fernway sells, to whom, for how much | `company/overview.md`, `company/pricing.md` |
| The six team rules | `company/team-rules.md` |
| Which tool is used for what | `company/tools.md` |
| Who owns what | `team/who-owns-what.md` |
| How a process works (onboarding, leads, support, billing, releases, hiring) | `processes/` |
| Exactly what to do, step by step | `runbooks/` |
| Which AI automations are running and who owns them | `agents/README.md` |
| What a word means here (T2L, ghost shift, Mara-check...) | `glossary.md` |
| What nobody has decided yet | `open-questions.md` |
| How to add or change something | `CONTRIBUTING.md` |

## Using the brain day to day

1. Ask Claude Code inside this folder. `CLAUDE.md` tells it to answer only from these files and to cite them.
2. On GitHub, open an issue and mention `@claude` with your question.
3. If you had to answer the same question twice in Slack, put the answer here (team rule 2). See `CONTRIBUTING.md`.
4. Once a month a "Docs review" issue opens automatically. Owners re-check their docs and bump `last_verified`.

## Why this repo exists

Fernway's decisions live in Slack threads and about 60 Notion pages that nobody has touched since the first six months (pack §3). New people learn from whoever has time that week (pack §2). This repo is the alternative: small, sourced, owned, and reviewed.
