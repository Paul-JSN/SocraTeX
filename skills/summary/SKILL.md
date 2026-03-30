---
name: summary
description: Use when the user wants a concise summary of studied content — key concepts, formulas, and takeaways in a compact format. Works with any STEM subject
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Parse $ARGUMENTS:
- A topic or chapter range → summarize that content from textbook files
- Empty → summarize what was covered in this study session

Find textbook .md files if a range is specified. Detect the subject from content.

Generate a concise summary (shorter than study-guide — this is a quick reference, not a comprehensive overview):

**1. Core Concepts** (3-5 bullet points)
One sentence each. What are the essential ideas?

**2. Key Formulas/Laws**
The critical formulas in LaTeX $$...$$ blocks. Only the ones worth memorizing — not every formula, just the important ones.

**3. Key Results/Theorems**
Statement only (no proofs). One line each.

**4. Connections**
How these concepts relate to each other. 2-3 sentences.

**5. What to Review**
Based on difficulty of the material, flag concepts that need more practice.

Apply `show_original_terms` and `term_format` from config.

Write the summary to `session.md` in the working directory (overwrite).
