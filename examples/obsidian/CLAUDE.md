# CLAUDE.md — Obsidian Vault

This file configures Claude Code when working inside this Obsidian vault.

## Vault Structure

Adapt the paths below to match your actual vault layout:

```
vault-root/
├── Notes/          # Atomic and permanent notes
├── Projects/       # Project-specific notes and tasks
├── Dailies/        # Daily notes (YYYY-MM-DD.md)
├── Templates/      # Note templates
├── Attachments/    # Images and other embedded files
└── Archive/        # Retired or old notes
```

## Obsidian Syntax Rules

Always preserve Obsidian-specific formatting when editing notes:

- **Wikilinks**: `[[Note Title]]` or `[[Note Title|display text]]` — never convert to standard Markdown links
- **Embeds**: `![[Note Title]]` or `![[image.png]]` — do not flatten or remove
- **Tags**: inline `#tag` and frontmatter `tags:` — keep both styles intact
- **Callouts**: `> [!NOTE]`, `> [!WARNING]`, `> [!TIP]` — preserve the `[!TYPE]` marker
- **Frontmatter**: YAML block at the top of the file between `---` delimiters

## Frontmatter Convention

When creating new notes, include this frontmatter template:

```yaml
---
title: "Note Title"
date: YYYY-MM-DD
tags: []
aliases: []
---
```

## Working Guidelines

- When asked to create a note, place it in the most appropriate folder and add correct frontmatter.
- When asked to link notes, use `[[Note Title]]` wikilink syntax, not `[text](path.md)`.
- When searching across notes, use `grep` or `find` on `.md` files.
- Do not modify files in `Attachments/` unless explicitly asked.
- Do not rename files without confirming — renames break existing wikilinks.
- When adding tags, keep them lowercase and hyphenated (e.g. `#project-ideas`).

## Daily Notes

Daily notes follow the filename format `YYYY-MM-DD.md` and live in `Dailies/`.
When appending to a daily note, add content at the end of the existing file rather than replacing it.
