---
name: socratex-quiz
description: Use when the user wants a quick 10-question quiz for rapid review — True/False, fill-in-the-blank, definition matching
---

Read `socratex.config.md` for language, difficulty, and term settings.

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

Do NOT write to session.md — this is a quick interactive quiz in the chat.
