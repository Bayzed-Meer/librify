# Librify — Claude Code Project Memory

Librify is a library management web application built with Angular 21.

---

## Tech Stack

- **Framework**: Angular 21, standalone, OnPush, signals
- **State**: NgRx 21 (store, effects, devtools)
- **UI**: Angular Material 21 (M3) + Tailwind CSS v4
- **Testing**: Vitest (unit), Playwright (E2E)
- **Language**: TypeScript 5.9, strict mode
- **Linting**: angular-eslint, Prettier (100 chars, single quotes)
- **Commits**: Conventional Commits via CommitLint

---

## Dev Commands

```bash
npm start              # ng serve — http://localhost:4200 (HMR)
npm test               # Vitest unit tests
npm run build          # production build
ng build               # run after generating files — catches type errors early
npm run lint           # eslint src/**/*.ts src/**/*.html
npm run format         # prettier --write
npm run format:check   # CI check
npm run e2e            # playwright test
npm run e2e:ui         # visual mode
npm run e2e:debug      # step debugger
```

---

## Folder Structure

```
src/app/
  features/<name>/
    <name>.routes.ts        # lazy route config + store providers
    <name>.component.ts     # smart/container component
    components/             # presentational children
    store/                  # NgRx slice: state, actions, reducer, effects, selectors
    services/
  core/
    services/ guards/ interceptors/
  shared/
    components/ pipes/ utils/
```

---

## Key Files

| File | Purpose |
|------|---------|
| `src/main.ts` | Bootstrap |
| `src/app/app.config.ts` | Root providers (router, store, devtools) |
| `src/app/app.routes.ts` | Root routes — keep minimal, lazy-load features |
| `src/styles.scss` | Material M3 theme via `mat.define-theme()` |
| `src/tailwind.css` | Tailwind v4 CSS-first config |
| `angular.json` | CLI schematics (OnPush, SCSS), build budgets |
| `eslint.config.js` | Flat ESLint with angular-eslint + prettier |

---

## Project Rules

Detailed rules live in `.claude/rules/` and are auto-loaded each session:

| File | Covers |
|------|--------|
| `angular.md` | Component conventions, reactivity, routing |
| `ngrx.md` | NgRx slice patterns, registration, store usage |
| `styling.md` | Tailwind + Material conventions |
| `testing.md` | Unit and E2E testing requirements |
| `commits.md` | Conventional Commits rules |

---

## Workflow

All development **must** follow the [agent-skills](https://github.com/addyosmani/agent-skills) agentic workflow (installed as a project plugin). Every task flows through these phases in order — do not skip or reorder them.

```
/spec        →  clarify requirements → structured spec (SPEC.md)
/plan        →  dependency graph → ordered tasks (tasks/plan.md + tasks/todo.md)
/build       →  RED → GREEN → REFACTOR → commit (one slice at a time)
/test        →  TDD for new logic; Prove-It pattern for bug fixes
/review      →  five-axis review: correctness, readability, arch, security, perf
/ship        →  parallel fan-out (code-reviewer + security-auditor + test-engineer)
                → GO / NO-GO decision with rollback plan
/code-simplify →  reduce complexity without changing behavior
```

**Mandatory skill-to-task mapping — check before any action:**

| Situation | Required skill / command |
|-----------|--------------------------|
| New feature or unclear requirements | `/spec` first |
| Have a spec, need a task list | `/plan` |
| Writing any implementation code | `/build` (TDD inside) |
| Bug fix or test writing | `/test` (Prove-It) |
| Pre-merge review | `/review` |
| Pre-deploy / PR ready | `/ship` |
| Code feels complex | `/code-simplify` |

The session-start hook injects the `using-agent-skills` meta-skill automatically each session. Use the skill discovery flowchart at the top of that skill to pick the right entry point whenever you're unsure.

> Skills provided by the `agent-skills@addy-agent-skills` plugin. See `.claude/settings.json` for plugin registration.
