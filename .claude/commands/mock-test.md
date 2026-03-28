---
description: Generate a mock exam based on textbook exercises and patterns
---

Read `socratex.config.md` for language settings.

Parse $ARGUMENTS as a chapter range. Read all exercises and theorems in that range from `books/`.

Generate a mock exam:

**Structure:**
- Difficulty distribution: 30% easy, 50% medium, 20% hard
- Mix of: definitions, proofs, computations, and conceptual questions
- Match the textbook's exercise style and notation

**For each question:**
- Number and point value
- Full problem statement in LaTeX
- Estimated time (in minutes)

**At the end:**
- Total points and recommended time
- Topic coverage summary

**Solutions:** Do NOT show solutions initially. When the student says "solutions", "answers", or "show solutions", then reveal step-by-step solutions for each question.

Write the mock test to `session.md` in the book directory (overwrite for clean test format).
