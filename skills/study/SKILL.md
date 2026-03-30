---
name: study
description: Use when the user wants to study a textbook chapter or section using Socratic dialogue with LaTeX-rendered definitions and theorems. Works with any STEM subject — math, physics, chemistry, statistics, engineering, economics
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto. Apply these throughout.

If $ARGUMENTS is empty, look for available textbook .md files and list chapters/sections found. Stop here.

Otherwise, parse $ARGUMENTS to identify the target chapter/section. Find textbook .md files — check `textbook_path` from config first, then `books/`, then the working directory, or use files provided in the conversation. Read the relevant file.

After reading, detect the subject from the content (terminology, notation, topic structure). If `subject` in config is not `auto`, use that instead. Adapt language, examples, and proof/derivation styles to the detected subject (see CLAUDE.md Subject Detection).

Present the material using strict Socratic method (see CLAUDE.md), adapting to the subject's nature:
1. State the key definition, theorem, or law in full LaTeX ($...$ inline, $$...$$ block).
   - Physics: include units and physical meaning. "What does this tell us about the system?"
   - Chemistry: connect to molecular behavior. "What's happening at the particle level?"
   - Math: emphasize rigor and conditions. "When does this hold? When doesn't it?"
   - Statistics: ground in data. "What would this look like with real data?"
2. Ask: "What do you think this means intuitively?" — wait for the student's response.
3. Based on their answer, ask guiding follow-up questions. Do NOT explain directly.
4. Use examples and counterexamples to probe understanding.
5. Confirm understanding before moving to the next concept.
6. Repeat for each concept in the section.

Apply `show_original_terms` and `term_format` from config when rendering technical terminology.

After each concept block, append the topic heading and key formulas to `session.md` in the working directory. Do not overwrite existing content — append incrementally.
