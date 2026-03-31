---
name: study-guide
description: Use when the user needs a structured study plan — concept hierarchy, formula sheet, study order, and time estimates. If an exam date is given, generates a realistic schedule that fits the available time. Works with any STEM subject
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto. Detect the subject from content and adapt the guide structure accordingly.

Parse $ARGUMENTS as a chapter range and optionally an exam date (e.g., "ch1-ch5 exam 4/15", "chapters 1-3 midterm next Monday", "sections 3.1-3.4 by Friday").

Find textbook .md files — check `textbook_path` from config first, then `books/`, then the working directory, or use files provided in the conversation. Read all .md files in that range.

## When to Use

| Student says... | Use | Rationale |
|---|---|---|
| "Make me a study plan" / "How should I study for the exam?" | `/study-guide` | Structured plan with schedule |
| "What should I learn next?" / "What comes after this?" | `/roadmap` | Long-term learning path beyond current material |
| "Summarize what I studied" | `/summary` | Quick reference, not a plan |
| "What do I need to know before chapter 5?" | `/prereq` | Prerequisite check, not a study plan |

**Key distinction**: `/study-guide` creates a plan for material you're about to study. `/roadmap` plans beyond your current textbook. `/summary` condenses what you already studied.

## Guide Generation

**1. Big Picture**
2-3 sentences: what this range covers and why it matters. Adapt framing to subject — physics: what phenomena does this explain? Math: what problems can you now solve? Chemistry: what reactions does this cover?

**2. Concept Hierarchy**
Outline format showing how topics build on each other. Indent sub-topics. Mark prerequisites with arrows.

**3. Section Summaries**
One-line summary per section. Focus on the key takeaway, not a description.

**4. Formula Sheet**
All critical formulas in LaTeX $$...$$ blocks. Organized by topic. Subject-adapted:
- Physics: include units and common variants
- Chemistry: include conditions (temperature, pressure, catalyst)
- Math: include conditions for validity
- Statistics: include distribution assumptions

**5. Recommended Study Order**
Optimal sequence if topics have prerequisites. Flag which sections are most exam-relevant.

**6. Time Estimates & Schedule**

Calculate estimated study time per section based on concept density and difficulty.

**If an exam date is given**, generate a day-by-day schedule:

1. Calculate available days until exam
2. Calculate total estimated study hours needed
3. Compare the two:

   - **Time is sufficient** — spread study sessions evenly, include review days before the exam
   - **Time is tight but possible** — prioritize high-weight topics, compress low-priority sections, schedule longer daily sessions
   - **Time is NOT enough** — be honest. Do NOT compress estimates to make it fit. Instead:
     - Say clearly: "You need ~X hours but only have ~Y hours available"
     - Create a triage plan: must-study (exam-critical), should-study (if time allows), skip (lowest priority)
     - Recommend increasing daily study hours (suggest specific amounts)
     - Mark what to sacrifice and what to absolutely not skip

4. Include in the schedule:
   - Daily topics with time allocations
   - At least 1 review session before the exam
   - Buffer time for `/exercise` practice on weak areas
   - Final day: review `/flashcard` + `/mistake` analysis

**If no exam date is given**, just show per-section time estimates without scheduling.

Write the complete guide to the session file (per `render_mode` in config). Apply language/term settings.

---

## Anti-Patterns

### Unrealistic Time Estimates
The most dangerous anti-pattern. Students rely on these estimates to plan real study time.

- BAD: "Chapter 5: 30 minutes" for a chapter with 8 theorems and 15 exercises
- GOOD: Estimate based on concept count, difficulty, and whether the student has prerequisites

A rough heuristic:
- Simple definition/concept: 10-15 min to study + understand
- Theorem with proof: 20-30 min
- Computation technique: 15-20 min to learn + 20-30 min to practice
- Exercise set: 5-10 min per problem (varies by difficulty)

### Lying About Insufficient Time
If the student has 3 days for 40 hours of material, do NOT compress estimates to fit. The student needs honesty, not false hope. Present the triage plan and let them decide priorities.

### Generic Study Advice
- BAD: "Review the key formulas and practice problems"
- GOOD: "Study the epsilon-delta definition first (30 min), then work through 3 limit computation exercises (20 min each), then tackle the squeeze theorem (25 min)"

Every recommendation must be specific and actionable.

### Ignoring Prerequisites
If Section 3 requires Section 2, the study order must reflect this. Never present a flat list that implies sections can be studied in any order when they can't.

### All Study, No Practice
A study guide that only says "read section X" is incomplete. Each study block should include time for `/exercise` practice. A good ratio: 60% studying, 40% practicing.

## Verification

After the guide is generated:
- Check that total estimated hours are realistic for the content volume
- Verify that the study order respects prerequisite chains
- If an exam date was given, verify the schedule adds up to the available days
- Confirm formula sheet covers all critical formulas (spot-check against textbook)

## Integration

| Student state | Suggest |
|---|---|
| Guide generated, ready to start | `/study [first topic in the plan]` |
| Wants to check prerequisites first | `/prereq [first topic]` to verify readiness |
| Already studied, wants quick review | `/summary [range]` for a condensed reference |
| Exam is imminent | `/mock-test [range]` for timed practice |
| Wants flashcards for review | `/flashcard [range]` for memorization |
| Completed the plan, exam tomorrow | `/exam-prep [range]` for final review materials |

See `_shared/skill-integration-map.md` for the full skill flow.
