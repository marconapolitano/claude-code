---
description: Create or append content to today's Obsidian daily note
argument-hint: "Optional content to append to today's note"
allowed-tools: ["Read", "Write", "Edit", "Bash"]
---

# Daily Note

Manage today's Obsidian daily note.

## Step 1 — Resolve today's date

```bash
date +%Y-%m-%d
```

## Step 2 — Locate the Dailies folder

Check for common daily note folder names:
```bash
find . -maxdepth 2 -type d \( -name "Dailies" -o -name "Daily" -o -name "Journal" -o -name "Daily Notes" \) | head -5
```

If none found, use the vault root.

## Step 3 — Create or append

**File path**: `{Dailies folder}/{YYYY-MM-DD}.md`

- If the file **does not exist**: create it with this frontmatter and a `## {YYYY-MM-DD}` heading:

```yaml
---
title: "{YYYY-MM-DD}"
date: {YYYY-MM-DD}
tags: [daily]
---
```

- If the file **already exists**: append content at the end of the file — never replace existing content.

## Step 4 — Handle arguments

If `$ARGUMENTS` is provided, append it as a new bullet point under a `### Notes` section (create the section if it doesn't exist).

Confirm the action and show the user the file path.
