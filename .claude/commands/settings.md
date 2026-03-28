---
description: View or modify socratex.config.md settings
---

Read `socratex.config.md`.

If $ARGUMENTS is empty, display all current settings in a clean table format. Stop here.

Otherwise, parse $ARGUMENTS as key=value pairs. Supported keys:
- `lang` → updates `study_language` (ISO 639-1 code: en, ko, ja, zh, es, fr, de, etc.)
- `terms` → updates `show_original_terms` (on/off → true/false)
- `format` → updates `term_format` (quoted string)
- `difficulty` → updates `difficulty` (easy, medium, hard, adaptive)
- `hints` → updates `hints_before_answer` (integer)

For each key=value pair, use the Edit tool to modify the corresponding line in `socratex.config.md`. Confirm each change.

After all changes, display the updated settings table.

**Examples:**
- `/settings` → show all settings
- `/settings lang=ko` → change language to Korean
- `/settings lang=ja terms=on` → change language to Japanese, enable term annotation
- `/settings difficulty=hard hints=5` → harder difficulty, 5 hints before answer
