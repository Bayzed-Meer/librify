#!/usr/bin/env python3
"""PostToolUse hook: run eslint on the edited file immediately after edits."""
import json
import subprocess
import sys


def main():
    try:
        data = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)

    tool_name = data.get("tool_name", "")
    if tool_name not in ["Edit", "Write", "MultiEdit"]:
        sys.exit(0)

    file_path = data.get("tool_input", {}).get("file_path", "")
    if not file_path or not (file_path.endswith(".ts") or file_path.endswith(".html")):
        sys.exit(0)

    result = subprocess.run(
        ["npx", "eslint", "--max-warnings=0", file_path],
        capture_output=True,
        text=True,
        cwd="/Users/bs01618/personal-projects/librify",
    )
    if result.returncode != 0:
        output = (result.stdout + result.stderr).strip()
        print(f"ESLint issues in {file_path}:\n{output}", file=sys.stderr)

    sys.exit(0)  # PostToolUse hooks must not block — never exit 2


if __name__ == "__main__":
    main()
