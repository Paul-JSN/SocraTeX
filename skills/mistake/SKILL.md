---
name: mistake
description: Use when the user wants to identify mistakes, gaps, and misconceptions. Analyzes the student's actual error patterns from conversation history, exercises, and quizzes to generate targeted corrections
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Parse $ARGUMENTS to identify the topic scope (e.g., "limits", "Newton's third law", "all"). If empty, analyze all topics covered in this session.

Find relevant textbook content if available. Detect the subject. Adapt the analysis to the subject's conventions and common pitfalls.

**Step 1: Scan conversation history**

This is the core of this skill. Thoroughly review the entire conversation for:
- Wrong answers the student gave during `/exercise`, `/quiz`, `/proof`, `/derive`
- Misconceptions revealed in `/study` dialogue (incorrect intuitions, wrong assumptions)
- Hints that were needed (topics where `hints_before_answer` was reached)
- Patterns across multiple mistakes (e.g., always forgets to check units, confuses similar notation)

Categorize each mistake by type:
- **Conceptual** — misunderstands the idea itself
- **Procedural** — knows the concept but applies it wrong
- **Notational** — reads or writes the math/formula incorrectly
- **Careless** — knows everything but makes avoidable slips

**Step 2: Gap analysis**

Based on the mistakes found, identify:
- Which concepts are shaky (need review)
- Which are solid (no mistakes)
- Which haven't been tested yet (blind spots)

Present as a gap map:
```
✅ Solid: [concepts with no errors]
⚠️ Shaky: [concepts with mistakes — needs review]
❓ Untested: [concepts not yet attempted]
```

**Step 3: Your mistake patterns**

For each actual mistake the student made:
- **What you did:** Quote or paraphrase their response
- **The error:** What specifically went wrong, with the wrong work in LaTeX
- **The fix:** Correct approach with worked example in LaTeX
- **The pattern:** Is this part of a recurring pattern? (e.g., "This is the 3rd time you dropped a negative sign")
- **Practice:** A targeted exercise to reinforce this specific weak point

**Step 4: Common mistakes** (supplementary)

Add 2-3 common mistakes for the topic that the student has NOT made yet — as a preventive warning. Keep this section brief; the focus is on actual student data.

**Step 5: Targeted practice plan**

Based on the gap analysis, generate:
- 3-5 specific exercises targeting the weakest areas
- Ordered by priority (most critical gap first)
- Each with a brief note on which mistake it targets

Write the full analysis to `session.md` in the working directory (overwrite). All math in LaTeX.
