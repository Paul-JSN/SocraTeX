#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE="$SCRIPT_DIR/.claude/skills"
TARGET="$HOME/.claude/skills"

if [ ! -d "$SOURCE" ]; then
    echo "Error: skills directory not found at $SOURCE"
    exit 1
fi

for skill_dir in "$SOURCE"/*/; do
    name=$(basename "$skill_dir")
    dest="$TARGET/socratex-$name"
    mkdir -p "$dest"
    cp "$skill_dir"SKILL.md "$dest/"
done

echo "SocraTeX skills installed to $TARGET"
echo ""
echo "Available skills:"
for skill_dir in "$TARGET"/socratex-*/; do
    name=$(basename "$skill_dir" | sed 's/^socratex-//')
    echo "  /socratex-$name"
done
echo ""
echo "Or use them without prefix when inside the SocraTeX project directory."
