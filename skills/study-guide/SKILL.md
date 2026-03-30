---
name: study-guide
description: Use when the user needs a structured study plan — concept hierarchy, formula sheet, study order, and time estimates. If an exam date is given, generates a realistic schedule that fits the available time
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto. Detect the subject from content and adapt the guide structure accordingly.

Parse $ARGUMENTS as a chapter range and optionally an exam date (e.g., "ch1-ch5 exam 4/15", "chapters 1-3 midterm next Monday", "sections 3.1-3.4 by Friday").

Find textbook .md files — check `textbook_path` from config first, then `books/`, then the working directory, or use files provided in the conversation. Read all .md files in that range.

Generate a structured study guide:

**1. Big Picture**
2-3 sentences: what this range covers and why it matters.

**2. Concept Hierarchy**
Outline format showing how topics build on each other. Indent sub-topics.

**3. Section Summaries**
One-line summary per section. Focus on the key takeaway.

**4. Formula Sheet**
All critical formulas in LaTeX $$...$$ blocks. Organized by topic. Designed to be printed/copied.

**5. Recommended Study Order**
Optimal sequence if topics have prerequisites. Flag which sections are most exam-relevant.

**6. Time Estimates & Schedule**

Calculate estimated study time per section based on concept density and difficulty.

**If an exam date is given**, generate a day-by-day schedule:

1. Calculate available days until exam
2. Calculate total estimated study hours needed
3. Compare the two:

   - **Time is sufficient** → spread study sessions evenly, include review days before the exam
   - **Time is tight but possible** → prioritize high-weight topics, compress low-priority sections, schedule longer daily sessions
   - **Time is NOT enough** → be honest. Do NOT compress estimates to make it fit. Instead:
     - Say clearly: "You need ~X hours but only have ~Y hours available"
     - Recommend increasing daily study hours (suggest specific amounts)
     - Create a triage plan: must-study (exam-critical), should-study (if time allows), skip (lowest priority)
     - Mark what to sacrifice and what to absolutely not skip

4. Include in the schedule:
   - Daily topics with time allocations
   - At least 1 review session before the exam
   - Buffer time for `/exercise` practice on weak areas
   - Final day: review `/flashcard` + `/mistake` analysis

**If no exam date is given**, just show per-section time estimates without scheduling.

Write the complete guide to `session.md` in the working directory (overwrite). Apply language/term settings.
