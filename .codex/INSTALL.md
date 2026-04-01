# Installing SocraTeX for Codex

Enable SocraTeX skills in Codex via native skill discovery. Clone and copy skills into Codex's skill directory.

## Prerequisites

- Git

## Installation

1. **Clone the SocraTeX repository:**
   ```bash
   git clone https://github.com/Paul-JSN/SocraTeX.git ~/.codex/socratex
   ```

2. **Copy skills into Codex's skill directory:**
   ```bash
   cp -r ~/.codex/socratex/plugin/skills/* ~/.codex/skills/
   ```

   **Windows (PowerShell):**
   ```powershell
   Copy-Item -Recurse -Force "$env:USERPROFILE\.codex\socratex\plugin\skills\*" "$env:USERPROFILE\.codex\skills\"
   ```

3. **Restart Codex** to discover skills.

## Verify

```bash
ls ~/.codex/skills/study/SKILL.md
```

You should see the SKILL.md file. All 24 SocraTeX skill folders + `_shared/` should be in `~/.codex/skills/`.

## Updating

```bash
cd ~/.codex/socratex && git pull
cp -r ~/.codex/socratex/plugin/skills/* ~/.codex/skills/
```

**Windows (PowerShell):**
```powershell
cd "$env:USERPROFILE\.codex\socratex"; git pull
Copy-Item -Recurse -Force "$env:USERPROFILE\.codex\socratex\plugin\skills\*" "$env:USERPROFILE\.codex\skills\"
```

## Uninstalling

Remove each SocraTeX skill folder from `~/.codex/skills/`:

```bash
cd ~/.codex/skills && rm -rf _shared btw compare derive exam-prep exercise feynman flashcard latex mistake mock-test prereq progress quiz relate review-test roadmap settings solve study study-guide summary translate visualize whatif
```

Optionally delete the clone: `rm -rf ~/.codex/socratex`.
