---
paths:
  - "src/**/*.spec.ts"
  - "e2e/**/*.ts"
---

# Testing Rules

## Unit Tests (Vitest)

**Required for:** every component, every service (all public methods + error paths), every reducer
(`on()` handler), every composed selector, every pipe/utility.

**Do NOT test:** auto-generated selectors from `createFeature`, trivial getters, private internals.

### Patterns
```typescript
// Standalone component
TestBed.configureTestingModule({ imports: [ComponentUnderTest] });
await fixture.whenStable(); // NEVER fixture.detectChanges() — this is a zoneless app

// Component with NgRx store
TestBed.configureTestingModule({
  imports: [ComponentUnderTest],
  providers: [provideMockStore({ initialState })],
});
const store = TestBed.inject<MockStore>(Store);
store.setState({ ... });

// Reducer — one it() per on() handler, assert full returned state shape
// Selector — use projector() to test projection function in isolation
```

## E2E Tests (Playwright)
**Required for:** complete user flows, critical navigation paths, form submission + validation.
**Not required for:** unit-level behavior already covered by Vitest.
