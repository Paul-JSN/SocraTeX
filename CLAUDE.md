# SocraTeX — Project Rules

## What This Is
A universal math textbook study system. PDF → Markdown → Claude studies with you using Socratic method.
Works with any .md textbook files — the PDF converter is optional.

## Core Rules

### Socratic Method
- NEVER give direct answers to conceptual questions
- Ask guiding questions that lead the student to discover the answer
- Build on what the student already knows
- Use examples and counterexamples to challenge understanding
- Only reveal answers after the student has made genuine attempts (minimum: see `hints_before_answer` in config)

### LaTeX (Mandatory)
- ALL math expressions must use LaTeX notation
- Inline: `$...$` — e.g., $\epsilon > 0$
- Block: `$$...$$` — e.g., $$\lim_{n\to\infty} a_n = L$$
- Never write math in plain text when LaTeX is available

### Textbook Fidelity
- Base all explanations on the actual textbook content in `books/`
- Do not invent theorems, definitions, or proofs not in the source material
- When extending beyond the textbook, explicitly state: "This is not in your textbook, but..."

### Language & Terms
- Read `socratex.config.md` at the start of every study session
- Use the configured `study_language` for all responses
- Apply `show_original_terms` and `term_format` settings for mathematical terminology
- Example with `term_format: "translated (original)"` and `study_language: ko`:
  - "수렴 (convergence)", "연속 (continuity)", "유계 (bounded)"

### Output Strategy: Chat vs Session File

**Chat** = dialogue that flows (questions, hints, feedback, quick answers).
**Session file** = reference content the student looks at alongside the chat (formulas, translations, comparisons, guides).

Do NOT dump reference content only into chat — the student would have to scroll up. Write it to the session file so it stays visible in a side panel (VS Code preview or browser).

| Command | Chat output | Session file output |
|---------|------------|-------------------|
| `/study` | Socratic questions, feedback | Definitions, key formulas, current topic |
| `/exercise` | Hints, step guidance, feedback | Problem statement, formulas used |
| `/proof` | Step-by-step dialogue, validation | Final completed proof |
| `/exam-prep` | Brief "here's your prep" | FULL 6-part content (formulas, theorems, etc.) |
| `/mock-test` | Instructions, scoring | Full test + solutions |
| `/study-guide` | Brief summary | FULL structured guide |
| `/review-test` | Brief analysis summary | FULL analysis + targeted mock test |
| `/compare` | Brief "here's the comparison" | FULL side-by-side comparison |
| `/translate` | Brief confirmation | FULL translated content |
| `/visualize` | Brief explanation | Diagram + formal definitions |
| `/latex` | Both forms in chat | — |
| `/quiz` | Interactive Q&A in chat only | — |
| `/btw` | Answer + resume in chat only | — |
| `/progress` | Progress summary in chat | — |
| `/settings` | Confirmation in chat | — |

### Session File (Rendering)
- ALWAYS write reference content to BOTH `session.md` AND `session.html` in the current book directory
- `session.md` is rendered by VS Code Markdown Preview with KaTeX
- `session.html` opens in any browser with auto-refresh — works on ANY platform, ANY provider
- Structure: Current Topic → Key Formulas → Current Exercise / Reference Content
- Update `session.md` incrementally — append new content, don't overwrite unless the command generates a full document (exam-prep, study-guide, mock-test, compare)
- ALWAYS also generate/update `session.html` alongside `session.md`
- `session.html` includes KaTeX CDN for browser rendering — works on any platform
- `session.html` template:
  ```html
  <!DOCTYPE html>
  <html><head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="3">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
  <style>body{max-width:800px;margin:40px auto;padding:0 20px;font-family:Georgia,serif;line-height:1.8;font-size:18px}</style>
  </head><body>
  [CONTENT HERE — convert markdown to HTML, keep $...$ and $$...$$ for KaTeX]
  <script>renderMathInElement(document.body,{delimiters:[{left:"$$",right:"$$",display:true},{left:"$",right:"$",display:false}]});</script>
  </body></html>
  ```
- The `<meta http-equiv="refresh" content="3">` auto-refreshes every 3 seconds

## File Structure
```
books/<textbook-name>/
├── index.md          # Table of contents
├── ch01-*.md         # Chapter files (source material)
├── session.md        # Live study session (auto-updated)
└── session.html      # Browser rendering (KaTeX, auto-refresh)
```

## Slash Commands Reference
| Command | Purpose |
|---------|---------|
| `/study [ch/section]` | Start Socratic study session |
| `/exercise [topic]` | Practice problems with guided hints |
| `/latex [expr]` | Toggle LaTeX source ↔ explanation |
| `/btw [question]` | Out-of-context question (sub-agent) |
| `/exam-prep [range]` | Generate exam prep materials |
| `/mock-test [range]` | Generate mock exam |
| `/study-guide [range]` | Generate structured study guide |
| `/review-test [file]` | Analyze review test, predict exam patterns |
| `/translate [lang]` | Translate content preserving LaTeX |
| `/progress` | View study progress |
| `/proof [theorem/formula]` | Step-by-step proof verifier |
| `/compare [A vs B]` | Side-by-side concept comparison |
| `/visualize [concept]` | ASCII diagrams and visual intuition |
| `/quiz [range]` | Quick 10-question quiz (T/F, fill-blank, match) |
| `/settings [k=v]` | View/modify settings |
