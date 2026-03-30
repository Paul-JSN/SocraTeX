---
name: exercise
description: Use when the user wants to practice problems with guided hints, tracking attempts before revealing solutions. Works with any STEM subject
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Parse $ARGUMENTS to locate relevant exercises. Find textbook .md files — check `textbook_path` from config first, then `books/`, then the working directory, or use files provided in the conversation. If $ARGUMENTS is a topic name, find exercises related to that topic. If it is a number, find that specific exercise.

After reading, detect the subject from the content. If `subject` in config is not `auto`, use that instead. Adapt problem style and terminology to the detected subject.

Present the problem with all math/formulas in LaTeX ($...$ inline, $$...$$ block).

Guide the student through solving — do NOT give the answer. Adapt to the subject:
- Physics: ask about diagrams, units, and which laws apply before computing
- Chemistry: ask about balanced equations, limiting reagents before solving
- Math: ask about which theorem or technique to use
- Statistics: ask about assumptions, hypotheses, and what the numbers mean

1. Ask: "What approach would you try first?"
2. After each student response, give feedback and one incremental hint.
3. Track hint count. Do not reveal the full solution until `hints_before_answer` hints have been given AND the student has attempted.
4. After each hint, check: "Does this give you an idea for the next step?"
5. If the student is stuck after all hints, walk through the solution step-by-step, explaining each transition.

When the student says "more" or "similar", generate a new problem of the same type and difficulty.

After presenting each exercise and during solution steps, update `session.md` in the working directory with the current exercise and key formulas. Append, do not overwrite.
