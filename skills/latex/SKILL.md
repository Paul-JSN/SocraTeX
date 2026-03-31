---
name: latex
description: Use when the user wants to toggle between LaTeX source code and plain-language explanation, or convert text to LaTeX notation
---

Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/core-rules.md` for Socratic method, LaTeX, subject detection, and session file rendering rules. Apply these throughout.

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

## Anti-Patterns

### Missing One Form
Always show BOTH the raw source and the rendered form. Showing only one defeats the purpose — the student needs to see the mapping between code and output.

### Not Explaining Notation
When converting plain text to LaTeX, explain non-obvious choices: "I used `\frac{}{}` instead of `/` for readability" or "The `\displaystyle` forces full-size rendering inline."

### Overcomplicating
Use the simplest LaTeX that produces the correct output. Don't use `\left( \right)` when `()` suffices. Don't use `\operatorname{}` when a standard command exists.
