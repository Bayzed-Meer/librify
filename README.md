# Librify

A library management web application built with Angular 21, NgRx, Angular Material M3, and Tailwind CSS v4.

## Quick Start

```bash
npm install
npm start          # http://localhost:4200
```

## Development

```bash
npm start          # dev server with HMR
npm test           # Vitest unit tests (watch mode)
npm run build      # production build
npm run lint       # ESLint
npm run format     # Prettier
npm run e2e        # Playwright E2E tests
npm run e2e:ui     # Playwright visual mode
```

## Agent-Driven Workflow

This project uses Claude Code for AI-assisted development. See [`docs/WORKFLOW.md`](docs/WORKFLOW.md) for the full pipeline.

```
/spec <name>       →  spec interview → docs/specs/<name>.spec.md
/feature-dev       →  implement + test
/review-pr         →  multi-agent code review
/commit            →  conventional commit
/create-pr         →  push + open PR
```

All conventions and rules are in [`CLAUDE.md`](CLAUDE.md).

## Stack

| Layer | Technology |
|-------|-----------|
| Framework | Angular 21 (standalone, OnPush, signals) |
| State | NgRx 21 (store, effects, devtools) |
| UI | Angular Material 21 (M3) + Tailwind CSS v4 |
| Testing | Vitest (unit) + Playwright (E2E) |
| Language | TypeScript 5.9 (strict) |
| Linting | angular-eslint + Prettier |
| Commits | Conventional Commits via CommitLint |

## Project Structure

```
src/app/
  features/<name>/       # feature module
    <name>.routes.ts     # lazy-load config + store providers
    <name>.component.ts  # smart/container component
    components/          # presentational children
    store/               # NgRx slice (state, actions, reducer, effects, selectors)
    services/
  core/                  # guards, interceptors, global services
  shared/                # reusable components, pipes, utils
```
