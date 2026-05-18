# Obsidian Syntax Skill

When working inside an Obsidian vault (any directory containing `.md` files with YAML frontmatter or `[[wikilinks]]`), always apply these rules:

## Wikilinks

- Internal links MUST use `[[Note Title]]` syntax — never convert them to `[text](path.md)`.
- Link with alias: `[[Note Title|display text]]`.
- Embedded notes: `![[Note Title]]`. Embedded images: `![[image.png]]`.

## Frontmatter

Every note starts with a YAML block:
```yaml
---
title: "..."
date: YYYY-MM-DD
tags: []
aliases: []
---
```
Preserve all existing frontmatter keys — do not remove unknown fields.

## Callouts

Obsidian callouts use the `[!TYPE]` marker:
```
> [!NOTE] Optional title
> Content here
```
Supported types: `NOTE`, `TIP`, `WARNING`, `DANGER`, `INFO`, `SUCCESS`, `QUESTION`, `QUOTE`. Never convert callouts to plain blockquotes.

## Tags

- Inline tags: `#tag-name` (lowercase, hyphens).
- Frontmatter tags: `tags: [tag-one, tag-two]`.
- Do not convert one form to the other without being asked.

## File Safety

- Never rename a `.md` file without confirming with the user — it breaks wikilinks.
- Never delete a `.md` file without confirming — data loss is irreversible.
- Do not write to files in `Attachments/` or equivalent folders unless explicitly asked.
