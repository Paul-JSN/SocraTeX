---
name: settings
description: Use when the user wants to view or change SocraTeX settings — language, term annotation, difficulty, hints, render mode, subject
---

If `socratex.config.md` does not exist in the working directory, create it with defaults (copy from `${CLAUDE_PLUGIN_ROOT}/socratex.config.md` if available, otherwise create with defaults: study_language: en, show_original_terms: false, difficulty: adaptive, hints_before_answer: 3, render_mode: desktop, subject: auto) before proceeding. Then read `socratex.config.md`.

Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/core-rules.md` for Socratic method, LaTeX, subject detection, and session file rendering rules. Apply these throughout.

If $ARGUMENTS is empty, display all current settings in a clean table format. Stop here.

Otherwise, parse $ARGUMENTS as key=value pairs. Supported keys:
- `lang` → updates `study_language` (ISO 639-1 code: en, ko, ja, zh, es, fr, de, etc.)
- `terms` → updates `show_original_terms` (on/off → true/false)
- `format` → updates `term_format` (quoted string)
- `path` → updates `textbook_path` (directory path to textbook .md files)
- `difficulty` → updates `difficulty` (easy, medium, hard, adaptive)
- `hints` → updates `hints_before_answer` (integer)
- `render` → updates `render_mode` (desktop or vscode)
- `subject` → updates `subject` (auto, math, physics, chemistry, statistics, economics, engineering)

For each key=value pair, use the Edit tool to modify the corresponding line in `socratex.config.md`. Confirm each change.

After all changes, display the updated settings table.

**Examples:**
- `/settings` → show all settings
- `/settings lang=ko` → change language to Korean
- `/settings lang=ja terms=on` → change language to Japanese, enable term annotation
- `/settings difficulty=hard hints=5` → harder difficulty, 5 hints before answer
- `/settings render=desktop` → output session.html, auto-open in browser (Claude Code Desktop/CLI)
- `/settings render=vscode` → output session.md, view in VS Code Markdown Preview
- `/settings subject=physics` → set subject to physics (overrides auto-detection)
- `/settings subject=auto` → reset to auto-detection

## Anti-Patterns

### Not Confirming Changes
Always show the before and after values. "Changed `study_language` from `en` to `ko`" — not just "Settings updated."

### Silently Ignoring Invalid Values
If the user sets `difficulty=extreme` or `hints=-1`, reject it with a clear message listing valid values. Don't silently accept invalid input.
