---
description: Generate a structured study guide — big picture overview, concept hierarchy, per-section summaries, printable formula sheet in LaTeX, optimal study order, and time estimates
---

Read `socratex.config.md` for language and term settings.

Parse $ARGUMENTS as a chapter range. Read all .md files in that range from `books/`.

Generate a structured study guide:

**1. Big Picture**
2-3 sentences: what this range covers and why it matters.

**2. Concept Hierarchy**
Outline format showing how topics build on each other. Indent sub-topics.

**3. Section Summaries**
One-line summary per section. Focus on the key takeaway.

**4. Formula Sheet**
All critical formulas in LaTeX $$...$$ blocks. Organized by topic. Designed to be printed/copied.

**5. Recommended Study Order**
Optimal sequence if topics have prerequisites. Flag which sections are most exam-relevant.

**6. Estimated Study Time**
Per-section time estimates based on concept density and difficulty.

Write the complete guide to `session.md` in the book directory (overwrite). Apply language/term settings.
