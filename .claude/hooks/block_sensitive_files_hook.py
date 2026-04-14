#!/usr/bin/env python3
"""PreToolUse hook: block edits to package-lock.json and .env files."""
import json
import os
import sys


BLOCKED_PATTERNS = [
    "package-lock.json",
    "yarn.lock",
    "pnpm-lock.yaml",
    "bun.lockb",
]

BLOCKED_PREFIXES = (".env",)


def is_blocked(file_path: str) -> bool:
    basename = os.path.basename(file_path)
    if basename in BLOCKED_PATTERNS:
        return True
    if any(basename.startswith(prefix) for prefix in BLOCKED_PREFIXES):
        return True
    return False


def main():
    try:
        data = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)

    file_path = data.get("tool_input", {}).get("file_path", "")
    if not file_path:
        sys.exit(0)

    if is_blocked(file_path):
        print(
            f"Blocked: direct edits to '{os.path.basename(file_path)}' are not allowed. "
            "Lock files are managed by the package manager; .env files must be edited manually.",
            file=sys.stderr,
        )
        sys.exit(2)  # Exit 2 blocks the tool call

    sys.exit(0)


if __name__ == "__main__":
    main()
