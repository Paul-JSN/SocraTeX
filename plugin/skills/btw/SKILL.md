---
name: btw
description: Use when the user asks a side question unrelated to the current study topic and needs an isolated answer without disrupting flow
---

Read `socratex.config.md` from the working directory. If not found, read `${CLAUDE_PLUGIN_ROOT}/socratex.config.md`. If neither exists, use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/core-rules.md` for Socratic method, LaTeX, subject detection, and session file rendering rules. Apply these throughout.

Do NOT write to the session file.

## Process

### Step 1: Freeze study state
Before answering, mentally note:
- Current subject and chapter being studied
- Last question asked or exercise in progress
- Where the session will resume after

### Step 2: Answer
Answer $ARGUMENTS concisely (3-5 sentences max). Use LaTeX for any math.

If the question connects to the current study topic, bridge briefly:
"This relates to what we're studying — [1-sentence connection]"

If the question is unrelated, answer it independently without referencing the study session.

### Step 3: Resume
State: "Back to our study session —" followed by a specific reminder of where we left off (the current topic, the last question asked, or the current exercise).

Resume exactly from that point. Do NOT let the side question change the study topic, difficulty, or flow.

---

## Anti-Patterns

### Losing Context After Return
After answering the side question, you MUST remind the student where they were. "Back to our study session" without context is useless.

- BAD: "Back to our study session —" (then silence)
- GOOD: "Back to our study session — we were working on the epsilon-delta proof for continuity. You were about to show that $\delta = \epsilon/3$ works."

### Over-Answering
This is a side question, not a study session. 3-5 sentences max. If the question deserves a full exploration, suggest: "That's a big topic — want to explore it with `/study [topic]` after we finish here?"

### Breaking Isolation
If the side question is actually related to the study topic, tell the student: "That's related to what we're studying — let me answer it in context instead of as a side question." Then answer within the study flow, not as a side question.
