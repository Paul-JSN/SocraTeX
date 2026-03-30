---
name: mock-test
description: Use when the user wants a practice exam with difficulty distribution, point values, time estimates, and hidden solutions
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Parse $ARGUMENTS as a chapter range. Find textbook .md files — check `textbook_path` from config first, then `books/`, then the working directory, or use files provided in the conversation. Read all exercises and theorems in that range.

Generate a mock exam:

**Structure:**
- Difficulty distribution: 30% easy, 50% medium, 20% hard
- Mix of: definitions, proofs/derivations, computations, and conceptual questions
- Match the textbook's exercise style and notation

**For each question:**
- Number and point value
- Full problem statement in LaTeX
- Estimated time (in minutes)

**At the end:**
- Total points and recommended time
- Topic coverage summary

**Solutions:** Do NOT show solutions initially. When the student says "solutions", "answers", or "show solutions", then reveal step-by-step solutions for each question.

Write the mock test to `session.md` in the working directory (overwrite for clean test format).
