---
description: Create a new Obsidian note with frontmatter in the correct vault folder
argument-hint: "Note title (e.g. My New Idea)"
allowed-tools: ["Read", "Write", "Bash", "AskUserQuestion"]
---

# Create New Obsidian Note

Your task is to create a new Markdown note for an Obsidian vault.

## Step 1 — Determine the title

If `$ARGUMENTS` is provided, use it as the note title.
Otherwise ask the user: "What is the title of the new note?"

## Step 2 — Determine the target folder

List the top-level folders in the current directory:
```bash
find . -maxdepth 1 -type d | sort
```

Ask the user which folder should contain the note. Common choices: `Notes/`, `Projects/`, `Archive/`. If unsure, use `Notes/`.

## Step 3 — Create the file

- Filename: `{folder}/{Title}.md` — use the exact title as the filename (spaces are fine in Obsidian).
- Include this frontmatter at the top:

```yaml
---
title: "{Title}"
date: {YYYY-MM-DD}
tags: []
aliases: []
---
```

Get today's date with: `date +%Y-%m-%d`

Leave one blank line after the closing `---`, then add a `## {Title}` heading.

## Step 4 — Confirm

Tell the user the full path of the created note and remind them that they can link to it from other notes using `[[{Title}]]`.
