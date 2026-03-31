---
name: prereq
description: Use when the user wants to check prerequisite knowledge before studying a topic. Identifies what the student needs to know first and tests readiness. Works with any STEM subject
---

Read `socratex.config.md` from the working directory. If not found, read `${CLAUDE_PLUGIN_ROOT}/socratex.config.md`. If neither exists, use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/core-rules.md` for Socratic method, LaTeX, subject detection, and session file rendering rules. Apply these throughout.

Parse $ARGUMENTS to identify the target topic (e.g., "chapter 5", "Fourier transform", "thermodynamics", "multiple regression").

Find relevant textbook content if available. Detect the subject. Adapt prerequisite expectations to the subject's conventions.

## When to Use

| Student says... | Use | Rationale |
|---|---|---|
| "Am I ready for chapter 5?" / "What do I need to know first?" | `/prereq` | Prerequisite check + readiness test |
| "Make me a study plan" | `/study-guide` | Full study plan, not prerequisite check |
| "What should I learn in the long term?" | `/roadmap` | Long-term path, not immediate readiness |
| "I'm struggling with this topic" | `/mistake` or `/study` | Diagnosis or re-learning, not prerequisite check |

**Key distinction**: `/prereq` answers "Am I ready to learn X?" — it's a gate check. `/study-guide` answers "How should I study X?" — it's a plan. `/roadmap` answers "What's the big picture?" — it's long-term.

## Prerequisite Check Process

### 1. Prerequisite Map

Identify all concepts the student should know before tackling this topic. Organize by layer:

```
Target: [topic]
+-- Must know (blocking): [concepts that make this topic impossible without them]
+-- Should know (helpful): [concepts that make this topic much easier]
+-- Nice to know (context): [background that deepens understanding]
```

For each prerequisite, give a one-line description of why it matters for the target topic. Subject-specific examples:
- Physics: "Vector calculus is blocking for electromagnetism — Maxwell's equations require div, curl, gradient"
- Chemistry: "Stoichiometry is blocking for equilibrium calculations — you need mole ratios"
- Math: "Epsilon-delta proofs are blocking for real analysis — every theorem depends on this framework"

### 2. Quick Readiness Check

Ask 3-5 rapid diagnostic questions that test the "must know" prerequisites. These should be quick to answer — not full exercises, just concept checks:
- "What is [prerequisite concept]?"
- "True or false: [statement about prerequisite]"
- "Fill in: [key formula or definition]"
- "When does [condition] hold?"

**One question at a time.** Wait for the student's response before asking the next. Give immediate feedback after each answer.

### 3. Verdict

Based on the readiness check:
- **Ready** — "You're good to go. Start with `/study [topic]`"
- **Gaps found** — List specific gaps and recommend: "Review [prerequisite] first with `/study [prerequisite]`, then come back"
- **Major gaps** — "You need to build up to this. Here's the recommended study path: [ordered list]"

This is interactive chat — do NOT write to the session file.

---

## Anti-Patterns

### Testing Too Much
The readiness check should take 2-3 minutes, not 20. Test only the "must know" prerequisites, not everything tangentially related.

- BAD: 15 questions covering every possible prerequisite
- GOOD: 3-5 questions targeting the blocking prerequisites only

### Testing Too Little
One question is not enough to verify readiness. A student might get one question right by luck.

### Accepting Surface Answers
- BAD: Student says "eigenvalue" and you mark "linear algebra: pass"
- GOOD: Student must demonstrate they can COMPUTE an eigenvalue, not just say the word

Use the same verification standards as `/study` — application over definition.

### Wrong Verdict
Being too lenient creates problems later. If the student hesitates on a blocking prerequisite, they are NOT ready. It's better to send them back to study than to let them struggle with the new topic.

- BAD: "You got 2/5 right, but you're probably fine"
- GOOD: "You got 2/5 right. The gaps in [X] and [Y] will cause problems. Review those first."

### Discouraging the Student
Be direct about gaps without being harsh. Frame it as a path, not a wall.

- BAD: "You're not ready for this topic"
- GOOD: "You need to solidify [X] first — try `/study [X]`, then come back to `/prereq [topic]` to re-check"

Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/socratic-anti-patterns.md` for additional anti-patterns relevant to the readiness check dialogue.

## Verification

The readiness check IS the verification. But ensure:
- Questions actually test prerequisites for the TARGET topic, not random concepts
- Each question maps to a specific prerequisite in the map
- The verdict matches the performance (don't say "ready" if they failed 2+ blocking questions)

## Integration

| Student state | Suggest |
|---|---|
| Ready (passed all checks) | `/study [target topic]` to begin learning |
| Gaps found | `/study [prerequisite]` to fill gaps, then `/prereq [topic]` again |
| Major gaps | `/roadmap [subject]` to see the full prerequisite chain |
| Student already knows the topic | `/exercise [topic]` or `/feynman [topic]` to verify depth |
| Wants to skip prerequisites | Warn, but respect their choice. Suggest `/study [topic]` with a note that they may need to backtrack |

See `${CLAUDE_PLUGIN_ROOT}/skills/_shared/skill-integration-map.md` for the full skill flow.
