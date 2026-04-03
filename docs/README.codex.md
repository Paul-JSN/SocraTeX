# SocraTeX for Codex

Guide for using SocraTeX with OpenAI Codex via native skill discovery.

## Quick Install

Tell Codex:

```
Fetch and follow instructions from https://raw.githubusercontent.com/Paul-JSN/SocraTeX/refs/heads/main/.codex/INSTALL.md
```

## Manual Installation

### Prerequisites

- OpenAI Codex CLI
- Git

### Steps

1. Clone the repo:
   ```bash
   git clone https://github.com/Paul-JSN/SocraTeX.git ~/.codex/SocraTeX
   ```

2. Create the skills symlink:
   ```bash
   mkdir -p ~/.agents/skills
   ln -s ~/.codex/SocraTeX/plugin/skills ~/.agents/skills/SocraTeX
   ```

3. Restart Codex.

### Windows

Use a junction instead of a symlink (works without Developer Mode):

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.agents\skills"
cmd /c mklink /J "$env:USERPROFILE\.agents\skills\SocraTeX" "$env:USERPROFILE\.codex\SocraTeX\plugin\skills"
```

## How It Works

Codex has native skill discovery — it scans `~/.agents/skills/` at startup, parses SKILL.md frontmatter, and loads skills on demand. SocraTeX skills are made visible through a single symlink:

```
~/.agents/skills/SocraTeX/ → ~/.codex/SocraTeX/plugin/skills/
```

24 skills are discovered automatically. Codex activates them when the task matches a skill's description.

## Skills Compatibility

### Works great in Codex (single-output)

These skills generate content without needing student interaction:

| Skill | What it does |
|-------|-------------|
| `/solve` | Full worked solution |
| `/derive` | Step-by-step derivation |
| `/summary` | Concise topic summary |
| `/flashcard` | Q&A flashcards with Anki export |
| `/exam-prep` | Comprehensive exam prep materials |
| `/mock-test` | Full practice exam |
| `/study-guide` | Study plan with schedule |
| `/compare` | Side-by-side concept comparison |
| `/relate` | Cross-discipline connection map |
| `/visualize` | ASCII diagrams |
| `/roadmap` | Long-term learning path |
| `/translate` | Translate content preserving LaTeX |
| `/latex` | LaTeX conversion/explanation |
| `/mistake` | Error pattern analysis |
| `/review-test` | Past exam analysis |

### Interactive (limited in Codex)

These skills use Socratic dialogue — they ask questions and wait for student responses. They work in Codex but behave more like single-turn outputs:

| Skill | What it does |
|-------|-------------|
| `/study` | Socratic walkthrough (asks guiding questions) |
| `/exercise` | Guided practice with hints |
| `/feynman` | Student explains concept back |
| `/prereq` | Prerequisite readiness check |
| `/quiz` | Interactive quiz with scoring |
| `/whatif` | Hypothetical exploration |
| `/sideq` | Side question |

## Textbook Files

Place your `.md` textbook files in the working directory. SocraTeX skills look for textbook content in:

1. `textbook_path` from `SocraTeX.config.md` (if exists in working directory)
2. `books/` directory
3. Current working directory
4. Files provided in conversation

## Updating

```bash
cd ~/.codex/SocraTeX && git pull
```

Skills update instantly through the symlink.

## Uninstalling

```bash
rm ~/.agents/skills/SocraTeX
```

**Windows (PowerShell):**
```powershell
Remove-Item "$env:USERPROFILE\.agents\skills\SocraTeX"
```

Optionally delete the clone: `rm -rf ~/.codex/SocraTeX`

## Troubleshooting

### Skills not showing up

1. Verify the symlink: `ls -la ~/.agents/skills/SocraTeX`
2. Check skills exist: `ls ~/.codex/SocraTeX/plugin/skills`
3. Restart Codex — skills are discovered at startup

### Windows junction issues

Junctions normally work without special permissions. If creation fails, try running PowerShell as administrator.
