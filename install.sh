#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE="$SCRIPT_DIR/.claude/commands"
TARGET="$HOME/.claude/commands/socratex"

if [ ! -d "$SOURCE" ]; then
    echo "Error: commands directory not found at $SOURCE"
    exit 1
fi

mkdir -p "$TARGET"
cp "$SOURCE"/*.md "$TARGET/"

echo "Socratex commands installed to $TARGET"
echo ""
echo "Available commands:"
for f in "$TARGET"/*.md; do
    name=$(basename "$f" .md)
    echo "  /socratex:$name"
done
echo ""
echo "Or use them without prefix when inside the socratex project directory."
