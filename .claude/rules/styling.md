---
paths:
  - "src/app/**/*.html"
  - "src/app/**/*.scss"
  - "src/styles.scss"
  - "src/tailwind.css"
---

# Styling Rules

## When to Use What
| Scenario | Tool |
|----------|------|
| Material component (button, dialog, table, chip…) | Angular Material only |
| Layout (flex, grid, spacing, padding, margins) | Tailwind utilities |
| Typography (font size, weight, line height) | Tailwind utilities |
| Global Material theme | `styles.scss` via `mat.define-theme()` |
| Component-specific styles not achievable with utilities | Component `.scss` file |

## Rules
- Never mix Tailwind and Material for the same element's primary styling — pick one
- Never replicate Material component behavior with Tailwind
- Never override Material component internals with global CSS
- Tailwind config is CSS-first in `tailwind.css` (v4) — there is no `tailwind.config.js`
- Component style budget: 4kB warning / 8kB error — keep component SCSS minimal
