---
name: ng-test
description: Generate a Vitest unit test for an Angular component, service, reducer, or selector following librify conventions (zoneless, MockStore, signal APIs).
user-invocable: false
---

Generate a complete Vitest unit test for the file at `{file_path}`.

## Required patterns — always enforce

### Components
- `TestBed.configureTestingModule({ imports: [ComponentUnderTest] })` — standalone components use `imports`, not `declarations`
- `await fixture.whenStable()` — NOT `fixture.detectChanges()` (this is a zoneless app)
- Inject the store with `provideMockStore({ initialState })` when the component uses NgRx
- Use `store.setState(...)` to drive state changes in tests

### Services
- Test every public method
- Test every error path (e.g., HTTP failures, thrown errors)
- Do NOT test private methods

### Reducers
- Test every `on()` handler — one `it` block per action
- Assert the full shape of the returned state slice
- Do NOT test auto-generated selectors from `createFeature`

### Selectors (composed only)
- Test every selector in `selectors.ts`
- Use `projector` from `createSelector` to test the projection function in isolation
- Skip auto-generated selectors (e.g., `selectBooks`, `selectLoading` from `booksFeature`)

### Pipes / utilities
- Test every public method and edge case

## Forbidden patterns
- `fixture.detectChanges()` — use `await fixture.whenStable()` instead
- `@Input()` / `@Output()` decorators in test helpers — use `input()` / `output()` signal APIs
- `*ngIf` / `*ngFor` in test templates — use `@if` / `@for`
- Constructor injection in test setup — use `inject()` or `TestBed.inject()`

## File under test
`{file_path}`
