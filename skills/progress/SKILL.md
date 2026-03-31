---
name: progress
description: Use when the user wants to see study progress — chapters covered, weak areas, untouched material, and next recommendations
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Check the conversation history and any previous study sessions to determine:

**1. Chapters Covered**
List chapters/sections that have been studied with /study. Mark completion level:
- Studied (concepts reviewed)
- Exercised (problems attempted)
- Both

**2. Weak Areas**
Topics where the student struggled, needed many hints, or got answers wrong. Based on conversation evidence.

**3. Untouched Material**
Available chapters/sections that haven't been studied yet (based on textbook files found).

**4. Recommendations**
- Next chapter/section to study
- Topics to review (based on weak areas)
- Suggested exercises for reinforcement

Present as a clean, scannable summary. Use checkboxes for covered/uncovered sections.

## Anti-Patterns

### Fabricating Progress
Only report what actually happened in the conversation. If the student hasn't done any exercises, don't mark topics as "exercised." If there's no data, say: "No study sessions recorded yet. Start with `/study [chapter]` to begin tracking."

### No Actionable Recommendations
Progress without next steps is just a report card. Always end with: "Recommended next: `/study [specific topic]`" or "/exercise [weak area]`."

### Ignoring Weak Areas
If the student struggled with a topic, it MUST appear in the weak areas section. Don't omit it to avoid discouragement — the whole point is honest assessment.
