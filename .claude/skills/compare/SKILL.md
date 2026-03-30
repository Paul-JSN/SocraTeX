---
name: compare
description: Use when the user wants to compare two mathematical concepts side by side — definitions, differences, counterexamples, when to use which
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop.

Parse $ARGUMENTS to identify the two concepts to compare (e.g., "uniform vs pointwise convergence", "open vs closed sets", "Riemann vs Lebesgue integral").

Generate a structured comparison:

**1. Definitions Side by Side**
Both definitions in LaTeX, formatted for easy visual comparison.

**2. Key Differences**
Bullet list of precise differences. Use math notation where helpful.

**3. Similarities**
What they share — common properties, cases where they coincide.

**4. Counterexamples**
The critical ones: cases where one holds but not the other. Full LaTeX with explanation.

**5. When to Use Which**
Practical guidance: in which contexts does each concept appear? When does the distinction matter?

**6. Common Confusion Points**
What students typically mix up between the two, and how to keep them straight.

Write the full comparison to `session.md` and `session.html` in the working directory. Apply language/term settings.
