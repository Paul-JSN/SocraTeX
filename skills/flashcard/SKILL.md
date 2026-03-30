---
name: flashcard
description: Use when the user wants to generate Q&A flashcards from studied content for review or Anki export. Works with any STEM subject
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Parse $ARGUMENTS to determine scope:
- A topic or chapter range → generate flashcards from that content
- "all" or empty → generate from all studied material in this session
- A number (e.g., "20") → generate that many cards

Find textbook .md files — check `textbook_path` from config first, then `books/`, then the working directory, or use files provided in the conversation. Detect the subject from content.

Generate flashcards as Q&A pairs:

**Card types to mix:**
- **Definition** — Front: "What is [term]?" / Back: formal definition in LaTeX
- **Formula** — Front: "Write the formula for [concept]" / Back: $$formula$$
- **Concept** — Front: "Explain why [statement] is true/false" / Back: reasoning
- **Application** — Front: "When would you use [technique]?" / Back: context + conditions

**Format — Markdown table:**
| # | Front | Back |
|---|-------|------|
| 1 | What is convergence? | A sequence $\{a_n\}$ converges to $L$ if... |

**After the table, generate Anki-importable format:**
```
Front<tab>Back
```
One card per line, tab-separated. Wrap in a code block so the student can copy it. LaTeX should use Anki's `\(` and `\)` delimiters for inline, `\[` and `\]` for block.

Apply `show_original_terms` and `term_format` from config.

Write the flashcard set to `session.md` in the working directory (overwrite).
