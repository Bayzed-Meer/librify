---
description: Generate a complete NgRx store slice (state, actions, reducer, effects, selectors) following librify conventions
argument-hint: "feature-name [optional: field1:type,field2:type]"
allowed-tools: Bash, Read, Write, Glob, Grep
---

# Generate NgRx Store Slice

Create a complete NgRx feature store following librify's Redux patterns.

**Feature:** $ARGUMENTS

## Step 1 — Read CLAUDE.md

Read `/Users/bs01618/personal-projects/librify/CLAUDE.md` and locate the "NgRx Patterns" section. All generated code must follow those exact patterns.

## Step 2 — Parse the feature name and fields

From `$ARGUMENTS`:
- Feature name (e.g., `books` → files named `books.state.ts`, etc.)
- Optional field definitions to populate the state interface

## Step 3 — Generate all 5 files

Create at `src/app/features/<name>/store/`:

### `<name>.state.ts`
```typescript
export interface <Name>State {
  items: <Model>[];
  selectedId: string | null;
  loading: boolean;
  error: string | null;
}

export const initial<Name>State: <Name>State = {
  items: [],
  selectedId: null,
  loading: false,
  error: null,
};
```

### `<name>.actions.ts`
Use `createActionGroup` — never individual `createAction()`:
```typescript
import { createActionGroup, emptyProps, props } from '@ngrx/store';

export const <Name>Actions = createActionGroup({
  source: '<Name>',
  events: {
    'Load <Name>s': emptyProps(),
    'Load <Name>s Success': props<{ items: <Model>[] }>(),
    'Load <Name>s Failure': props<{ error: string }>(),
    'Select <Name>': props<{ id: string }>(),
  },
});
```

### `<name>.reducer.ts`
Use `createFeature` to auto-generate basic selectors:
```typescript
import { createFeature, createReducer, on } from '@ngrx/store';
import { <Name>Actions } from './<name>.actions';
import { initial<Name>State } from './<name>.state';

export const <name>Feature = createFeature({
  name: '<name>',
  reducer: createReducer(
    initial<Name>State,
    on(<Name>Actions.load<Name>s, (state) => ({ ...state, loading: true, error: null })),
    on(<Name>Actions.load<Name>sSuccess, (state, { items }) => ({ ...state, items, loading: false })),
    on(<Name>Actions.load<Name>sFailure, (state, { error }) => ({ ...state, error, loading: false })),
    on(<Name>Actions.select<Name>, (state, { id }) => ({ ...state, selectedId: id })),
  ),
});

export const { select<Name>State, selectItems, selectSelectedId, selectLoading, selectError } =
  <name>Feature;
```

### `<name>.effects.ts`
Functional effects — no class, no constructor:
```typescript
import { inject } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { catchError, map, switchMap } from 'rxjs/operators';
import { of } from 'rxjs';
import { <Name>Actions } from './<name>.actions';
import { <Name>Service } from '../services/<name>.service';

export const load<Name>s$ = createEffect(
  (actions$ = inject(Actions), <name>Service = inject(<Name>Service)) => {
    return actions$.pipe(
      ofType(<Name>Actions.load<Name>s),
      switchMap(() =>
        <name>Service.getAll().pipe(
          map((items) => <Name>Actions.load<Name>sSuccess({ items })),
          catchError((error: unknown) =>
            of(<Name>Actions.load<Name>sFailure({ error: String(error) })),
          ),
        ),
      ),
    );
  },
  { functional: true },
);
```

### `<name>.selectors.ts`
Only composed/derived selectors — basic ones already come from `createFeature`:
```typescript
import { createSelector } from '@ngrx/store';
import { <name>Feature } from './<name>.reducer';

export const selectSelected<Name> = createSelector(
  <name>Feature.selectItems,
  <name>Feature.selectSelectedId,
  (items, id) => items.find((item) => item.id === id) ?? null,
);
```

## Step 4 — Show route wiring

Print the exact code needed to register the store in the feature route:
```typescript
// In <name>.routes.ts providers array:
provideState(<name>Feature),
provideEffects(<Name>Effects),
```

Remind: register here, NOT in `app.config.ts`.

## Step 5 — Build verification

```bash
ng build
```

Report the build result. Fix any type errors before completing.

## Step 6 — Summary

Report:
- All 5 files created (with paths)
- Route wiring instructions
- Build result
