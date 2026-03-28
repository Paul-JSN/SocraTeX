# Socratex on Claude.ai

## Setup

1. **Convert your textbook** using the converter CLI (see main README)
2. **Create a new Project** on Claude.ai
3. **Upload** the converted `.md` files to Project Knowledge
4. **Copy** the contents of `system-prompt.md` (below the `---` line) into Custom Instructions
5. Start chatting!

## Usage

Claude.ai doesn't have slash commands, so use natural language:

- "Let's study chapter 3" → starts Socratic study session
- "Give me practice problems on convergence" → guided exercises
- "Help me prep for the midterm, chapters 1-5" → full exam prep
- "Generate a mock test" → timed practice exam
- "Translate this to Korean" → translated with original terms
- "btw, what's a metric space?" → quick side answer, then back to topic

## Limitations vs Claude Code Version

| Feature | Claude.ai | Claude Code |
|---------|-----------|-------------|
| LaTeX rendering | Native | Via VS Code preview |
| Slash commands | Natural language | /study, /exercise, etc. |
| /btw isolation | Partial (manual) | Full (sub-agent) |
| Settings config | Via conversation | /settings command |
| Progress tracking | Manual | Automatic |
| session.md updates | N/A | Automatic |
