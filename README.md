<div align="center">

# SocraTeX

### Socratic + LaTeX

**Study any math textbook with Claude.**

Drop your `.md` files and start a Socratic dialogue. All math in LaTeX.

---

<img src="https://img.shields.io/badge/license-CC--BY--NC--ND--4.0-blue" alt="License" />
<img src="https://img.shields.io/badge/setup-zero--dependency-brightgreen" alt="Zero Dependency" />
<img src="https://img.shields.io/badge/platform-Claude_Code_%7C_Claude.ai-blueviolet" alt="Platform" />

[한국어](docs/README_ko.md) | [中文](docs/README_zh.md) | [日本語](docs/README_ja.md) | [Espanol](docs/README_es.md)

</div>

---

## What is SocraTeX?

15 slash commands that turn Claude into a Socratic math tutor. No setup, no dependencies — just Markdown files with LaTeX.

```
Your .md textbook  ──>  Claude reads it  ──>  Socratic dialogue
                                               (never gives direct answers)
```

**No direct answers.** Claude guides you with questions, hints, and counterexamples until you discover the solution yourself. All math is rendered in beautiful LaTeX.

> **Have a PDF?** Use [MinerU](https://mineru.net) (Precision mode, `vlm` model) to convert PDF to Markdown with LaTeX preserved. Free tier available.

---

## Features

| Command | What it does |
|---------|-------------|
| `/study [chapter]` | Socratic walkthrough — reads the chapter, asks guiding questions, never gives answers directly |
| `/exercise [topic]` | Guided practice — incremental hints, tracks attempts, generates similar problems |
| `/exam-prep [range]` | Full exam prep — formula cheat sheet, theorem summaries, must-do exercises, proof strategies, common mistakes, concept map |
| `/mock-test [range]` | Timed mock exam — 30/50/20 difficulty split, point values, hidden solutions |
| `/study-guide [range]` | Structured overview — concept hierarchy, section summaries, formula sheet, study order |
| `/review-test [file]` | Review analysis — predicts exam patterns, finds coverage gaps, generates targeted practice |
| `/proof [theorem]` | Proof mode — write your proof line by line, Claude verifies each step's logic. Works for theorems, formulas, identities |
| `/compare [A vs B]` | Side-by-side comparison — definitions, differences, similarities, counterexamples, when to use which |
| `/visualize [concept]` | ASCII visualization — function graphs, set diagrams, number lines, epsilon-delta illustrations |
| `/quiz [range]` | Quick 10-question quiz — True/False, fill-in-the-blank, definition matching. Fast review, instant scoring |
| `/latex [expr]` | LaTeX toggle — explain a formula, get copyable source, or convert plain text to LaTeX |
| `/translate [lang]` | Translate with math — preserves all LaTeX, configurable bilingual term display |
| `/btw [question]` | Side question — answered in isolation via sub-agent, resumes study flow automatically |
| `/settings [k=v]` | Configuration — language, difficulty, term annotations, hint count, render mode |
| `/progress` | Progress tracker — chapters covered, weak areas, next recommendations |

---

## Quick Start

### 1. Clone

```bash
git clone https://github.com/Paul-JSN/SocraTeX.git
cd SocraTeX
```

### 2. Add Your Textbook

```bash
mkdir -p books/my-textbook
# Place your .md files here
```

> **Converting from PDF?** Use [MinerU](https://mineru.net) — free, preserves LaTeX, outputs clean Markdown.

### 3. Start Studying

<table>
<tr>
<th>Claude Code (VS Code) — Full features</th>
<th>Claude.ai — Quick start</th>
</tr>
<tr>
<td>

```bash
claude
/study ch01
```

Open `session.md` in VS Code Markdown Preview for rendered LaTeX.

</td>
<td>

1. Create a **Project** on claude.ai
2. Upload `.md` files → Project Knowledge
3. Paste `claude-ai/system-prompt.md` → Custom Instructions
4. Chat: *"Let's study chapter 3"*

</td>
</tr>
</table>

### 4. Install Globally (Optional)

```bash
./install.sh        # macOS / Linux
./install.ps1       # Windows (PowerShell)
```

Use `/socratex:study`, `/socratex:exercise`, etc. from any project.

---

## How It Works

```
┌──────────────────────────────────────────────────────┐
│  VS Code                                             │
│  ┌──────────────────┐   ┌──────────────────────────┐ │
│  │  Claude Code     │   │  Markdown Preview        │ │
│  │                  │   │  (session.md + KaTeX)    │ │
│  │  > /study ch03   │   │                          │ │
│  │                  │   │  Definition 3.1.1        │ │
│  │  What do you     │   │                          │ │
│  │  think this ε    │   │  ∀ε>0, ∃N∈ℕ s.t.        │ │
│  │  condition       │   │  n≥N ⟹ |aₙ - L| < ε    │ │
│  │  means?          │   │                          │ │
│  │                  │   │  Key Formulas:           │ │
│  │  > It means...   │   │  lim aₙ = L             │ │
│  └──────────────────┘   └──────────────────────────┘ │
└──────────────────────────────────────────────────────┘
```

**Left**: Socratic dialogue with Claude &nbsp;&nbsp;|&nbsp;&nbsp; **Right**: Rendered LaTeX via session file

Two render modes:

| Mode | Output | Best for |
|------|--------|----------|
| `desktop` (default) | `session.html` — auto-opens in browser, KaTeX CDN, 3s auto-refresh | Claude Code Desktop / CLI |
| `vscode` | `session.md` — VS Code Markdown Preview | VS Code users |

Change with `/settings render=vscode` or `/settings render=desktop`.

---

## Configuration

Edit `socratex.config.md` directly or use `/settings`:

```yaml
study_language: en            # Any ISO 639-1 code (en, ko, ja, zh, es, fr, de, ...)
show_original_terms: false    # Show original terms alongside translations
term_format: "translated (original)"   # Options: "translated (original)" | "original → translated" | "translated [original]"
render_mode: desktop          # desktop (browser) | vscode (Markdown Preview)
difficulty: adaptive          # easy | medium | hard | adaptive
hints_before_answer: 3        # Minimum hints before revealing solutions
```

**Examples:**
```
/settings lang=ko terms=on              →  수렴 (convergence)
/settings lang=ja terms=on              →  収束 (convergence)
/settings format="original → translated" →  convergence → 수렴
/settings difficulty=hard hints=5
```

---

## Works With Any AI

SocraTeX commands are Claude Code native, but the system works with any AI:

| Provider | How to use |
|----------|-----------|
| **Claude Code** | Automatic — `/study`, `/exercise`, etc. just work |
| **Claude.ai** | Paste `claude-ai/system-prompt.md` into Custom Instructions |
| **Codex / OpenClaw** | Load `CLAUDE.md` + relevant command `.md` files as system context |
| **Gemini / GPT / Others** | Same — use `CLAUDE.md` as system prompt, load commands as needed |

The command files in `.claude/commands/` are plain Markdown instructions. Any AI that can read text can follow them.

---

## Project Structure

```
SocraTeX/
├── .claude/commands/    # 15 slash commands (skill format)
├── claude-ai/           # System prompt for Claude.ai
├── CLAUDE.md            # Rules for Claude (Socratic method, LaTeX, etc.)
├── socratex.config.md   # User settings
├── install.sh / .ps1    # Global installation scripts
└── books/               # Your textbook files go here
```

---

## Requirements

| Requirement | Notes |
|-------------|-------|
| Claude Code or Claude.ai | Any active plan |
| `.md` textbook files | With LaTeX notation (`$...$`, `$$...$$`) |
| VS Code + [Markdown+Math](https://marketplace.visualstudio.com/items?itemName=goessner.mdmath) | Optional — for session.md preview |

> **Tip:** Open this repo in VS Code — it will automatically recommend the right extensions.
>
> **No VS Code?** SocraTeX auto-generates `session.html` with KaTeX CDN. Just open it in any browser — it auto-refreshes every 3 seconds.

---

## License

**CC BY-NC-ND 4.0** — Free to use. No commercial use. No derivatives.

See [LICENSE](LICENSE) for details.
