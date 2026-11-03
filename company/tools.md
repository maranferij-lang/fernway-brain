---
title: Tools and what each is for
owner: Hana Kim
source: pack §2 (The team), §3 (Tools)
last_verified: 2026-11-03
---

# Tools and what each is for

Hana Kim is the tooling admin (pack §2). No credentials are kept in this repo; they live in 1Password (`company/team-rules.md`, rule 4).

| Tool | Used for | Notes |
|---|---|---|
| Slack | Main channel for everything | Most decisions happen in threads and are never recorded elsewhere. |
| Notion | Around 60 pages | Most were written in the first six months and never touched again. |
| HubSpot | CRM and sales pipeline | New contracts and inbound leads land here. Holds customer data (rule 3). |
| Linear | Engineering tickets | Start of every release (`runbooks/release.md`). |
| Intercom | Customer support inbox | Start of support escalation (`processes/support-escalation.md`). Also an inbound lead source. |
| Stripe | Billing and invoices | Holds customer data (rule 3). See `processes/billing.md`. |
| Google Workspace | Docs, shared drive, calendars | |
| Metabase | Dashboards over the production database | The team shares one read-only login; the credentials sit in 1Password. |
| n8n | Ivan Petrenko's own instance for internal automations | See `agents/n8n-instance.md`. |
| 1Password | Where secrets are supposed to live | |

## Known risks

- **Shared Metabase login.** One read-only login for the whole team. Access is not per person.
- **API keys inside n8n nodes.** A couple of n8n workflows have API keys pasted directly into the nodes instead of 1Password (`agents/n8n-instance.md`).
