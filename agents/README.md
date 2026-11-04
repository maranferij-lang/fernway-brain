---
title: AI automations register
owner: Hana Kim
source: pack §2 (The team), §3 (Tools), §7 (Other things that came up)
last_verified: 2026-11-03
---

# AI automations register

Every automation or AI tool Fernway runs gets a card here: what it does, where it runs, who owns it, what data it touches, what is unknown. If it is not registered here, assume nobody else knows it exists.

Technical review: Ivan Petrenko (`CONTRIBUTING.md`).

| Name | What it is | Runs where | Owner | Status | Card |
|---|---|---|---|---|---|
| n8n internal automations | Six or seven workflows | Ivan Petrenko's own n8n instance | Ivan Petrenko | Running. Nobody else can explain them. | `agents/n8n-instance.md` |
| Claude for support draft replies | Claude drafting replies to support requests | Unknown | Unknown | Trial. No usage rules yet. | `agents/claude-support-drafts.md` |

## Adding a card

Copy an existing card. Fill in every field. Write "unknown" where the source does not say, and add the gap to `open-questions.md`. Never put a key, token, login, webhook URL or password on a card. Record that a secret exists and where it should live, never its value.
