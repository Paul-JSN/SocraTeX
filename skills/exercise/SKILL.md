---
name: exercise
description: Use when the user wants to practice problems with guided hints, tracking attempts before revealing solutions. Works with any STEM subject
---

Read `socratex.config.md` from the working directory. If not found, read `${CLAUDE_PLUGIN_ROOT}/socratex.config.md`. If neither exists, use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/core-rules.md` for Socratic method, LaTeX, subject detection, and session file rendering rules. Apply these throughout.

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

After presenting each exercise and during solution steps, update the session file (per `render_mode` in config) with the current exercise and key formulas. Append, do not overwrite.

---

## When to Use

Use `/exercise` when the student wants to **practice applying** concepts they have already studied.

| Situation | Skill |
|-----------|-------|
| Practice problems with guided hints | `/exercise` |
| See a full worked solution (Claude demonstrates) | `/solve` |
| Step through a derivation interactively | `/derive` |
| Learn the concept for the first time | `/study` |

If the student has not yet studied the topic and is immediately struggling, suggest `/study [topic]` first rather than giving increasingly explicit hints.

## Anti-Patterns

### Hints That ARE the Answer
The most common failure mode. A hint should narrow the search space, not eliminate it.

- BAD hint: "Use integration by parts with $u = x$ and $dv = e^x dx$." (This IS the solution setup.)
- GOOD hint: "This integrand is a product of two types of functions. What technique handles products?"

### Revealing the Technique in the First Hint
The first hint should be the most general. Never name the specific method on hint 1.

- BAD first hint: "Apply L'Hopital's rule."
- GOOD first hint: "What form does this limit take when you substitute directly?"

### Not Scaling Hint Specificity
Each hint must be strictly more specific than the previous one. If hint 2 is no more helpful than hint 1, you have wasted a hint.

### Giving All Hints at Once
One hint per message. Wait for the student to respond and attempt something before offering the next hint.

Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/socratic-anti-patterns.md` for the full anti-pattern reference.

## Style Learning

Before generating problems, read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/style-analysis-guide.md` and analyze the textbook's exercise style:
- Match the numbering format, sub-part structure, and difficulty curve
- Use the same variable names and notation conventions as the textbook
- If the textbook uses "Show that..." for proofs, use "Show that..." (not "Prove that...")
- Generated problems should look like they belong in the same textbook

For detailed problem creation strategies, see `${CLAUDE_PLUGIN_ROOT}/skills/exercise/problem-generation-guide.md`.

## Hint Progression Example

Problem: Find $\lim_{x \to 0} \frac{e^x - 1 - x}{x^2}$.

**Hint 1 (General direction):**
"What happens when you substitute $x = 0$ directly into the numerator and denominator? What form do you get?"
--> Student should recognize $\frac{0}{0}$ indeterminate form.

**Hint 2 (Narrow the technique):**
"We have a $\frac{0}{0}$ form. You know at least two techniques for handling these — one involves derivatives, another involves expanding functions as series. Which feels more natural here?"
--> Student chooses a technique.

**Hint 3 (Specific guidance):**
"If you expand $e^x$ as a Taylor series around $x = 0$ up to the $x^2$ term, what do you get for the numerator after subtracting $1 + x$?"
--> Student should be able to finish: numerator becomes $\frac{x^2}{2} + \cdots$, limit is $\frac{1}{2}$.

Notice: each hint is strictly more specific. Hint 1 does not mention any technique. Hint 2 names categories but not the answer. Hint 3 points to the specific approach but still requires the student to execute.

## Difficulty Calibration

Track student performance within the session and adjust:

| Signal | Action |
|--------|--------|
| Solved with 0 hints, correct on first attempt | Increase difficulty: add constraints, combine concepts, or reverse the problem (see `problem-generation-guide.md`) |
| Solved with 1 hint | Maintain current level, vary the problem type |
| Needed 2+ hints | Stay at current difficulty, generate another problem targeting the same concept |
| Failed after all hints | Drop difficulty. Consider suggesting `/study [prerequisite]` to review the underlying concept |
| Repeated errors on the same step | This is a misconception, not a difficulty issue. Suggest `/mistake [topic]` to analyze the pattern |

When `difficulty=adaptive` in config, apply this calibration automatically. When set to a fixed level, stay at that level but still note when the student is clearly above or below it.

## Integration

After an exercise session, suggest the natural next step. Reference `${CLAUDE_PLUGIN_ROOT}/skills/_shared/skill-integration-map.md` for the full flow.

| Student state | Suggest |
|---------------|---------|
| Solved problems consistently | `/quiz [topic]` for breadth testing across the chapter |
| Made repeated errors | `/mistake [topic]` to identify patterns, then return to `/exercise` |
| Completely stuck, could not start | `/solve [problem]` to see a worked example, then retry with `/exercise` |
| Wants more challenge | `/exercise` with harder variants, or `/derive` to understand why the formulas work |
| Done practicing, exam coming | `/mock-test [chapter range]` for timed practice |
