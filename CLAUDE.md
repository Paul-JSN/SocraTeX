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

Check `render_mode` in `socratex.config.md` to decide output behavior:

**`render_mode: browser`** (default — works everywhere):
- Write reference content to `session.html` in the current book directory
- Use this HTML template (KaTeX CDN + 3-second auto-refresh):
  ```html
  <!DOCTYPE html>
  <html><head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="3">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
  <style>body{max-width:800px;margin:40px auto;padding:0 20px;font-family:Georgia,serif;line-height:1.8;font-size:18px;color:#1a1a1a}h1,h2,h3{color:#2c3e50}code{background:#f4f4f4;padding:2px 6px;border-radius:3px}</style>
  </head><body>
  [CONTENT — convert markdown to HTML paragraphs/headings, keep $...$ and $$...$$ for KaTeX]
  <script>renderMathInElement(document.body,{delimiters:[{left:"$$",right:"$$",display:true},{left:"$",right:"$",display:false}]});</script>
  </body></html>
  ```
- On FIRST write of a session, auto-open the file: run `start session.html` (Windows) or `open session.html` (Mac) or `xdg-open session.html` (Linux) via Bash tool
- Subsequent updates: just overwrite the file — browser auto-refreshes via meta tag

**`render_mode: vscode`** (for VS Code users):
- Write reference content to `session.md` in the current book directory
- User views it with VS Code Markdown Preview (Ctrl+K V) + Markdown+Math extension
- No need to open browser

**Common rules for both modes:**
- Structure: Current Topic → Key Formulas → Current Exercise / Reference Content
- For incremental commands (/study, /exercise, /proof): append to session file
- For full-document commands (/exam-prep, /study-guide, /mock-test, /compare, /translate): overwrite session file with new content

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
