# obsidian

Claude Code plugin for working inside an [Obsidian](https://obsidian.md) vault.

## Features

### Commands

| Command | Description |
|---------|-------------|
| `/new-note [title]` | Create a new Markdown note with correct frontmatter in the right vault folder |
| `/daily [content]` | Create or append to today's daily note (`YYYY-MM-DD.md`) |
| `/find-broken-links [folder]` | Scan the vault for `[[wikilinks]]` that point to missing notes |

### Hook — Wikilink Guard

A `PreToolUse` hook intercepts `Bash` commands and warns Claude before it runs `mv` or `rm` on `.md` files. Renaming or deleting a note breaks every `[[wikilink]]` pointing to it across the vault. The hook exits with code `1` (warn, allow) so Claude can reconsider or ask the user first.

### Skill — Obsidian Syntax

An auto-applied skill that injects Obsidian formatting rules into Claude's context whenever it works in a vault:

- Always use `[[wikilink]]` syntax — never convert to standard Markdown links
- Preserve `![[embed]]`, callouts (`> [!NOTE]`), inline tags, and frontmatter
- Confirm with the user before renaming or deleting any `.md` file

## Installation

Copy the plugin to your Claude Code plugins directory or register it in your project's `.claude/settings.json`:

```json
{
  "plugins": ["path/to/plugins/obsidian"]
}
```

Then copy `examples/obsidian/CLAUDE.md` and `examples/obsidian/.claude/settings.json` into your vault root for the best experience.

## Vault Structure (recommended)

```
vault-root/
├── Notes/
├── Projects/
├── Dailies/
├── Templates/
├── Attachments/
└── Archive/
```

Adjust the folder names in `CLAUDE.md` to match your actual layout.
