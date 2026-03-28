---
description: Practice problems with Socratic guidance and incremental hints
---

Read `socratex.config.md` for settings, especially `hints_before_answer` and `difficulty`.

Parse $ARGUMENTS to locate relevant exercises in the textbook .md files under `books/`. If $ARGUMENTS is a topic name, find exercises related to that topic. If it is a number, find that specific exercise.

Present the problem with all math in LaTeX ($...$ inline, $$...$$ block).

Guide the student through solving — do NOT give the answer:
1. Ask: "What approach would you try first?"
2. After each student response, give feedback and one incremental hint.
3. Track hint count. Do not reveal the full solution until `hints_before_answer` hints have been given AND the student has attempted.
4. After each hint, check: "Does this give you an idea for the next step?"
5. If the student is stuck after all hints, walk through the solution step-by-step, explaining each transition.

When the student says "more" or "similar", generate a new problem of the same type and difficulty.

After presenting each exercise and during solution steps, update `session.md` in the book directory with the current exercise and key formulas. Append, do not overwrite.
