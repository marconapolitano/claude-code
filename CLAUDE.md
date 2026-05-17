# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

This is the **official Claude Code public repository** — a documentation, examples, and plugins repo. It does **not** contain the Claude Code CLI source code itself. Instead it houses:

- **`plugins/`** — Official Claude Code plugins (commands, agents, skills, hooks)
- **`examples/`** — Reference implementations for hooks, settings, and MDM deployment
- **`scripts/`** — GitHub issue automation scripts (TypeScript, runs on Bun)
- **`.claude/commands/`** — Repository-specific slash commands for Claude Code
- **`.github/workflows/`** — GitHub Actions that use `claude-code-action@v1` for automated issue triage and deduplication

There is no build system, test suite, or package.json at the root. Changes here are primarily Markdown, JSON, shell scripts, Python, and TypeScript.

## Running the GitHub Automation Scripts

Scripts in `scripts/` are TypeScript and require [Bun](https://bun.sh/):

```bash
# Run a script (requires GITHUB_TOKEN env var)
GITHUB_TOKEN=... bun run scripts/sweep.ts --dry-run
GITHUB_TOKEN=... bun run scripts/auto-close-duplicates.ts
```

Shell scripts (`scripts/gh.sh`, `scripts/edit-issue-labels.sh`, `scripts/comment-on-duplicates.sh`) are thin wrappers around the `gh` CLI and are invoked by the GitHub Actions workflows via `CLAUDE_CODE_SCRIPT_CAPS` allowlists — they are not meant to be called directly in normal development.

## Plugin Architecture

Each plugin lives under `plugins/<name>/` and follows this structure:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json          # Required manifest (name, version, description, author)
├── commands/                # Slash commands — Markdown files with YAML frontmatter
├── agents/                  # Sub-agent definitions — Markdown prompt files
├── skills/                  # Skills (auto-triggered by keyword phrases) — Markdown
├── hooks/                   # Hook scripts + hooks.json wiring
│   └── hooks.json           # Declares which hook events call which scripts
├── .mcp.json                # MCP server configuration (optional)
└── README.md
```

**The `${CLAUDE_PLUGIN_ROOT}` environment variable** is injected at runtime and points to the installed plugin's root directory. Always use it in `hooks.json` command paths instead of hardcoding paths.

### Hook Exit Codes

Hook scripts receive JSON on stdin and communicate via exit codes:

- `0` — Allow the operation to proceed (no output shown)
- `1` — Show stderr to the user as a warning, but still proceed
- `2` — Block the tool call and show stderr to Claude as context

### Skills vs Commands vs Agents

- **Commands** (`commands/*.md`) — User-invoked via `/command-name`; YAML frontmatter sets `allowed-tools` and `description`
- **Agents** (`agents/*.md`) — Sub-agents spawned by commands; isolated context windows
- **Skills** (`skills/*.md`) — Auto-triggered by keyword phrases in the system prompt; not user-invoked

## Repository-Specific Slash Commands

The `.claude/commands/` directory contains commands available in this repo:

- `/commit-push-pr` — Stages, commits, pushes, and opens a PR in one step
- `/dedupe <repo>/issues/<number>` — Finds duplicate GitHub issues using 5 parallel search agents
- `/triage-issue REPO: <r> ISSUE_NUMBER: <n> EVENT: <e>` — Applies lifecycle labels to an issue

These commands use `./scripts/gh.sh` as a controlled `gh` CLI wrapper (not direct `gh` or MCP tools).

## GitHub Automation Architecture

The repo uses `claude-code-action@v1` in three main workflows:

| Workflow | Trigger | Model | Purpose |
|---|---|---|---|
| `claude.yml` | `@claude` mentions | `claude-sonnet-4-5` | General PR/issue assistance |
| `claude-issue-triage.yml` | New issues, comments | `claude-opus-4-6` | Applies labels via `/triage-issue` |
| `claude-dedupe-issues.yml` | New issues | `claude-sonnet-4-5` | Finds duplicates via `/dedupe` |

Issue lifecycle (stale → autoclose) is defined in `scripts/issue-lifecycle.ts` as a single source of truth. Labels and their timeout days are consumed by both `sweep.ts` (marks stale) and `lifecycle-comment.ts` (posts nudge comments).

## Adding a New Plugin

1. Create `plugins/<name>/` with the structure above
2. Add `plugin.json` in `.claude-plugin/`
3. Register it in `.claude-plugin/marketplace.json` under the `plugins` array
4. Add a row to the table in `plugins/README.md`

When writing `hooks.json`, always use `${CLAUDE_PLUGIN_ROOT}` in command paths. For Python hooks, add `CLAUDE_PLUGIN_ROOT`'s parent to `sys.path` to enable package-relative imports (see `plugins/hookify/hooks/pretooluse.py` for the pattern).
