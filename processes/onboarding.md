---
title: New customer onboarding
owner: Lukas Weber
source: pack §1 (The company), §4 (How things actually work)
last_verified: 2026-11-03
---

# New customer onboarding

**Owner:** Lukas Weber (Customer Success), end to end.
**Step-by-step:** `runbooks/new-customer-onboarding.md`.

## Why it matters

Onboarding speed is Fernway's whole positioning: the pitch is that a venue is live in under a day (`company/overview.md`). The metric is **T2L**, time to live: contract signed to first schedule published (`glossary.md`).

## Flow

Contract signed in HubSpot -> setup call (45 minutes) -> venue and staff import from the customer's CSV -> pay rules configured for the country -> customer publishes their first schedule -> 7-day check-in call -> handover to support.

Typical T2L today: 1 to 3 days.

## Hand-offs

| From | To | When |
|---|---|---|
| Sales (contract in HubSpot) | Lukas Weber | Contract signed |
| Lukas Weber | Support (Jonas Berg, `processes/support-escalation.md`) | After the 7-day check-in call |

## Known problem: the importer

The CSV importer fails on:

- names with non-Latin characters;
- files exported from Apple Numbers.

**Noor Haddad** knows the workaround. It has never been written down, so Lukas messages Noor every time. The workaround itself is **not in the brain** yet (`open-questions.md`). When Noor writes it down, it goes into `runbooks/new-customer-onboarding.md` through a pull request.
