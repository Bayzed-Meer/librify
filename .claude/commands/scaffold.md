---
description: Scaffold Angular artifacts (component, service, store slice, guard, route) using librify project conventions
argument-hint: "component features/books/components/book-card | service features/books/services/books | store books | guard core/guards/auth | route books"
allowed-tools: Bash, Read, Edit, Write, Glob, Grep
---

# Scaffold Angular Artifact

Generate Angular code following librify project conventions from CLAUDE.md.

**Request:** $ARGUMENTS

## Process

### Step 1 — Parse the request

Identify:
- **Artifact type**: component | service | store | guard | route
- **Path**: e.g., `features/books/components/book-card`
- **Name**: e.g., `book-card`

### Step 2 — Generate

#### Component
```bash
ng g c <path>/<name>
```
OnPush change detection and SCSS are applied automatically via schematics defaults in `angular.json`.

After generating, open the component and verify it follows CLAUDE.md conventions:
- Uses `input()` / `output()` not `@Input()` / `@Output()`
- Uses `inject()` not constructor injection
- Uses `@if` / `@for` not structural directives

#### Service
```bash
ng g s <feature>/services/<name>
```
After generating:
- State should be exposed as readonly signals via `.asReadonly()`
- HTTP calls should return Observables (for NgRx effects compatibility)
- Use `inject(HttpClient)` not constructor injection

#### Store Slice (NgRx)
No CLI command — create 5 files manually at `src/app/features/<name>/store/`:

1. `<name>.state.ts` — interface + initialState
2. `<name>.actions.ts` — `createActionGroup` with all events
3. `<name>.reducer.ts` — `createFeature` (auto-generates basic selectors)
4. `<name>.effects.ts` — functional effects with `inject()`
5. `<name>.selectors.ts` — composed/derived selectors only

Follow the exact patterns in CLAUDE.md's "NgRx Patterns" section.
Register providers in the feature route, NOT in `app.config.ts`.

#### Guard
```bash
ng g g core/guards/<name>
```
Generates a functional guard (`CanMatchFn` or `CanActivateFn`). Not class-based.

#### Route (lazy-loaded feature)
1. Create `src/app/features/<name>/<name>.routes.ts` with `Routes` export
2. Add to `src/app/app.routes.ts`:
```typescript
{
  path: '<path>',
  loadChildren: () =>
    import('./features/<name>/<name>.routes').then((m) => m.<NAME>_ROUTES),
}
```
3. If the feature has an NgRx store, add `provideState` + `provideEffects` to the route's `providers` array.

### Step 3 — Verify

Always run:
```bash
ng build
```
Fix any type errors before reporting the task as complete.

### Step 4 — Summary

Report:
- What was generated (file paths)
- Any wiring steps that remain (route registration, provider setup, etc.)
- Build result (pass/fail)
