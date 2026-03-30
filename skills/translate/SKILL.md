---
name: translate
description: Use when the user wants study content translated to another language while preserving all LaTeX math and term annotation settings
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

If $ARGUMENTS specifies a language (e.g., "ko", "ja", "zh", "es"), use that language for this translation. Otherwise, use `study_language` from config.

Translate the most recent study content (the last topic, exercise, or explanation discussed) into the target language.

**Rules:**
- ALL LaTeX expressions must remain unchanged — do not translate math notation
- Apply `term_format` for technical terms when `show_original_terms` is true
  - Example with `term_format: "translated (original)"` and lang=ko: "수렴 (convergence)"
  - Example with `term_format: "original → translated"` and lang=ja: "convergence → 収束"
- Preserve the structure and formatting of the original content
- Keep theorem/definition labels in their original form (e.g., "Theorem 3.1.1")

Update `session.md` in the working directory with the translated version. Append — do not overwrite the original.
