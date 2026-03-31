---
name: btw
description: Use when the user asks a side question unrelated to the current study topic and needs an isolated answer without disrupting flow
---

This skill provides context isolation. The side question must NOT affect the study flow.

Use the Agent tool to spawn a sub-agent that answers $ARGUMENTS independently. The sub-agent should:
- Give a concise answer (3-5 sentences max)
- Not reference or modify the current study context
- Not read or write session.md

After displaying the sub-agent's answer, explicitly state:

"Back to our study session --"

Then briefly remind the student where we left off (the current topic, the last question asked, or the current exercise) and resume exactly from that point.

Do NOT let the side question change the study topic, difficulty, or flow. The entire point is that $ARGUMENTS is handled in isolation.

## Anti-Patterns

### Losing Context After Return
After answering the side question, you MUST remind the student where they were. "Back to our study session" without context is useless.

- BAD: "Back to our study session —" (then silence)
- GOOD: "Back to our study session — we were working on the epsilon-delta proof for continuity. You were about to show that $\delta = \epsilon/3$ works."

### Over-Answering
This is a side question, not a study session. 3-5 sentences max. If the question deserves a full exploration, suggest: "That's a big topic — want to explore it with `/study [topic]` after we finish here?"

### Breaking Isolation
The sub-agent must not read or reference the study session context. If the side question is actually related to the study topic, tell the student: "That's related to what we're studying — let me answer it in context instead of as a side question."
