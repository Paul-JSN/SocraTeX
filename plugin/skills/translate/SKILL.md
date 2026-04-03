---
name: translate
description: Use when the user wants study content translated to another language while preserving all LaTeX math and term annotation settings
---

Read `SocraTeX.config.md` from the working directory. If not found, read `${CLAUDE_PLUGIN_ROOT}/SocraTeX.config.md`. If neither exists, use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/core-rules.md` for Socratic method, LaTeX, subject detection, and session file rendering rules. Apply these throughout.

If $ARGUMENTS specifies a language (e.g., "ko", "ja", "zh", "es"), use that language for this translation. Otherwise, use `study_language` from config.

Translate the most recent study content (the last topic, exercise, or explanation discussed) into the target language.

**Rules:**
- ALL LaTeX expressions must remain unchanged — do not translate math notation
- Apply `term_format` for technical terms when `show_original_terms` is true
  - Example with `term_format: "translated (original)"` and lang=ko: "수렴 (convergence)"
  - Example with `term_format: "original → translated"` and lang=ja: "convergence → 収束"
- Preserve the structure and formatting of the original content
- Keep theorem/definition labels in their original form (e.g., "Theorem 3.1.1")

Write the translated version to the session file (per `render_mode` in config). Overwrite — this is a full-document skill.

## Anti-Patterns

### Translating LaTeX
Never translate math notation. $\int_0^1 x^2\,dx$ is universal. Only translate the surrounding text.

### Inconsistent Terminology
Pick one translation for each technical term and use it consistently throughout. Don't translate "convergence" as three different words in the same document.

### Losing Structure
The translated version must preserve headings, bullet points, numbering, and theorem labels from the original. Translation is about language, not reformatting.
