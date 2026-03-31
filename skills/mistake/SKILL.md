---
name: mistake
description: Use when the user wants to identify mistakes, gaps, and misconceptions. Analyzes the student's actual error patterns from conversation history, exercises, and quizzes to generate targeted corrections. Works with any STEM subject
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Parse $ARGUMENTS to identify the topic scope (e.g., "limits", "Newton's third law", "all"). If empty, analyze all topics covered in this session.

Find relevant textbook content if available. Detect the subject. Adapt the analysis to the subject's conventions and common pitfalls.

## When to Use

| Student says... | Use | Rationale |
|---|---|---|
| "What am I getting wrong?" / "Where are my gaps?" | `/mistake` | Pattern analysis from actual student data |
| "I keep making the same error" | `/mistake` | Identify the recurring pattern and drill it |
| "Give me a problem to practice" | `/exercise` | Practice new problems, not analyze old ones |
| "What should I study?" | `/study-guide` or `/prereq` | Planning, not diagnosis |

**Key distinction**: `/mistake` is backward-looking (analyzing what already happened). `/exercise` is forward-looking (practicing new problems). `/quiz` tests breadth. `/mistake` finds depth of specific weaknesses.

## Analysis Process

### Step 1: Scan conversation history

This is the core of this skill. Thoroughly review the entire conversation for:
- Wrong answers the student gave during `/exercise`, `/quiz`, `/derive`
- Misconceptions revealed in `/study` dialogue (incorrect intuitions, wrong assumptions)
- Hints that were needed (topics where `hints_before_answer` was reached)
- Patterns across multiple mistakes (e.g., always forgets to check units, confuses similar notation)

Categorize each mistake by type:
- **Conceptual** — misunderstands the idea itself
- **Procedural** — knows the concept but applies it wrong
- **Notational** — reads or writes the math/formula incorrectly
- **Careless** — knows everything but makes avoidable slips

### Step 2: Gap analysis

Based on the mistakes found, identify:
- Which concepts are shaky (need review)
- Which are solid (no mistakes)
- Which haven't been tested yet (blind spots)

Present as a gap map:
```
Solid: [concepts with no errors]
Shaky: [concepts with mistakes -- needs review]
Untested: [concepts not yet attempted]
```

### Step 3: Your mistake patterns

For each actual mistake the student made:
- **What you did:** Quote or paraphrase their response
- **The error:** What specifically went wrong, with the wrong work in LaTeX
- **The fix:** Correct approach with worked example in LaTeX
- **The pattern:** Is this part of a recurring pattern? (e.g., "This is the 3rd time you dropped a negative sign")
- **Practice:** A targeted exercise to reinforce this specific weak point

### Step 4: Common mistakes (supplementary)

Reference `mistake/common-stem-mistakes.md` for the detected subject. Add 2-3 common mistakes for the topic that the student has NOT made yet — as a preventive warning. Keep this section brief; the focus is on actual student data.

### Step 5: Targeted practice plan

Based on the gap analysis, generate:
- 3-5 specific exercises targeting the weakest areas
- Ordered by priority (most critical gap first)
- Each with a brief note on which mistake it targets

Write the full analysis to the session file (per `render_mode` in config). All math in LaTeX.

---

## Anti-Patterns

### Inventing Mistakes the Student Didn't Make
The most critical anti-pattern. If the conversation history shows no errors, say "I don't have enough data to analyze your mistakes. Try `/exercise [topic]` or `/quiz [topic]` first, then come back."

Never fabricate mistakes to have something to report.

### Generic Advice Instead of Specific Diagnosis
- BAD: "You should review integration techniques."
- GOOD: "In exercises 3 and 7, you forgot to apply the chain rule when differentiating composite functions. Specifically, you wrote $\frac{d}{dx}\sin(x^2) = \cos(x^2)$ instead of $\cos(x^2) \cdot 2x$."

Every diagnosis must quote or reference a specific student action.

### Conflating Mistake Types
A conceptual misunderstanding requires different remediation than a careless error. If the student understands the concept but keeps dropping negative signs, sending them back to `/study` is wrong — they need `/exercise` with careful attention to signs.

| Mistake type | Remedy |
|---|---|
| Conceptual | `/study [topic]` — re-learn the concept |
| Procedural | `/exercise [topic]` — practice the procedure |
| Notational | `/exercise` with explicit notation focus |
| Careless | Practice with self-checking habit (estimate first, verify units) |

### Overwhelming the Student
If there are 10+ mistakes, prioritize. Present the top 3-5 patterns that will fix the most problems. Group related mistakes under one pattern rather than listing each individually.

### Praising to Soften the Blow
This skill is diagnostic. Be direct and specific, not encouraging. "You made 4 sign errors" is more useful than "Great effort! Just watch out for a few small sign things."

Read `_shared/socratic-anti-patterns.md` for additional anti-patterns.

## Verification

After presenting the analysis:
- Give the student 1-2 targeted problems from the practice plan
- If they solve correctly: the diagnosis was accurate, the gap is closing
- If they make the same mistake again: the issue is deeper than identified — suggest `/study [prerequisite]`
- If they make a different mistake: update the analysis

## Integration

| Student state | Suggest |
|---|---|
| Conceptual gaps identified | `/study [weak topic]` to re-learn, then `/exercise` to practice |
| Procedural errors | `/exercise [topic]` with focus on the specific procedure |
| Recurring careless errors | `/exercise` with emphasis on verification habits |
| Wants to test if gaps are fixed | `/quiz [topic]` for a quick assessment |
| Gaps are closed | `/exercise` for harder problems, or move to next topic |
| Student disagrees with diagnosis | `/feynman [concept]` — have them explain the concept to verify understanding |

See `_shared/skill-integration-map.md` for the full skill flow.
