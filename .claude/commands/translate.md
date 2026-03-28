---
description: Translate current study content while preserving LaTeX notation
---

Read `socratex.config.md` for `study_language`, `show_original_terms`, and `term_format`.

If $ARGUMENTS specifies a language (e.g., "ko", "ja", "zh", "es"), use that language for this translation. Otherwise, use `study_language` from config.

Translate the most recent study content (the last topic, exercise, or explanation discussed) into the target language.

**Rules:**
- ALL LaTeX expressions must remain unchanged — do not translate math notation
- Apply `term_format` for mathematical terms when `show_original_terms` is true
  - Example with `term_format: "translated (original)"` and lang=ko: "수렴 (convergence)"
  - Example with `term_format: "original → translated"` and lang=ja: "convergence → 収束"
- Preserve the structure and formatting of the original content
- Keep theorem/definition labels in their original form (e.g., "Theorem 3.1.1")

Update `session.md` with the translated version. Append — do not overwrite the original.
