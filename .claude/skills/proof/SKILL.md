---
name: proof
description: Use when the user wants to write and verify a proof or derivation step by step, with logical validation at each line
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop.

Parse $ARGUMENTS to identify what to prove or derive. This can be:
- A theorem name/number (e.g., "Theorem 3.1.1", "Bolzano-Weierstrass")
- A formula to derive (e.g., "quadratic formula", "integration by parts")
- An identity to prove (e.g., "sum of geometric series")

Present the statement to be proved in full LaTeX.

Then enter **proof mode**:
1. Ask: "What would be your first step or approach?"
2. The student writes each step of the proof/derivation.
3. For EACH step, evaluate:
   - Is the logic valid? If yes: confirm and ask for the next step.
   - Is there a gap? Ask: "Why does this follow from the previous step?"
   - Is it wrong? Don't say "wrong" directly. Ask: "What assumption are you using here?" or "Can you think of a case where this doesn't hold?"
4. If the student is stuck, offer a strategic hint — not the next step, but the TECHNIQUE to use (induction, contradiction, epsilon-delta, etc.)
5. When the proof is complete, summarize the full proof cleanly with all steps in LaTeX.

Update `session.md` in the working directory with the theorem statement and completed proof. Also update `session.html` if it exists.
