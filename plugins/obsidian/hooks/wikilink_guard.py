#!/usr/bin/env python3
"""
Obsidian wikilink guard hook.

Warns Claude before it runs mv or rm on .md files inside the vault,
because renaming or deleting a note breaks all [[wikilinks]] pointing to it.
Exit code 1 = warn but allow. Exit code 2 = block.
"""

import json
import re
import sys

DANGEROUS_PATTERNS = [
    (r"\bmv\b.*\.md", "Renaming a Markdown file breaks all [[wikilinks]] that reference it. Update wikilinks across the vault first, or ask the user before proceeding."),
    (r"\brm\b.*\.md", "Deleting a Markdown file permanently removes it and breaks all [[wikilinks]] pointing to it. Confirm with the user before deleting vault notes."),
]


def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)

    if data.get("tool_name") != "Bash":
        sys.exit(0)

    command = data.get("tool_input", {}).get("command", "")

    for pattern, message in DANGEROUS_PATTERNS:
        if re.search(pattern, command):
            print(f"[obsidian-guard] {message}", file=sys.stderr)
            sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
