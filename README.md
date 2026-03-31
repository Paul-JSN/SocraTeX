<div align="center">

# SocraTeX

### Socratic + LaTeX

**Your AI study partner for any STEM textbook.**

Drop your `.md` files — start a Socratic dialogue. Never get direct answers. All math in LaTeX.

---

<img src="https://img.shields.io/badge/license-CC--BY--NC--ND--4.0-blue" alt="License" />
<img src="https://img.shields.io/badge/setup-zero--dependency-brightgreen" alt="Zero Dependency" />
<img src="https://img.shields.io/badge/skills-24-orange" alt="24 Skills" />
<img src="https://img.shields.io/badge/subjects-math_%7C_physics_%7C_chemistry_%7C_stats_%7C_engineering_%7C_economics-blueviolet" alt="Subjects" />

[한국어](docs/README_ko.md) | [中文](docs/README_zh.md) | [日本語](docs/README_ja.md) | [Espanol](docs/README_es.md)

</div>

---

## What is SocraTeX?

24 skills that turn Claude into a Socratic STEM tutor. No setup, no dependencies — just Markdown textbooks with LaTeX.

```
Your .md textbook  ──>  Claude reads it  ──>  Detects subject  ──>  Socratic dialogue
                                                                     (never gives direct answers)
```

**No direct answers.** Claude guides you with questions, hints, and counterexamples until you discover the solution yourself.

**Any STEM subject.** SocraTeX auto-detects whether you're studying math, physics, chemistry, statistics, engineering, or economics — and adapts its teaching style accordingly.

