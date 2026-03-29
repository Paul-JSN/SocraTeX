---
name: socratex-btw
description: Use when the user asks a side question unrelated to the current study topic and needs an isolated answer without disrupting flow
---

This command provides context isolation. The side question must NOT affect the study flow.

Use the Agent tool to spawn a sub-agent that answers $ARGUMENTS independently. The sub-agent should:
- Give a concise answer (3-5 sentences max)
- Not reference or modify the current study context
- Not read or write session.md

After displaying the sub-agent's answer, explicitly state:

"Back to our study session --"

Then briefly remind the student where we left off (the current topic, the last question asked, or the current exercise) and resume exactly from that point.

Do NOT let the side question change the study topic, difficulty, or flow. The entire point is that $ARGUMENTS is handled in isolation.
