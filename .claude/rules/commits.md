# Commit Rules

- Must follow Conventional Commits: `feat:`, `fix:`, `refactor:`, `test:`, `chore:`, `docs:`, `style:`
- Scope is encouraged: `feat(books): add book search`
- Never use `--no-verify` to skip the pre-commit hook
- Pre-commit runs lint-staged (Prettier + ESLint) and CommitLint automatically
- Never include `Co-Authored-By` trailers in commit messages
