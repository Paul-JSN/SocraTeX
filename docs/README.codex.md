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
   git clone https://github.com/Paul-JSN/SocraTeX.git ~/.codex/socratex
   ```

2. Copy skills into Codex's skill directory:
   ```bash
   cp -r ~/.codex/socratex/plugin/skills/* ~/.codex/skills/
   ```

3. Restart Codex.

### Windows

```powershell
git clone https://github.com/Paul-JSN/SocraTeX.git "$env:USERPROFILE\.codex\socratex"
Copy-Item -Recurse -Force "$env:USERPROFILE\.codex\socratex\plugin\skills\*" "$env:USERPROFILE\.codex\skills\"
```

## How It Works

Codex scans `~/.codex/skills/` at startup, parses SKILL.md frontmatter, and loads skills on demand.

After installation, 24 SocraTeX skill folders are copied directly into `~/.codex/skills/`. Codex discovers them automatically.

> **Note:** Codex does not follow symlinks for skill discovery ([known issue](https://github.com/openai/codex/issues/11314)). This is why skills are copied directly instead of symlinked.

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
| `/btw` | Side question |

## Textbook Files

Place your `.md` textbook files in the working directory. SocraTeX skills look for textbook content in:

1. `textbook_path` from `socratex.config.md` (if exists in working directory)
2. `books/` directory
3. Current working directory
4. Files provided in conversation

## Updating

```bash
cd ~/.codex/socratex && git pull
cp -r ~/.codex/socratex/plugin/skills/* ~/.codex/skills/
```

## Uninstalling

Remove SocraTeX skill folders from `~/.codex/skills/`:

```bash
cd ~/.codex/skills && rm -rf _shared btw compare derive exam-prep exercise feynman flashcard latex mistake mock-test prereq progress quiz relate review-test roadmap settings solve study study-guide summary translate visualize whatif
```

**Windows (PowerShell):**
```powershell
$skills = @("_shared","btw","compare","derive","exam-prep","exercise","feynman","flashcard","latex","mistake","mock-test","prereq","progress","quiz","relate","review-test","roadmap","settings","solve","study","study-guide","summary","translate","visualize","whatif")
foreach ($s in $skills) { Remove-Item -Recurse -Force "$env:USERPROFILE\.codex\skills\$s" -ErrorAction SilentlyContinue }
```

Optionally delete the clone: `rm -rf ~/.codex/socratex`

## Troubleshooting

### Skills not showing up

1. Verify skills exist: `ls ~/.codex/skills/study/SKILL.md`
2. Make sure files are real copies, not symlinks (Codex doesn't follow symlinks)
3. Restart Codex — skills are discovered at startup

### Windows path issues

Use PowerShell (not cmd). Ensure `$env:USERPROFILE\.codex\skills\` exists before copying.
