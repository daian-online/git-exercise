# Acme Retail — `acme-inventory` service

Acme Retail runs a small backend service, `acme-inventory`, that tracks
warehouse stock, prices orders, and processes refunds. It's maintained by a
small backend team:

- **Priya Nair** — senior engineer. Careful, reviews everything, ships small
  clean commits.
- **Marcus Lee** — mid-level engineer. Ships fast, sometimes too fast —
  known for bundling unrelated changes into one commit.
- **Dana Kim** — engineer, currently on leave. Was mid-feature on refunds
  before she left.
- **Sam Ortiz** — QA. Files the tickets you'll find in `docs/`.
- **You** — on-call engineer this week. Everything in `docs/` is yours to
  resolve.

This repository is both the real (if small) codebase, and an open set of
incidents currently affecting it. Work through the tickets in `docs/` in
order — each one tells you what's wrong and what everyone involved knows
about it, not which git command to run. That part's on you.

## The codebase

- `inventory.py` — warehouse stock tracking.
- `pricing.py` — discount and tax calculations.
- `orders.py` — order creation and totals (built on `pricing.py`).
- `refunds.py` — refund calculations (built on `pricing.py`).
- `scripts/check_total.py` — a standalone regression checker QA uses.
- `tests/` — one test file per module. Run all of them with `pytest`, or a
  single one with `pytest tests/test_<name>.py`.

## Engineering Git Playbook

House rules for working on this repo. When a ticket in `docs/` doesn't spell
out which git command to use, this is what should guide your decision:

1. **Revert vs. reset.** `main` deploys automatically on every push and the
   rest of the team pulls from it constantly. Never use `git reset` to
   remove a commit that's already been pushed to a shared branch — it
   rewrites history other people already have. Use `git revert` instead.
   `git reset` is fine for branches only you have ever touched.
2. **Fast-forward vs. `--no-ff`.** Merge a feature branch with `--no-ff` if
   it represents real, multi-commit work — it keeps that work visible as a
   unit in `git log`. A trivial single-commit fix can just be fast-forwarded;
   there's no meaningful history to preserve.
3. **Rebase vs. merge.** Never rebase a branch that anyone besides you has
   pulled or built on top of — you'd be rewriting commits they already have.
   Your own local, unpushed branch is fair game: rebase it onto the latest
   `main` for a clean, linear history, then merge it in (it'll fast-forward).
4. **Reset vs. restore.** `git reset` moves your branch pointer — use it to
   uncommit. `git restore` changes your working tree or staging area without
   moving the branch pointer — use it to discard edits or unstage files.
   Don't reach for `reset --hard` to fix a single file; use `restore`.
5. **Revert vs. fix-forward.** `git revert` undoes an *entire* commit. If a
   bad commit bundled a real fix together with a regression, reverting
   throws away the good part too. In that case, track down the exact bad
   lines and fix them forward in a new commit instead.

## Working through this exam

1. Fork this repository.
2. Work through `docs/chapter1.md` through `docs/chapter5.md`, in order, in
   your fork. Each one is self-contained but assumes the previous ones are
   done.
3. Each ticket tells you which test file to run to confirm you're done.
4. When you've worked through all five, open a pull request from your fork
   back to this repository so it can be reviewed.
