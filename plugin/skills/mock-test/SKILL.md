---
name: mock-test
description: Use when the user wants a practice exam with difficulty distribution, point values, time estimates, and hidden solutions
---

Read `SocraTeX.config.md` from the working directory. If not found, read `${CLAUDE_PLUGIN_ROOT}/SocraTeX.config.md`. If neither exists, use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/core-rules.md` for Socratic method, LaTeX, subject detection, and session file rendering rules. Apply these throughout.

Parse $ARGUMENTS as a chapter range. Find textbook .md files — check `textbook_path` from config first, then `books/`, then the working directory, or use files provided in the conversation. Read all exercises and theorems in that range.

Generate a mock exam:

**Structure:**
- Difficulty distribution: 30% easy, 50% medium, 20% hard
- Mix of: definitions, proofs/derivations, computations, and conceptual questions
- Match the textbook's exercise style and notation

**For each question:**
- Number and point value
- Full problem statement in LaTeX
- Estimated time (in minutes)

**At the end:**
- Total points and recommended time
- Topic coverage summary

**Solutions:** Do NOT show solutions initially. When the student says "solutions", "answers", or "show solutions", then reveal step-by-step solutions for each question.

Write the mock test to the session file (`session.html` if `render_mode: desktop`, `session.md` if `render_mode: vscode`) (overwrite for clean test format).

---

## Style Learning

Follow `${CLAUDE_PLUGIN_ROOT}/skills/_shared/style-analysis-guide.md` for full methodology.

When past exams or problem sets are available, match their exact format before defaulting to any standard structure:
- **Question count**: If past exams always have 6 questions, generate exactly 6 — not 10 or 15
- **Point distribution**: If past exams total 100 points with a 20/20/20/20/20 split, use that — not a difficulty-weighted split
- **Time allocation**: If past exams are 90 minutes, design for 90 minutes total — not 120
- **Question types**: If past exams are 60% computation, 30% proof, 10% conceptual, replicate that ratio
- **Difficulty distribution**: Do NOT default to 30/50/20 if actual exams use a different ratio. Analyze and match.
- **Formatting**: Match numbering style (1a, 1b vs i, ii, iii), sub-part structure, and how much setup/context each question provides
- **Notation**: Use the same variable names, derivative notation, and conventions as the textbook and past exams

When no past exam is available, use the 30/50/20 default but acknowledge: "I'm using a standard difficulty distribution. Share a past exam and I'll match its exact format."

---

## Exam Design Principles

These principles distinguish a useful mock test from a textbook exercise set:

**Transfer over Recall**
- Questions should NOT be textbook exercises with numbers changed. They should require applying concepts in slightly new contexts.
- At least one question should combine concepts from different sections within the range (e.g., using continuity to prove an inequality, or combining kinematics with energy conservation).

**Realistic Time Estimation**
- Estimate time by mentally working through the solution yourself. A question requiring 5 algebraic steps takes ~5 minutes, not 2.
- Include buffer time: total estimated time should be 80-90% of the exam duration, leaving time for review.
- Mark questions where time pressure is likely (complex computation, multi-part proofs).

**Point Values Reflect Difficulty**
- A routine computation should not be worth the same as a challenging proof.
- Partial credit structure should be clear: for a 10-point proof, indicate how points distribute across setup/key step/conclusion.
- Total points should match past exam conventions (typically 100, but some courses use 50 or 150).

**Progressive Difficulty**
- Start with 1-2 confidence-building questions (easy, high-value per minute).
- Middle section tests core competency (medium difficulty, bulk of points).
- End with 1-2 challenging questions that separate performance levels.

---

## Anti-Patterns

Avoid these when generating mock tests:

- **Textbook clones**: Questions that are barely modified textbook exercises test memorization, not understanding. Change the context, combine concepts, or require a strategy the student hasn't seen applied in exactly that way.
- **Unrealistic time estimates**: Do not assign 5 minutes to a question that requires setting up and solving a differential equation. Do not assign 20 minutes to a straightforward definition question. Work the solution mentally and estimate honestly.
- **Step-skipping solutions**: When solutions are revealed, every algebraic step matters. Students reviewing a mock test need to see WHERE they went wrong, which requires complete solutions. Show intermediate results, not just "by simplification, we get..."
- **Flat difficulty**: If you claim 30% easy / 50% medium / 20% hard, the questions must actually vary in difficulty. An "easy" question should be solvable in 2-3 minutes with direct application. A "hard" question should require insight or multi-step reasoning.
- **Type monotony**: A mock test that is all computation (or all proof) does not prepare students for real exams. Include definitions, conceptual reasoning, computation, and proof/derivation. Match the type distribution from past exams or use a balanced default.
- **Missing coverage**: Every major topic in the chapter range should appear in at least one question. If 4 chapters are covered and 3 of them have zero representation, the mock test has a coverage gap.

---

## Verification

After generating the mock test, run these checks before presenting it:

1. **Difficulty distribution check**: Count questions by difficulty. Does the actual ratio match the target (e.g., 30/50/20)? If 5 of 6 questions are medium, rebalance.
2. **Time budget check**: Sum all time estimates. Does the total fall within 80-100% of the intended exam duration? If it exceeds 100%, the test is too long. If it is below 70%, it is too short.
3. **Topic coverage check**: Map each question to its source chapter/section. Are all major topics in the range represented? Flag any chapters with zero questions.
4. **Question type check**: Tally question types (definition, proof, computation, conceptual). Does the mix match past exams or a reasonable default? A 100% computation test is a red flag.
5. **Solution completeness check**: When solutions are requested, verify each one shows every step. No "it follows that..." or "after simplification..." without showing the work.
6. **Point total check**: Do point values sum to the expected total? Are points proportional to difficulty and expected time?

---

## Integration

This skill connects to the exam prep flow (see `${CLAUDE_PLUGIN_ROOT}/skills/_shared/skill-integration-map.md`):

- **After completing the mock test**, suggest `/review-test` — the student can submit their answers for detailed analysis of what they got right/wrong and why
- **After completing the mock test**, suggest `/mistake [topic]` to identify error patterns across multiple attempts
- **Feeds from `/exam-prep`**: the formula cheat sheet and proof strategies from exam-prep serve as allowed reference material (or study material before attempting the mock)
- **Feeds from `/review-test`**: if a review test analysis exists with predicted topics, weight question selection toward those predictions
- **Feeds into `/study-guide`**: mock test performance informs which topics need more study time in the schedule
