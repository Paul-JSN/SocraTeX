---
name: socratex-latex
description: Use when the user wants to toggle between LaTeX source code and plain-language explanation, or convert text to LaTeX notation
---

Handle $ARGUMENTS in one of three modes:

**LaTeX expression given** (contains `\`, `$`, `^`, `_`, `{`, or `}`):
- Explain what the expression means in plain language.
- Show the rendered form (in $$...$$ block) and the raw LaTeX source in a code block.

**"source" or empty**:
- Show the LaTeX source code for the most recent math output from this conversation.
- Present it in a fenced code block so the student can copy it.

**Plain text describing math** (e.g., "integral of x squared from 0 to 1"):
- Convert to proper LaTeX notation.
- Show both the LaTeX source (in a code block) and the rendered form (in $$...$$ block).
- Explain notation choices if non-obvious.

Always show both forms: the raw LaTeX code AND what it represents. This helps students learn to read and write LaTeX themselves.
