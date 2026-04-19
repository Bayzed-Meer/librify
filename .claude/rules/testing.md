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

### E2E coverage requirements
- At least one test per acceptance criterion marked as a user-facing flow
- Cover the happy path, the primary empty state, and the primary error state
- Use `page.getByRole()` and `page.getByTestId()` — never CSS selectors

---

## Mandatory Agent Workflow (Step 3 — after writing code)

After writing implementation code, agents MUST follow this sequence before committing:

### 1. Write unit tests alongside implementation
Write Vitest tests for every new service, reducer `on()` handler, composed selector, and component with logic. Do not defer — write them immediately after each file.

### 2. Run unit tests and fix failures
```bash
npm test -- --watch=false
```
If any test fails: read the failure output, fix the source or test, and re-run until all pass.

### 3. Write E2E tests
Write Playwright tests covering the primary acceptance criteria flows.

### 4. Start the dev server and run E2E tests locally
```bash
# Terminal 1 (background)
npm start &

# Wait for server, then run E2E
npx playwright test --project=chromium
```
If any E2E test fails: read the Playwright error and trace output, fix the implementation or test, and re-run until all pass. Do NOT commit with failing E2E tests.

### 5. Stop the dev server, then commit
Only commit after both `npm test` and `npx playwright test` pass locally.
