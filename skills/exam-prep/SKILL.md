---
name: exam-prep
description: Use when the user needs comprehensive exam preparation materials for a chapter range — formulas, theorems, exercises, proof strategies, common mistakes
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Parse $ARGUMENTS as a chapter/section range (e.g., "ch1-ch5", "chapters 1 to 3", "sections 3.1-3.4"). Find textbook .md files — check `textbook_path` from config first, then `books/`, then the working directory, or use files provided in the conversation. Read all .md files in that range.

After reading, detect the subject from the content. If `subject` in config is not `auto`, use that instead. Adapt categories to the detected subject (e.g., for physics: include unit analysis and dimensional checks; for chemistry: include reaction mechanisms).

Generate these 6 categories, ALL with LaTeX:

**1. Formula Cheat Sheet**
Extract every important formula, equation, and identity. Organize by topic. Use $$...$$ blocks.

**2. Theorem Summary**
Each theorem with: statement, proof sketch (2-3 lines), and when to use it.

**3. Must-Do Exercises**
List exercises that cover core concepts. Prioritize those testing key theorems. Include exercise numbers and brief descriptions.

**4. Proof Strategies**
Common proof/derivation patterns in this range. Show the template structure. Adapt to subject: math (epsilon-delta, induction), physics (conservation laws, free-body diagrams), chemistry (stoichiometry, equilibrium), etc.

**5. Common Mistakes**
Pitfalls students frequently hit. "Do NOT confuse X with Y" format.

**6. Concept Map**
Text-based relationship diagram: definitions → theorems → applications → connections.

Write the complete output to `session.md` in the working directory (overwrite — this is a reference document, not incremental). Apply language/term settings throughout.
