---
name: study-guide
description: Use when the user needs a structured overview of chapters — concept hierarchy, summaries, formula sheet, study order, and time estimates
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop.

Parse $ARGUMENTS as a chapter range. Find textbook .md files — check `textbook_path` from config first, then `books/`, then the working directory, or use files provided in the conversation. Read all .md files in that range.

Generate a structured study guide:

**1. Big Picture**
2-3 sentences: what this range covers and why it matters.

**2. Concept Hierarchy**
Outline format showing how topics build on each other. Indent sub-topics.

**3. Section Summaries**
One-line summary per section. Focus on the key takeaway.

**4. Formula Sheet**
All critical formulas in LaTeX $$...$$ blocks. Organized by topic. Designed to be printed/copied.

**5. Recommended Study Order**
Optimal sequence if topics have prerequisites. Flag which sections are most exam-relevant.

**6. Estimated Study Time**
Per-section time estimates based on concept density and difficulty.

Write the complete guide to `session.md` in the working directory (overwrite). Apply language/term settings.
