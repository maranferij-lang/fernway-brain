---
title: Glossary
owner: Hana Kim
source: pack §1 (The company), §4 (How things actually work), §5 (Team rules), §6 (How people talk here)
last_verified: 2026-11-03
---

# Glossary: how Fernway talks

Terms as this team uses them. If a word means something different here than elsewhere, this file wins.

## Account vs venue

The pair new hires mix up most often.

| | Account | Venue |
|---|---|---|
| What it is | The customer relationship | A paying location under an account |
| How many | One account can have many venues | |
| Contract | **Per account** | |
| Billing | | **Per venue**: EUR 39 per venue per month (`company/pricing.md`) |
| Today | About 40 accounts | About 140 paying venues |

Test: counting what gets billed? Count venues. Counting contracts? Count accounts.

## Pay rules

The per-country break and overtime configuration set during onboarding (step 4 in `runbooks/new-customer-onboarding.md`). Fernway Shifts checks schedules against these rules.

## The importer

The CSV staff-import tool used in onboarding. Known to fail on names with non-Latin characters and on files exported from Apple Numbers (`processes/onboarding.md`).

## T2L

Time to live: from **contract signed** to **first schedule published**. The main onboarding metric. Typical today: 1 to 3 days (`processes/onboarding.md`).

## Ghost shift

A published shift nobody claimed. The single most common support complaint (`processes/support-escalation.md`).

## Friday freeze

The no-deploys-on-Friday rule (team rule 5, `runbooks/release.md`).

## Mara-check

A pricing exception that needs the CEO, Mara Voss: anything below EUR 39 per venue per month or beyond the 15% annual-prepay discount (`company/pricing.md`).

## Activation

**No agreed definition.** Everyone uses the word; nobody has defined it.

| Who | What they mean |
|---|---|
| Sales | First published schedule |
| Lukas Weber (Customer Success) | A full week scheduled |
| Metabase dashboard | Something else again (what exactly is not recorded) |

Until someone decides, say which meaning you use, or say "first published schedule" / "full week scheduled" instead of "activation". Tracked in `open-questions.md`.
