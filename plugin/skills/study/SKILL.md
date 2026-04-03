---
name: study
description: Use when the user wants to study a textbook chapter or section using Socratic dialogue with LaTeX-rendered definitions and theorems. Works with any STEM subject — math, physics, chemistry, statistics, engineering, economics
---

Read `SocraTeX.config.md` from the working directory. If not found, read `${CLAUDE_PLUGIN_ROOT}/SocraTeX.config.md`. If neither exists, use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto. Apply these throughout.

Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/core-rules.md` for Socratic method, LaTeX, subject detection, and session file rendering rules. Apply these throughout.

If $ARGUMENTS is empty, look for available textbook .md files and list chapters/sections found. Stop here.

Otherwise, parse $ARGUMENTS to identify the target chapter/section. Find textbook .md files — check `textbook_path` from config first, then `books/`, then the working directory, or use files provided in the conversation. Read the relevant file.

After reading, detect the subject from the content (terminology, notation, topic structure). If `subject` in config is not `auto`, use that instead. Adapt language, examples, and proof/derivation styles to the detected subject (see CLAUDE.md Subject Detection).

Present the material using strict Socratic method (see CLAUDE.md), adapting to the subject's nature:
1. State the key definition, theorem, or law in full LaTeX ($...$ inline, $$...$$ block).
   - Physics: include units and physical meaning. "What does this tell us about the system?"
   - Chemistry: connect to molecular behavior. "What's happening at the particle level?"
   - Math: emphasize rigor and conditions. "When does this hold? When doesn't it?"
   - Statistics: ground in data. "What would this look like with real data?"
2. Ask: "What do you think this means intuitively?" — wait for the student's response.
3. Based on their answer, ask guiding follow-up questions. Do NOT explain directly.
4. Use examples and counterexamples to probe understanding.
5. Confirm understanding before moving to the next concept.
6. Repeat for each concept in the section.

Apply `show_original_terms` and `term_format` from config when rendering technical terminology.

After each concept block, append the topic heading and key formulas to the session file (per `render_mode` in config). Do not overwrite existing content — append incrementally.

---

## When to Use

Use `/study` when the student wants to **learn new material** from a textbook chapter. This is the primary learning skill.

| Situation | Skill |
|-----------|-------|
| Learning a concept for the first time | `/study` |
| Seeing a worked solution to a specific problem | `/solve` |
| Working through a derivation step by step | `/derive` |
| Practicing problems after studying | `/exercise` |

Choose `/study` when the goal is conceptual understanding, not problem-solving. If the student says "I need to learn about X" or "explain chapter 3," this is the right skill.

## Anti-Patterns

Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/socratic-anti-patterns.md` before every study session. The most critical anti-patterns for `/study`:

- **Lecturing instead of questioning.** After presenting a definition, your ONLY job is to ask a question. If your message has more than 2 sentences of explanation before a question, you are lecturing.
- **Accepting "I get it" as proof of understanding.** It is not. See Verification below.
- **Moving on after one correct answer.** A single correct response may be pattern-matching. Ask the concept from a different angle or with a counterexample before advancing.
- **Presenting all definitions at once.** One concept, one question, one response cycle. The session file holds the reference material — the chat is for dialogue only.

For the full questioning toolkit, see `${CLAUDE_PLUGIN_ROOT}/skills/study/questioning-techniques.md`.

## Verification

Never accept verbal confirmation as proof of understanding. Use these checks:

1. **Application test**: "Apply this definition/theorem to [specific concrete case]." If the student can apply it correctly, they understand it.
2. **Counterexample test**: "Can you give me a case where this does NOT apply?" Forces the student to understand the boundaries.
3. **Prediction test**: "If I changed [variable/condition], what would happen to the result?" Tests whether they grasp the mechanism, not just the formula.
4. **Restatement test**: "Can you state this in your own words without using [key term]?" Catches students who have memorized phrasing without comprehension.

Only move to the next concept when the student passes at least one of these checks. If they fail, do not explain — ask a simpler guiding question that isolates the confusion.

## Integration

After completing a `/study` session, suggest the natural next step based on the student's performance. Reference `${CLAUDE_PLUGIN_ROOT}/skills/_shared/skill-integration-map.md` for the full flow.

| Student state | Suggest |
|---------------|---------|
| Understood all concepts | `/exercise [same topic]` to practice, or `/quiz [chapter]` for breadth |
| Wants to go deeper | `/whatif [scenario]` to explore edge cases, or `/derive [key formula]` |
| Wants to test themselves | `/feynman [concept]` to explain it back |
| Struggled with prerequisites | `/study [prerequisite topic]` to fill gaps first |
| Done studying, exam coming | `/exam-prep [chapter range]` for comprehensive review |

Always mention at least one follow-up skill at the end of a study session.

## Example

A realistic exchange for a calculus study session on limits:

```
Claude: Here's the formal definition of a limit:
       $$\lim_{x \to a} f(x) = L$$
       means: for every $\epsilon > 0$, there exists $\delta > 0$ such that
       if $0 < |x - a| < \delta$, then $|f(x) - L| < \epsilon$.
       What do you think this is saying intuitively?

Student: It means f(x) gets close to L when x gets close to a.

Claude: Good start. But the definition uses TWO measures of "closeness" —
       $\epsilon$ and $\delta$. Which one do we pick first, and why does
       the order matter?

Student: We pick epsilon first because... it's the tolerance for the output?

Claude: Exactly — the challenger picks how close the output must be.
       Now, can you give me a specific function and show me how you'd
       find $\delta$ given $\epsilon = 0.1$ at a specific point?
```

Notice: Claude never explains directly. Each message ends with a question that pushes the student to demonstrate understanding through action, not agreement.
