---
paths:
  - "src/app/**/*.ts"
  - "src/app/**/*.html"
---

# Angular Rules

## Components
- All components are **standalone** — never use NgModules
- Selector prefix: `app-` (kebab-case for components, camelCase for directives)
- OnPush change detection and SCSS enforced via schematics defaults
- Use `input()` / `output()` signal APIs — never `@Input()` / `@Output()` decorators
- Use `inject()` for DI — never constructor injection
- Use `@if`, `@for`, `@switch` control flow — never `*ngIf`, `*ngFor`, `*ngSwitch`
- Use `signal()` for internal mutable state; expose readonly via `.asReadonly()` from services

## Reactivity
- Prefer signals over Observables for local component state and derived values
- Use `computed()` for values derived from signals — no explicit subscriptions
- Use `resource()` / `rxResource()` for async data fetching into signal state (Angular 21)
- Use `effect()` only for side effects (DOM, third-party libs) — not state derivation
- Use `linkedSignal()` for writable state that resets when a source signal changes
- Always read signals before `await` boundaries in async reactive contexts

## Routing
- Feature routes lazy-loaded via `loadChildren` — not `loadComponent` for feature roots
- Guards are functional (`CanMatchFn`, `CanActivateFn`) — not class-based
- Resolvers use `ResolveFn` — not class-based
- Route params accessed via `inject(ActivatedRoute).snapshot` or signal inputs
