---
title: "Runbook: release to production"
owner: Ivan Petrenko
source: pack §4 (How things actually work), §5 (Team rules)
last_verified: 2026-11-03
---

# Runbook: release to production

**Owner:** Ivan Petrenko.
**Use when:** a change in Linear is ready to go out.

## Steps

1. Make sure the work has a Linear ticket.
2. Open a pull request for it.
3. Ana Silva tests it on staging.
4. Check the day. Deploy only on **Tuesday or Thursday**.
5. If it is Friday, stop. Friday freeze: no deploys on Friday (team rule 5).
6. Deploy.

## Not in the brain

- The deploy command or tooling.
- How staging is reset. Only Ana Silva knows (`open-questions.md`).
- Who tests on staging while Ana is away for three weeks in August.
- What to do if a release breaks production, beyond the fact that Noor Haddad is on call for production incidents (`processes/support-escalation.md`).
