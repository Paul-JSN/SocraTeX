---
name: solve
description: Use when the user wants to see a complete worked solution — Claude demonstrates the full solving process step by step. Unlike /exercise (student solves), here Claude shows how. Works with any STEM subject
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Parse $ARGUMENTS to identify the problem. This can be:
- An exercise number from the textbook
- A problem pasted directly
- A topic (e.g., "integration by parts example", "projectile motion problem")

Find relevant textbook content if available. Detect the subject. Adapt the solution style to the subject's conventions.

Present the problem statement clearly in LaTeX.

Then solve it step by step, showing the full thought process:

**For each step:**
1. State what you're about to do and WHY (not just the mechanics, but the reasoning)
2. Show the math/work in LaTeX
3. Briefly explain the transition to the next step

**Subject-specific solution style:**
- Math: rigorous steps, cite theorems used, check conditions
- Physics: draw a diagram first (ASCII), identify knowns/unknowns, state which law/principle applies, check units at the end
- Chemistry: write the balanced equation first, identify limiting reagents, track units
- Statistics: state hypotheses, check assumptions, compute, interpret in context

**After the solution:**
1. Box the final answer: $$\boxed{answer}$$
2. Sanity check: "Does this make sense?" (magnitude, units, boundary behavior)
3. Alternative approaches: briefly mention if there's another way to solve it
4. Ask: "Would you like a similar problem to try yourself? Run `/exercise [topic]`"

Write the solution to `session.md` in the working directory. Append, do not overwrite.
