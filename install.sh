#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE="$SCRIPT_DIR/skills"
TARGET="$HOME/.claude/skills"

if [ ! -d "$SOURCE" ]; then
    echo "Error: skills directory not found at $SOURCE"
    exit 1
fi

# Copy each skill directory (SKILL.md + supporting files)
for skill_dir in "$SOURCE"/*/; do
    name=$(basename "$skill_dir")
    # Skip _shared directory — handled separately
    [ "$name" = "_shared" ] && continue
    dest="$TARGET/socratex-$name"
    mkdir -p "$dest"
    cp -r "$skill_dir"* "$dest/"
done

# Copy _shared resources
if [ -d "$SOURCE/_shared" ]; then
    dest="$TARGET/socratex-_shared"
    mkdir -p "$dest"
    cp -r "$SOURCE/_shared/"* "$dest/"
fi

echo "SocraTeX skills installed to $TARGET"
echo ""
echo "Available skills:"
for skill_dir in "$TARGET"/socratex-*/; do
    [ ! -d "$skill_dir" ] && continue
    name=$(basename "$skill_dir" | sed 's/^socratex-//')
    [ "$name" = "_shared" ] && continue
    echo "  /socratex-$name"
done
echo ""
echo "Or use them without prefix when inside the SocraTeX project directory."
