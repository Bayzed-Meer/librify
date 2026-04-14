---
description: Add a lazy-loaded feature route to the app following librify conventions
argument-hint: "path feature-name [with-store]"
allowed-tools: Bash, Read, Edit, Write, Glob
---

# Add Lazy-Loaded Route

Add a new lazy-loaded feature route to the librify app.

**Route:** $ARGUMENTS

## Step 1 — Read current routes

Read `src/app/app.routes.ts` to see existing routes and avoid conflicts.

## Step 2 — Verify or create feature routes file

Check if `src/app/features/<name>/<name>.routes.ts` exists. If not, create it:

```typescript
import { Routes } from '@angular/router';
import { <Name>Component } from './<name>.component';

export const <NAME>_ROUTES: Routes = [
  {
    path: '',
    component: <Name>Component,
  },
];
```

If `with-store` was specified, add `providers` to the route:
```typescript
import { provideState } from '@ngrx/store';
import { provideEffects } from '@ngrx/effects';
import { <name>Feature } from './store/<name>.reducer';
import * as <Name>Effects from './store/<name>.effects';

// Inside the route object:
providers: [provideState(<name>Feature), provideEffects(<Name>Effects)],
```

## Step 3 — Add to app.routes.ts

Add the lazy-loaded route to `src/app/app.routes.ts`:

```typescript
{
  path: '<path>',
  loadChildren: () =>
    import('./features/<name>/<name>.routes').then((m) => m.<NAME>_ROUTES),
},
```

## Step 4 — Build verification

```bash
ng build
```

Fix any type errors before completing.

## Step 5 — Summary

Report:
- Route path added
- Feature routes file created or updated
- Store providers wired (if `with-store`)
- Build result
