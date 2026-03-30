---
name: settings
description: Use when the user wants to view or change SocraTeX settings — language, term annotation, difficulty, hints, render mode
---

If `socratex.config.md` does not exist, create it with defaults (study_language: en, show_original_terms: false, difficulty: adaptive, hints_before_answer: 3, render_mode: desktop) before proceeding. Then read `socratex.config.md`.

If $ARGUMENTS is empty, display all current settings in a clean table format. Stop here.

Otherwise, parse $ARGUMENTS as key=value pairs. Supported keys:
- `lang` → updates `study_language` (ISO 639-1 code: en, ko, ja, zh, es, fr, de, etc.)
- `terms` → updates `show_original_terms` (on/off → true/false)
- `format` → updates `term_format` (quoted string)
- `path` → updates `textbook_path` (directory path to textbook .md files)
- `difficulty` → updates `difficulty` (easy, medium, hard, adaptive)
- `hints` → updates `hints_before_answer` (integer)
- `render` → updates `render_mode` (desktop or vscode)

For each key=value pair, use the Edit tool to modify the corresponding line in `socratex.config.md`. Confirm each change.

After all changes, display the updated settings table.

**Examples:**
- `/settings` → show all settings
- `/settings lang=ko` → change language to Korean
- `/settings lang=ja terms=on` → change language to Japanese, enable term annotation
- `/settings difficulty=hard hints=5` → harder difficulty, 5 hints before answer
- `/settings render=desktop` → output session.html, auto-open in browser (Claude Code Desktop/CLI)
- `/settings render=vscode` → output session.md, view in VS Code Markdown Preview
