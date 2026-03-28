<div align="center">

# SocraTeX

### Socratic + LaTeX

**Study any math textbook with Claude.**

Drop a PDF. Get structured Markdown. Start a Socratic dialogue.

---

<img src="https://img.shields.io/badge/license-CC--BY--NC--ND--4.0-blue" alt="License" />
<img src="https://img.shields.io/badge/python-3.10+-yellow" alt="Python" />
<img src="https://img.shields.io/badge/platform-Claude_Code_%7C_Claude.ai-blueviolet" alt="Platform" />

[한국어](docs/README_ko.md) | [中文](docs/README_zh.md) | [日本語](docs/README_ja.md) | [Espanol](docs/README_es.md)

</div>

---

## What is SocraTeX?

SocraTeX turns any math textbook PDF into an interactive study system powered by Claude.

```
PDF  ──>  MinerU API  ──>  Structured .md  ──>  Claude teaches you
                                                  (Socratic method)
```

**No direct answers.** Claude guides you with questions, hints, and counterexamples until you discover the solution yourself. All math is rendered in beautiful LaTeX.

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
| `/latex [expr]` | LaTeX toggle — explain a formula, get copyable source, or convert plain text to LaTeX |
| `/translate [lang]` | Translate with math — preserves all LaTeX, configurable bilingual term display |
| `/proof [theorem]` | Proof mode — write your proof line by line, Claude verifies each step's logic. Works for theorems, formulas, identities |
| `/compare [A vs B]` | Side-by-side comparison — definitions, differences, similarities, counterexamples, when to use which |
| `/visualize [concept]` | ASCII visualization — function graphs, set diagrams, number lines, epsilon-delta illustrations |
| `/quiz [range]` | Quick 10-question quiz — True/False, fill-in-the-blank, definition matching. Fast review, instant scoring |
| `/btw [question]` | Side question — answered in isolation via sub-agent, resumes study flow automatically |
| `/settings [k=v]` | Configuration — language, difficulty, term annotations, hint count |
| `/progress` | Progress tracker — chapters covered, weak areas, next recommendations |

---

## Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/Paul-JSN/SocraTeX.git
cd SocraTeX
pip install -r requirements.txt
```

### 2. Set Up MinerU API Token

Get your token at [mineru.net/apiManage](https://mineru.net/apiManage):

```bash
cp .env.example .env
# Edit .env → add your MINERU_API_TOKEN
```

### 3. Convert Your Textbook

```bash
python -m converter path/to/textbook.pdf
```

Output: `books/your-textbook/index.md` + per-chapter `.md` files with preserved LaTeX.

### 4. Start Studying

<table>
<tr>
<th>Claude Code (VS Code) — Full features</th>
<th>Claude.ai — Quick start</th>
</tr>
<tr>
<td>

```bash
cd SocraTeX
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

### 5. Install Globally (Optional)

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

**Left**: Socratic dialogue with Claude &nbsp;&nbsp;|&nbsp;&nbsp; **Right**: Rendered LaTeX via `session.md`

All study commands automatically update `session.md` so VS Code's Markdown Preview stays in sync.

**Not using VS Code?** SocraTeX also generates `session.html` with KaTeX CDN — just open it in any browser. It auto-refreshes every 3 seconds as you study.

---

## Skills-Only Mode (No Converter Needed)

Already have `.md` files? Skip the PDF converter entirely:

```bash
mkdir -p books/my-textbook
# Place your .md files in books/my-textbook/
# Create an index.md with links to each chapter
```

The slash commands work with any Markdown files containing LaTeX notation. The MinerU converter is just one way to get those files.

---

## Configuration

Edit `socratex.config.md` directly or use `/settings`:

```yaml
study_language: en            # Any ISO 639-1 code (en, ko, ja, zh, es, fr, de, ...)
show_original_terms: false    # Show original terms alongside translations
term_format: "translated (original)"   # Options: "translated (original)" | "original → translated" | "translated [original]"
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

## Requirements

| Requirement | Notes |
|-------------|-------|
| Python 3.10+ | For the PDF converter |
| [MinerU API token](https://mineru.net/apiManage) | Free tier available |
| Claude Code or Claude.ai | Any active plan |
| VS Code + [Markdown+Math](https://marketplace.visualstudio.com/items?itemName=goessner.mdmath) | Recommended for LaTeX rendering |

> **Tip:** Open this repo in VS Code — it will automatically recommend the right extensions (`.vscode/extensions.json`).

---

## Project Structure

```
SocraTeX/
├── converter/           # PDF → Markdown (Python CLI)
├── .claude/commands/    # 11 slash commands for Claude Code
├── claude-ai/           # System prompt for Claude.ai
├── books/               # Your converted textbooks (gitignored)
├── socratex.config.md   # User settings
└── CLAUDE.md            # Rules for Claude (Socratic method, LaTeX, etc.)
```

---

## License

**CC BY-NC-ND 4.0** — Free to use. No commercial use. No derivatives.

See [LICENSE](LICENSE) for details.

