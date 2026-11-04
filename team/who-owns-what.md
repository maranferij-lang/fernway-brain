---
title: Who owns what
owner: Hana Kim
source: pack §2 (The team), §4 (How things actually work)
last_verified: 2026-11-03
---

# Who owns what

Roles only. Personal contact details are not kept here (`CONTRIBUTING.md`, "Excluded on purpose"); use Slack.

## People

| Person | Role | Owns |
|---|---|---|
| Mara Voss | CEO, co-founder | Fundraising, pricing, top 5 accounts. Every pricing exception (Mara-check). Decides on hires. |
| Ivan Petrenko | CTO, co-founder | Product and engineering. Releases. Built all internal automations, alone, in his own n8n instance. Escalation point for anything involving customer data. |
| Noor Haddad | Backend lead | On call for production incidents. Knows the CSV importer workaround. |
| Tom Backer | Frontend | |
| Ana Silva | QA and technical support (50/50) | Tests releases on staging. Technical support escalations. Only person who knows how staging is reset. |
| Sofia Marchetti | Head of Sales | |
| Daniel Okafor | Account Executive | Runs demos. |
| Priya Raman | SDR | Outbound and inbound lead qualification. |
| Lukas Weber | Customer Success | Customer onboarding, end to end. |
| Emma Doyle | Marketing (part-time contractor, 2 days a week) | |
| Hana Kim | Ops lead | Billing, invoices, vendor accounts, tooling admin. Owner of this repo. |
| Jonas Berg | Support agent | First-line support. |
| Head of People | Open role | Unfilled since March. |

Teams: engineering (4, including Ivan), go-to-market (5), operations (3, including the open Head of People role).

## External

- A Berlin bookkeeping firm.
- A freelance designer, used per project.

## Process owners

| Process | Owner | Doc |
|---|---|---|
| New customer onboarding | Lukas Weber | `processes/onboarding.md` |
| Inbound leads | Priya Raman | `processes/inbound-leads.md` |
| Support escalation | Jonas Berg | `processes/support-escalation.md` |
| Billing | Hana Kim | `processes/billing.md` |
| Releases | Ivan Petrenko | `processes/releases.md` |
| Hiring | No process; Mara Voss decides | `processes/hiring.md` |
| Documentation | Nobody, per the source. This repo proposes Hana Kim. | `open-questions.md` |

## Single points of failure

- **Ana Silva** is the only person who knows how the staging environment is reset. She is away for three weeks in August.
- **Noor Haddad** is the only person who knows the CSV importer workaround.
- **Ivan Petrenko** is the only person who can explain the n8n workflows.
- **Mara Voss** approves every pricing exception.

All four are in `open-questions.md`.
