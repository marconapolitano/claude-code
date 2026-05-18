---
description: Find broken wikilinks across the Obsidian vault
argument-hint: Optional subfolder to limit the search
allowed-tools: ["Bash", "Read"]
---

# Find Broken Wikilinks

Scan the vault for `[[wikilinks]]` that point to notes that do not exist.

## Step 1 — Collect all note titles

```bash
find . -name "*.md" | sed 's|.*/||; s|\.md$||' | sort > /tmp/obsidian_titles.txt
```

## Step 2 — Extract all wikilinks

```bash
grep -roh '\[\[[^\]]*\]\]' ${ARGUMENTS:-.} --include="*.md" \
  | sed 's/.*:\[\[//; s/\]\].*//' \
  | sed 's/|.*//' \
  | sort -u > /tmp/obsidian_links.txt
```

## Step 3 — Find missing targets

```bash
comm -23 /tmp/obsidian_links.txt /tmp/obsidian_titles.txt
```

## Step 4 — Report

Show the user:
- How many unique wikilinks were scanned
- Which links have no matching note file (broken links)
- For each broken link, show which files reference it:
  ```bash
  grep -rl "\[\[{broken link}" . --include="*.md"
  ```

If no broken links are found, say so clearly. Do not suggest fixes unless the user asks.
