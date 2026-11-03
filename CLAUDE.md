# Fernway brain: instructions for Claude

This repository is Fernway's company brain. Fernway is a remote-first B2B SaaS company (product: Fernway Shifts). Every fact in here comes from one source, the Fernway context pack, and each doc says which section of the pack it comes from.

## How to answer questions

1. Answer only from files in this repository. Do not fill gaps with general knowledge, assumptions about "typical startups", or guesses.
2. Cite the file for every fact, as a path: `(processes/onboarding.md)`. If you combine two files, cite both.
3. If the answer is not in the repo, say exactly "not in the brain". Then say who is the most likely owner to ask, only if a doc names one.
4. If the question touches anything listed in `open-questions.md`, say it is open, quote what the repo says about each side, and do not pick an answer.
5. If two docs disagree, say so and cite both. Do not resolve it yourself.
6. Check `last_verified` in the front matter. If it is older than 90 days, warn that the doc may be stale.
7. Use the team's words as defined in `glossary.md`. "Account" and "venue" are not the same thing. "Activation" has no agreed meaning.
8. Keep answers short: the answer, the source file, the owner to contact if one is named.

## Where things are

| Path | What it holds |
|---|---|
| `README.md` | Start here: map of the repo for a new colleague |
| `company/` | What Fernway is, pricing rules, team rules, tools |
| `team/who-owns-what.md` | Roles and who owns which process |
| `processes/` | How work flows: onboarding, leads, support, billing, releases, hiring |
| `runbooks/` | Numbered step-by-step procedures (releases, customer onboarding) |
| `agents/` | Register of AI automations Fernway already runs |
| `glossary.md` | How this team talks: terms with precise meanings |
| `open-questions.md` | Things the pack does not settle. Not facts. |
| `CONTRIBUTING.md` | Hard rules, review flow, what is excluded on purpose |
| `scripts/check_docs.py` | Front matter and sensitive-data check, runs in CI |

## Rules when you change anything here

These apply to you exactly as they apply to people (see `CONTRIBUTING.md`).

1. Never commit to `main`. Work on a branch and open a pull request.
2. Every doc needs front matter with `owner`, `source` (pack section, as `pack §N`) and `last_verified` (YYYY-MM-DD).
3. If the pack does not say it, it goes into `open-questions.md`, never into a doc as fact.
4. Never write secrets (API keys, tokens, passwords, logins), customer data or exports, compensation, or personal contact details. Not even as examples. Not even partly masked.
5. Do not paste customer data into this session or into an issue (team rule 3, `company/team-rules.md`).
6. Run `python3 scripts/check_docs.py` before opening a pull request. It must pass.
7. When you update a fact, update `last_verified` and say in the PR which pack section you checked.