> **Have a PDF?** Use [MinerU](https://mineru.net) (Precision mode, `vlm` model) to convert PDF to Markdown with LaTeX preserved. Free tier available.

---

## Quick Start

### Option A: Plugin Install (Claude Code)

```
/plugin install socratex
```

### Option B: Clone & Use

```bash
git clone https://github.com/Paul-JSN/SocraTeX.git
cd SocraTeX
```

Add your textbook files to `books/` and start:

```
/study ch01
```

### Option C: Claude.ai

1. Create a **Project** on claude.ai
2. Upload `.md` textbook files to **Project Knowledge**
3. Paste contents of `claude-ai/system-prompt.md` into **Custom Instructions**
4. Chat: *"Let's study chapter 3"*

---

## Skills (24)

### Study

| Skill | What it does |
|-------|-------------|
| `/study [chapter]` | Socratic walkthrough — reads the chapter, asks guiding questions |
| `/exercise [topic]` | Guided practice — incremental hints, tracks attempts |
| `/solve [problem]` | Worked solution — Claude demonstrates the full solving process |
| `/derive [formula]` | Step-by-step derivation of formulas, laws, proofs |
| `/feynman [concept]` | You explain the concept to Claude — Claude probes your understanding |

### Explore

| Skill | What it does |
|-------|-------------|
| `/whatif [scenario]` | "What if gravity doubled?" — hypothetical exploration (context-isolated) |
| `/compare [A vs B]` | Side-by-side comparison — definitions, differences, counterexamples |
| `/relate [concept]` | Cross-discipline connections — how concepts link across fields |
| `/visualize [concept]` | ASCII diagrams — graphs, circuits, force diagrams, molecular structures |

### Test Prep

| Skill | What it does |
|-------|-------------|
| `/quiz [range]` | Quick 10-question quiz — T/F, fill-in-blank, matching |
| `/mock-test [range]` | Full mock exam — difficulty distribution, point values, hidden solutions |
| `/exam-prep [range]` | Comprehensive prep — formulas, theorems, exercises, strategies, common mistakes |
| `/review-test [file]` | Analyze a past test — predict exam patterns, generate targeted practice |

### Review & Plan

| Skill | What it does |
|-------|-------------|
| `/study-guide [range] [exam date]` | Study plan — concept hierarchy, formula sheet. With exam date: day-by-day schedule |
| `/flashcard [topic]` | Q&A flashcards with Anki-importable export |
| `/summary [range]` | Concise summary — key concepts, formulas, takeaways |
| `/prereq [topic]` | Prerequisite check — tests readiness before studying a new topic |
| `/mistake [topic]` | Mistake analysis — scans your chat history for error patterns + gap analysis |
| `/roadmap [goal]` | Long-term learning path — what to study next, career connections |

### Utility

| Skill | What it does |
|-------|-------------|
| `/translate [lang]` | Translate content — preserves all LaTeX, bilingual term display |
| `/latex [expr]` | LaTeX toggle — explain a formula, get source, or convert text to LaTeX |
| `/progress` | Progress tracker — chapters covered, weak areas, recommendations |
| `/settings [k=v]` | Configuration — language, difficulty, subject, hints, render mode |
| `/btw [question]` | Side question — answered in isolation, resumes study flow |

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
│  │  think this      │   │  For all epsilon > 0,    │ │
│  │  means           │   │  there exists N such     │ │
│  │  physically?     │   │  that n >= N implies     │ │
│  │                  │   │  |a_n - L| < epsilon     │ │
│  │  > It means...   │   │                          │ │
│  └──────────────────┘   └──────────────────────────┘ │
└──────────────────────────────────────────────────────┘
```

**Left**: Socratic dialogue &nbsp;|&nbsp; **Right**: Rendered LaTeX session file

Two render modes:

| Mode | Output | Best for |
|------|--------|----------|
| `desktop` (default) | `session.html` — auto-opens in browser, KaTeX, 3s auto-refresh | Claude Code Desktop / CLI |
| `vscode` | `session.md` — VS Code Markdown Preview | VS Code users |

Change with `/settings render=vscode` or `/settings render=desktop`.

---

## Configuration

Edit `socratex.config.md` directly or use `/settings`:

```yaml
study_language: en            # Any ISO 639-1 code (en, ko, ja, zh, es, fr, de, ...)
show_original_terms: false    # Show original terms alongside translations
term_format: "translated (original)"
subject: auto                 # auto | math | physics | chemistry | statistics | economics | engineering
render_mode: desktop          # desktop (browser) | vscode (Markdown Preview)
difficulty: adaptive          # easy | medium | hard | adaptive
hints_before_answer: 3        # Minimum hints before revealing solutions
textbook_path:                # Path to textbook .md files (auto-detected if empty)
```

**Examples:**
```
/settings lang=ko terms=on        →  수렴 (convergence)
/settings subject=physics         →  force subject to physics mode
/settings difficulty=hard hints=5 →  harder, more hints before answer
```

---

## Subject Auto-Detection

SocraTeX detects the subject from your textbook content automatically:

| Subject | Adapts how |
|---------|-----------|
| **Math** | Rigorous proofs, epsilon-delta, theorem-definition-proof structure |
| **Physics** | Derivations, units, dimensional analysis, physical intuition |
| **Chemistry** | Reaction equations, equilibria, molecular notation |
| **Statistics** | Distributions, hypothesis testing, confidence intervals |
| **Economics** | Optimization, equilibrium models, marginal analysis |
| **Engineering** | System modeling, transfer functions, circuit analysis |

Override with `/settings subject=physics` or let it auto-detect (`subject=auto`).

---

## Project Structure

```
SocraTeX/
├── .claude-plugin/      # Plugin metadata (plugin.json, marketplace.json)
├── skills/              # 24 skills (SKILL.md format)
├── claude-ai/           # System prompt for Claude.ai users
├── CLAUDE.md            # Core rules (Socratic method, LaTeX, subject detection)
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

> **No VS Code?** SocraTeX generates `session.html` with KaTeX CDN. Open in any browser — auto-refreshes every 3 seconds.

---

## License

**CC BY-NC-ND 4.0** — Free to use. No commercial use. No derivatives.

See [LICENSE](LICENSE) for details.
