---
name: study
description: Use when the user wants to study a math textbook chapter or section using Socratic dialogue with LaTeX-rendered definitions and theorems
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop. Apply these throughout.

If $ARGUMENTS is empty, look for available textbook .md files and list chapters/sections found. Stop here.

Otherwise, parse $ARGUMENTS to identify the target chapter/section. Find textbook .md files — check `textbook_path` from config first, then `books/`, then the working directory, or use files provided in the conversation. Read the relevant file.

Present the material using strict Socratic method (see CLAUDE.md):
1. State the key definition or theorem in full LaTeX ($...$ inline, $$...$$ block).
2. Ask: "What do you think this means intuitively?" — wait for the student's response.
3. Based on their answer, ask guiding follow-up questions. Do NOT explain directly.
4. Use examples and counterexamples to probe understanding.
5. Confirm understanding before moving to the next concept.
6. Repeat for each concept in the section.

Apply `show_original_terms` and `term_format` from config when rendering mathematical terminology.

After each concept block, append the topic heading and key formulas to `session.md` in the working directory. Do not overwrite existing content — append incrementally.
