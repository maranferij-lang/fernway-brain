---
title: Team rules
owner: Hana Kim
source: pack §5 (Team rules)
last_verified: 2026-11-03
---

# Team rules

The six rules Fernway works by, as written in the source.

1. **No decisions in DMs.** Anything affecting more than one person goes in a public Slack channel.
2. **Answer the same question twice and it gets written down.** In practice nobody does this; it is the rule the team breaks most often. This repo is where it gets written down (`CONTRIBUTING.md`, "How the brain stays alive").
3. **Customer data stays in the systems it lives in:** HubSpot, Stripe, the production database. No exports into docs, spreadsheets, or AI tools.
4. **Secrets live in 1Password.** Never in Slack, never in a document, never in a repo.
5. **No deploys on Friday.** The team calls this the Friday freeze (`glossary.md`, `runbooks/release.md`).
6. **English is the working language,** including in country channels.

## Where rules meet reality

- Rule 3 and the support-draft trial with Claude: there are no rules yet for what may be pasted into Claude (`agents/claude-support-drafts.md`, `open-questions.md`).
- Rule 4 and n8n: some n8n workflows have API keys pasted directly into the nodes (`agents/n8n-instance.md`).
