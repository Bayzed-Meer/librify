#!/usr/bin/env python3
"""PostToolUse hook: run prettier on the edited file immediately after edits."""
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
    if not file_path or not any(
        file_path.endswith(ext) for ext in (".ts", ".html", ".scss", ".json")
    ):
        sys.exit(0)

    subprocess.run(
        ["npx", "prettier", "--write", file_path],
        capture_output=True,
        text=True,
        cwd="/Users/bs01618/personal-projects/librify",
    )

    sys.exit(0)  # PostToolUse hooks must not block — never exit 2


if __name__ == "__main__":
    main()
