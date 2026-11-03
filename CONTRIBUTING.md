# Contributing to the Fernway brain

The same rules apply to people and to AI agents (Claude Code, `@claude` on GitHub). No exceptions for either.

## Hard rules

1. **Nothing lands without a pull request.** No direct pushes to `main`. The only exception was the first commit that created the repo.
2. **Every doc has front matter** with `owner`, `source` and `last_verified`:

   ```yaml
   ---
   title: Short title
   owner: Name of the Fernway person who keeps this true
   source: pack §4 (How things actually work)
   last_verified: 2026-11-03
   ---
   ```

   `source` names the section of the Fernway context pack the facts come from. `last_verified` is the date someone last checked the doc against its source.
3. **If the source does not say it, it is not a fact.** Put it in `open-questions.md` with what is known, who disagrees, and who could decide. Do not write a guess into a doc, however reasonable.
4. **No secrets, no customer data, no compensation, no personal contact details.** See "Excluded on purpose" below.
5. **`python3 scripts/check_docs.py` must pass.** CI runs it on every pull request.
6. **The doc owner (or the reviewer below) approves the change.** Technical docs (releases, agents, scripts, workflows) are reviewed by Ivan Petrenko.

## Who owns what

| Area | Owner |
|---|---|
| The repo as a whole, rules, open questions, glossary | Hana Kim |
| Technical docs review (releases, agents, `scripts/`, `.github/`) | Ivan Petrenko |
| `processes/onboarding.md`, `runbooks/new-customer-onboarding.md` | Lukas Weber |
| `processes/inbound-leads.md` | Priya Raman |
| `processes/support-escalation.md` | Jonas Berg |
| `processes/billing.md` | Hana Kim |
| `processes/releases.md`, `runbooks/release.md` | Ivan Petrenko |
| `company/pricing.md`, `processes/hiring.md` | Mara Voss |

**GitHub accounts.** Fernway people do not have GitHub accounts in this repo yet. Every line in `.github/CODEOWNERS` points to the repo creator's account (`maranferij-lang`) as a stand-in. A comment above each line names the real Fernway owner. When owners get accounts, replace the stand-in handle line by line.

## How the brain stays alive

1. **Answered twice, written down.** Team rule 2 is the rule Fernway breaks most often (pack §5). If you answer the same question twice in Slack, Intercom or a call, open a pull request with the answer, or an issue if you do not know the answer.
2. **Monthly review.** On the 1st of each month a GitHub Action opens a "Docs review" issue. It lists every doc whose `last_verified` is older than 90 days. Each owner re-checks their docs, fixes or confirms them, and bumps `last_verified` in a pull request. Hana Kim closes the issue.
3. **The 90-day threshold is an assumption** made when the repo was built, not a Fernway decision. It is listed in `open-questions.md`.
4. **Open questions get decided, then moved.** When someone with authority decides an open question, the decision goes into the right doc in a pull request (citing who decided and when) and the entry leaves `open-questions.md`.

## Excluded on purpose

These categories were in the source material and were deliberately left out. Values are not repeated here.

- Compensation bands and salaries, for any role.
- Personal contact details of customers or staff: phone numbers, personal messaging apps, personal emails.
- Customer names, customer records and exports of any kind (team rule 3: customer data stays in HubSpot, Stripe and the production database).
- Unresolved commercial matters about specific accounts, such as pricing migrations that have not been decided or announced.
- Secrets: API keys, tokens, passwords and shared logins. This includes the Metabase shared login and the keys pasted into n8n nodes. Their existence is recorded as a risk in `agents/`, never their values.
- Personal notes and opinions about colleagues.

Where these belong instead: secrets in 1Password, customer data in the system it lives in, compensation outside GitHub entirely.

## Opening a pull request

1. Branch from `main`: `git switch -c docs/short-description`.
2. Make the change. Update `last_verified` on every doc you checked.
3. Run `python3 scripts/check_docs.py`.
4. Open the pull request and fill in the template.
