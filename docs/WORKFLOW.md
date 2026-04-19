# Librify — Agent-Driven Development Workflow

## Overview

Each feature follows a 6-step pipeline. Always work on a dedicated branch — never commit directly to `main`.

---

## Step 1 — Write the Feature Spec

```
/spec <feature-name>
```

Claude interviews you with 6 questions:

1. User story
2. Acceptance criteria
3. API / data contracts
4. Edge cases & error states
5. Out of scope
6. Success metrics

Output: `docs/specs/<feature-name>.spec.md`

At the end Claude presents an approval gate — choose **(a) proceed**, **(b) revise**, or **(c) stop**.

---

## Step 2 — Create a Feature Branch

```bash
git checkout -b feat/<feature-name>
```

Always branch from an up-to-date `main`:

```bash
git checkout main && git pull && git checkout -b feat/<feature-name>
```

---

## Step 3 — Implement the Feature

```
/feature-dev
```

Point it at the spec file when prompted: `docs/specs/<feature-name>.spec.md`

The agent will:

1. Explore the codebase and propose an architecture — **you approve before any code is written**
2. Implement the feature (components, NgRx store, services, routes)
3. Write Vitest unit tests alongside each file
4. Run `npm test -- --watch=false` → fix any failures → re-run until green
5. Write Playwright E2E tests covering the acceptance criteria flows
6. Start the dev server and run `npx playwright test --project=chromium` → fix any failures → re-run until green
7. Stop the dev server

The agent does **not** commit — that is Step 5.

---

## Step 4 — Code Review

```
/review-pr
```

Six specialized review agents check the changes in parallel:

- Architecture & conventions
- NgRx store correctness
- Angular component patterns
- Styling (Material M3 + Tailwind)
- Test coverage quality
- Security & edge cases

The agent applies fixes automatically. You approve the final diff.

---

## Step 5 — Commit

```
/commit
```

This will:

1. Run lint-staged (Prettier + ESLint) via the pre-commit hook
2. Run CommitLint to enforce Conventional Commits format
3. Create the commit with a message like `feat(books): add book search`

If the pre-commit hook fails, the agent fixes the issue and creates a **new** commit — it never uses `--no-verify`.

---

## Step 6 — Push and Open a PR

```
/create-pr
```

This will:

1. Push the branch to GitHub
2. Open a pull request against `main` with a summary and test plan

---

## Step 7 — CI Validates (Automatic)

GitHub Actions runs two jobs automatically on every push:

| Job | What it checks |
|-----|---------------|
| `quality` | Format → Lint → Build → Unit tests |
| `e2e` | Playwright Chromium tests on a clean Linux environment |

Branch protection on `main` blocks merge until both jobs are green.

---

## Step 8 — Merge

Once CI is green, merge the PR on GitHub. Then locally:

```bash
git checkout main && git pull
```

Repeat from Step 1 for the next feature.

---

## Quick Reference

```
/spec <name>          →  interview → docs/specs/<name>.spec.md
git checkout -b feat/<name>
/feature-dev          →  implement + test + fix locally
/review-pr            →  automated code review + fixes
/commit               →  pre-commit hook + conventional commit
/create-pr            →  push + open PR
                         CI runs automatically
                         merge on GitHub when green
git checkout main && git pull
```

---

## Rules That Govern Agent Behavior

| Rule file | Covers |
|-----------|--------|
| `.claude/rules/angular.md` | Component conventions, reactivity, routing |
| `.claude/rules/ngrx.md` | NgRx slice patterns, store usage |
| `.claude/rules/styling.md` | Tailwind + Material conventions |
| `.claude/rules/testing.md` | Unit + E2E requirements, local run mandate |
| `.claude/rules/commits.md` | Conventional Commits format |
