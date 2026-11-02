# How we work

## 1. Tickets
Lukas (product) writes every piece of work as a **GitHub issue**. The issue says
*what* should happen and *why*. It is the source of truth for a PR: if the code
and the ticket disagree, the code is wrong or the ticket needs updating first.

## 2. Branches
One branch per ticket, cut from `main`:

```
feature/<issue>-short-name     # new behaviour
fix/<issue>-short-name         # bug fix
chore/<short-name>             # tooling, deps, no behaviour change
```

Nobody pushes directly to `main`.

## 3. Pull requests
- Open a PR against `main` and fill in the PR template.
- Link the ticket with `Closes #<issue>` so it closes on merge.
- **One PR = one change.** Unrelated fixes get their own PR.
- Keep PRs small. Anything over ~400 changed lines will be asked to split.
- **CI** (ruff + pytest) runs on every push. A red PR is not reviewed.

## 4. Review
- Every PR needs **one approval** before merge.
- Reviewers check the PR against the **ticket**, not only against itself.
- Comment prefixes:
  - **`blocking:`** must be fixed before merge
  - **`nit:`** small style/naming point, author decides
  - **`question:`** reviewer wants to understand something
- Authors respond to every comment: fix it, or explain why not.
- After pushing fixes, the author re-requests review.

## 5. Merge
- **Squash and merge** only, so each PR becomes one commit on `main`.
- The author merges once approved and CI is green, then deletes the branch.
- `main` is deployed several times a week.

## House rules
- **Money is integer cents.** `4990` means €49.90. Never use `float` for money.
- **Prices in the catalog are gross** (VAT included, 19 %).
- Customer-facing error messages go through the exceptions in `voltbox/errors.py`.
- New behaviour needs tests. Bug fixes need a test that would have caught the bug.
- No `print()` in library code. Use `logging`.
