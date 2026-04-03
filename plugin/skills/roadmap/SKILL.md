---
name: roadmap
description: Use when the user wants a long-term learning path beyond the current textbook — what to study next, prerequisite chains across courses, career-oriented study paths. Goes beyond textbook scope using general knowledge
---

Read `SocraTeX.config.md` from the working directory. If not found, read `${CLAUDE_PLUGIN_ROOT}/SocraTeX.config.md`. If neither exists, use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/core-rules.md` for Socratic method, LaTeX, subject detection, and session file rendering rules. Apply these throughout.

Parse $ARGUMENTS to identify the goal. This can be:
- A subject area: "linear algebra", "quantum mechanics", "machine learning"
- A career goal: "data scientist", "quant researcher", "embedded systems engineer"
- A "what's next" question: "what after real analysis?", "I finished this textbook, now what?"
- A broad field: "pure math", "applied physics", "bioinformatics"

## When to Use

| Student says... | Use | Rationale |
|---|---|---|
| "What should I learn after this?" / "I want to become a [career]" | `/roadmap` | Long-term path beyond current material |
| "Make me a study plan for this exam" | `/study-guide` | Short-term plan within current textbook |
| "What do I need before chapter 5?" | `/prereq` | Prerequisite check for a specific topic |
| "Summarize what I covered" | `/summary` | Backward-looking reference, not forward planning |

**Key distinction**: `/roadmap` is long-term and goes beyond the textbook. `/study-guide` is short-term and stays within the textbook. `/prereq` checks readiness for a specific topic.

## Roadmap Generation

**Important:** This skill goes beyond textbook content. It draws on general knowledge about academic curricula and career paths. Acknowledge this: "This roadmap is based on general academic structure, not your specific textbook."

### 1. Where You Are Now
Based on the textbook content and study history, summarize the student's current level. What have they covered? What's their foundation?

### 2. The Roadmap
Generate a structured learning path as a tree:

```
Current Level: [what they know]
|
+-- Next Step: [immediate next topic]
|   +-- Why: [why this comes next]
|   +-- Resources: [standard textbook recommendations]
|
+-- Then: [following topic]
|   +-- Why: [builds on previous]
|   +-- Resources: [textbook recommendations]
|
+-- Advanced: [deeper topics]
|   +-- ...
|
+-- Specialization Options:
    +-- Path A: [e.g., pure math track]
    +-- Path B: [e.g., applied/computational track]
    +-- Path C: [e.g., interdisciplinary track]
```

### 3. Prerequisites Map
For each step in the roadmap, list what it requires. Help the student see which paths are open now vs later.

### 4. Time Estimates
Rough time estimates per stage (e.g., "1 semester", "3-6 months self-study"). Be realistic — see Anti-Patterns.

### 5. Career Connections (if a career goal was given)
Map the roadmap to career milestones: "After [stage], you can apply for [role]" or "This is the minimum for [field]."

### 6. Recommended Starting Point
Based on the student's current level, recommend exactly where to begin: "Start with [topic]. When you're ready, run `/study [topic]` or `/prereq [next topic]` to check."

Write the roadmap to the session file (per `render_mode` in config). Use LaTeX for any formulas referenced.

---

## Anti-Patterns

### Unrealistic Time Estimates
- BAD: "Learn quantum field theory in 2 months"
- GOOD: "QFT typically takes 1-2 semesters with strong prerequisites in quantum mechanics and special relativity"

Err on the side of longer estimates. Students can always move faster, but underestimating leads to frustration.

### Too Many Paths Without Guidance
Presenting 5+ specialization paths without helping the student choose is overwhelming.

- BAD: "Here are 8 possible paths you could take"
- GOOD: "Based on your interest in [X], Path B is most relevant. Path A is an alternative if you prefer [Y]."

Always recommend a default path. Other paths are options, not requirements.

### Ignoring Prerequisites
Every step must list what it requires. Never suggest "learn topology" without checking whether the student has real analysis foundations.

### Generic Textbook Lists
- BAD: "Read any linear algebra textbook"
- GOOD: "Axler's *Linear Algebra Done Right* (proof-focused) or Strang's *Introduction to Linear Algebra* (computation-focused, with MIT OCW lectures)"

Recommend specific resources with a note about their style and level.

### Treating All Students the Same
A student who finished Calculus I has a different roadmap than one who finished Real Analysis. Calibrate the starting point to what they actually know, not what's typical.

## Verification

After generating the roadmap:
- Verify every prerequisite chain is valid (no step requires something not yet covered)
- Check that time estimates are consistent (later stages shouldn't be shorter than earlier ones unless they truly are)
- Confirm that the recommended starting point matches the student's actual level
- If a career goal was given, verify the roadmap actually leads to that career

## Integration

| Student state | Suggest |
|---|---|
| Roadmap generated, ready to start | `/study [first topic]` or `/prereq [first topic]` to check readiness |
| Wants to verify current level | `/quiz [current topics]` or `/feynman [key concept]` |
| Needs to fill prerequisite gaps | `/study [prerequisite]` before advancing |
| Wants to explore a specific branch | `/study [branch topic]` or ask for a more detailed roadmap of that branch |
| Finished a roadmap stage | Update the roadmap: `/roadmap [same goal]` to recalibrate |

See `${CLAUDE_PLUGIN_ROOT}/skills/_shared/skill-integration-map.md` for the full skill flow.
