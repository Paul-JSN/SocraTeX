---
name: quiz
description: Use when the user wants a quick 10-question quiz for rapid review — True/False, fill-in-the-blank, definition matching
---

Read `socratex.config.md` from the working directory. If not found, read `${CLAUDE_PLUGIN_ROOT}/socratex.config.md`. If neither exists, use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto. Detect the subject from context and adapt question style accordingly.

Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/core-rules.md` for Socratic method, LaTeX, subject detection, and session file rendering rules. Apply these throughout.

Parse $ARGUMENTS as a topic or chapter range. If empty, quiz on all studied material.

Generate a quick quiz with 10 questions mixing these types:

**True/False** (3-4 questions):
- Statement in LaTeX → student answers T or F
- After answer: brief explanation of why

**Fill in the Blank** (3-4 questions):
- Definition or theorem with a key part blanked: "A sequence is Cauchy if for every $\varepsilon > 0$, there exists _____ such that _____"
- Accept equivalent correct formulations

**Definition Match** (2-3 questions):
- Give the formal definition → student names the concept
- Or give the concept name → student states the definition

**Quick Scoring:**
After all 10 questions, show:
- Score: X/10
- Weak spots identified
- "Run `/exercise [topic]` to practice your weak areas"

Keep it fast — don't Socratic-method each question. Give immediate feedback after each answer. The point is speed and coverage, not deep exploration.

Do NOT write to the session file — this is a quick interactive quiz in the chat.

---

## Anti-Patterns

Avoid these when generating quiz questions:

**True/False**
- DO NOT write ambiguous statements where the answer depends on interpretation. "A continuous function is differentiable" is bad — it depends on context. "Every continuous function on $\mathbb{R}$ is differentiable" is clear (False).
- DO NOT write trivially true or trivially false statements. "The number 2 is even" tests nothing. "$\sum_{n=1}^{\infty} \frac{1}{n}$ converges" is a real test of knowledge.
- DO NOT include edge cases that even experts would debate. The answer must be unambiguous at the student's level.

**Fill in the Blank**
- DO NOT create blanks where multiple valid answers exist but only one is accepted. If the blank is "A metric space is _____ if every Cauchy sequence converges," accept both "complete" and "a complete metric space."
- DO NOT blank out trivial words. Blank the mathematically meaningful part: the key term, the condition, the bound.
- DO NOT create blanks that require memorizing exact phrasing rather than understanding the concept.

**Definition Match**
- DO NOT test obscure definitions that are not central to the chapter range. Focus on definitions that appear in multiple theorems or exercises.
- DO NOT accept vague paraphrases — require the essential mathematical content (e.g., for continuity, the $\varepsilon$-$\delta$ condition must appear in some form).

**General**
- DO NOT pull questions verbatim from the textbook. Students who reviewed the textbook may have memorized them. Rephrase or test the same concept from a different angle.
- DO NOT make all 10 questions the same difficulty. Include 3-4 straightforward recall questions, 4-5 moderate application questions, and 1-2 that require connecting ideas.
- DO NOT test pure memorization when you can test understanding. Instead of "State the Intermediate Value Theorem," ask "True or False: If $f$ is continuous on $[0,1]$ with $f(0)=-1$ and $f(1)=3$, then $f(c) = 2$ for some $c \in (0,1)$."

---

## Question Quality

Each question must meet these standards:

- **Exactly one unambiguous correct answer.** If you cannot defend why the answer is uniquely correct, rewrite the question.
- **True/False statements are clearly true or clearly false.** Test them by asking: could a knowledgeable student argue the opposite? If yes, rewrite.
- **Fill-in-the-blank targets the key concept**, not filler words. The blank should be the most mathematically important part of the sentence.
- **Definition match tests recognition of formal definitions**, not informal descriptions. The student should need to know the actual mathematical content.
- **Difficulty is distributed**: mark each question internally as easy/medium/hard. Ensure the set has variety.
- **Feedback is immediate and educational**: after each answer, explain WHY it is correct or incorrect in 1-2 sentences. Do not just say "Correct!" or "Wrong."

---

## Style Learning

Follow `${CLAUDE_PLUGIN_ROOT}/skills/_shared/style-analysis-guide.md` for matching textbook style.

- If the textbook has end-of-chapter review questions, analyze their style and match it. Some textbooks use "True/False with justification" — if so, require a brief justification, not just T/F.
- If the textbook uses specific terminology for question types (e.g., "Conceptual Questions" vs "Review Exercises"), mirror that language.
- Match the notation conventions from the textbook (variable names, theorem numbering, derivative notation).
- If no textbook review section exists, use a clean academic style with standard mathematical formatting.

---

## Integration

This skill connects to the study flow (see `${CLAUDE_PLUGIN_ROOT}/skills/_shared/skill-integration-map.md`):

- **If score < 7/10**, suggest `/exercise [weak topics]` for focused practice on the topics the student missed, then `/mistake [topic]` to analyze their error patterns
- **If score >= 7/10**, suggest `/flashcard [same range]` to reinforce the material through spaced repetition, then move to the next topic
- **For any missed question**, the feedback should name the specific concept that was weak, making it easy to run `/exercise [that concept]` or `/study [that section]`
- **Feeds from `/study`**: quiz is the natural check after a study session to verify retention
- **Feeds into `/mock-test`**: once quiz scores are consistently high, the student is ready for a full-length mock test
