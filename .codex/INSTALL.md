# Installing SocraTeX for Codex

Enable SocraTeX skills in Codex via native skill discovery. Clone and symlink.

## Prerequisites

- Git

## Installation

1. **Clone the SocraTeX repository:**
   ```bash
   git clone https://github.com/Paul-JSN/SocraTeX.git ~/.codex/SocraTeX
   ```

2. **Create the skills symlink:**
   ```bash
   mkdir -p ~/.agents/skills
   ln -s ~/.codex/SocraTeX/plugin/skills ~/.agents/skills/SocraTeX
   ```

   **Windows (PowerShell):**
   ```powershell
   New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.agents\skills"
   cmd /c mklink /J "$env:USERPROFILE\.agents\skills\SocraTeX" "$env:USERPROFILE\.codex\SocraTeX\plugin\skills"
   ```

3. **Restart Codex** to discover skills.

## Verify

```bash
ls -la ~/.agents/skills/SocraTeX
```

You should see a symlink pointing to your SocraTeX skills directory with 24 skill folders + `_shared/`.

## Updating

```bash
cd ~/.codex/SocraTeX && git pull
```

Skills update instantly through the symlink.

## Uninstalling

```bash
rm ~/.agents/skills/SocraTeX
```

Optionally delete the clone: `rm -rf ~/.codex/SocraTeX`.
