---
name: derive
description: Use when the user wants to derive a formula, equation, or law step by step with Socratic guidance. Works with any STEM subject — physics equations, math identities, chemistry equilibria
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Parse $ARGUMENTS to identify what to derive (e.g., "E=mc²", "quadratic formula", "Nernst equation", "central limit theorem", "Euler-Lagrange equation").

Find relevant textbook .md files if available. Detect the subject from content. If `subject` in config is not `auto`, use that instead.

Present the target result in full LaTeX: "We want to arrive at: $$...$$"

Then state the starting assumptions and known prerequisites.

Enter **derivation mode** (Socratic):
1. Ask: "What's our starting point? What do we already know that could lead us here?"
2. The student proposes each step.
3. For EACH step, evaluate:
   - Valid → confirm, ask for the next step
   - Gap → "What justifies this transition?" or "What assumption are you making here?"
   - Wrong → "Let's check the units/dimensions" or "What happens if we test this with a specific case?"
4. If stuck, hint at the TECHNIQUE, not the step: "Try applying [conservation law / chain rule / ideal gas assumption / Taylor expansion]"
5. When complete, present the full derivation cleanly in LaTeX with all steps numbered.

**Subject-specific adaptation:**
- Physics: emphasize dimensional analysis, check units at each step
- Chemistry: track stoichiometry, verify equilibrium conditions
- Math: verify logical rigor, check boundary cases
- Statistics: verify distributional assumptions

Write the completed derivation to `session.md` in the working directory. Append, do not overwrite.
