---
title: "Agent card: n8n internal automations"
owner: Ivan Petrenko
source: pack §2 (The team), §3 (Tools)
last_verified: 2026-11-03
---

# Agent card: n8n internal automations

| Field | Value |
|---|---|
| What | Six or seven internal automation workflows |
| Runs where | Ivan Petrenko's own n8n instance |
| Built by | Ivan Petrenko, alone |
| Owner | Ivan Petrenko |
| Who else understands it | Nobody |
| Workflow names and purposes | Unknown |
| Triggers and schedules | Unknown |
| Systems it connects to | Unknown |
| Data it touches | Unknown |

## Risks

1. **Secrets in nodes.** A couple of the workflows have API keys pasted directly into the nodes. Team rule 4 says secrets live in 1Password (`company/team-rules.md`). The key values are not recorded anywhere in this repo and must never be.
2. **Single owner.** Only Ivan can explain the workflows.
3. **Personal instance.** The workflows run in Ivan's own instance, not a company one.

## What is needed to complete this card

Ivan Petrenko lists each workflow (name, trigger, what it does, which systems, whether it touches customer data). Tracked in `open-questions.md`.
