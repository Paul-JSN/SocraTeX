---
name: whatif
description: Use when the user asks "what if" or wants to explore hypothetical scenarios — changing variables, removing constraints, or testing edge cases. Context-isolated so it doesn't disrupt study flow. Works with any STEM subject
---

This skill provides context isolation, like `/btw`. The what-if exploration must NOT derail the current study session.

Use the Agent tool to spawn a sub-agent that handles the what-if scenario independently. The sub-agent should:

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, render_mode=desktop, subject=auto.

Parse $ARGUMENTS to identify the scenario. This can be:
- Numerical: "what if mass = 100kg?", "what if x = 0?"
- Conceptual: "what if gravity didn't exist?", "what if all functions were continuous?"
- Constraint removal: "what if we drop the assumption that...?"

Find relevant textbook content if available. Detect the subject.

**Phase 1: Setup**
Present the original formula/law/concept in LaTeX. State the current assumptions.
Then state the what-if change clearly: "We're changing [X] to [Y]. Everything else stays the same."

**Phase 2: Predict**
Ask the student: "Before we work this out — what do you THINK will happen?" Wait for their prediction.

**Phase 3: Explore**
Work through the consequences step by step:
- For numerical what-ifs: compute with the new values, compare to baseline
- For conceptual what-ifs: trace the logical chain ("if A changes, then B must change because...")
- For constraint removal: show what breaks and why the constraint exists

**Phase 4: Insight**
- Compare prediction vs result
- Ask: "Why did [surprising thing] happen?"
- Connect back to the underlying principle

After the sub-agent finishes, display the result and state:

"Back to our study session —"

Resume from where the student left off.

This is interactive chat — do NOT write to session.md.
