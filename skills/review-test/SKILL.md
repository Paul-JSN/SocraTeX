---
name: review-test
description: Use when the user has a review test to analyze for predicting exam patterns, finding coverage gaps, and generating targeted practice
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto. Detect the subject from the review test content and adapt analysis accordingly.

$ARGUMENTS should be a file path to a review test, or the student can paste the review test content directly.

If a file path is given, read that file. Otherwise, use the pasted content.

**Analysis Steps:**

1. **Question Type Breakdown** — Categorize each question (definition, proof, computation, conceptual, true/false).

2. **Topic Coverage** — Map each question to textbook chapters/sections. Identify heavily tested topics.

3. **Gap Analysis** — Compare review test topics against the full syllabus range. Flag topics NOT in the review that could still appear on the exam.

4. **Pattern Prediction** — Based on the review + textbook exercises, predict likely exam question types and topics. Assign confidence levels (high/medium/low).

5. **Targeted Mock Test** — Generate 5-8 practice questions focused on predicted exam topics, especially the gaps.

6. **Priority Study Plan** — Ordered list of what to study first, based on prediction confidence and the student's likely weak spots.

Write the full analysis to `session.md` in the working directory (overwrite). All math in LaTeX.

---

## Pattern Prediction Methodology

How to systematically predict exam questions from a review test:

**High-Probability Topics (80%+ confidence)**
- Topics that appear directly in the review test are very likely on the exam. Professors use reviews to signal what matters.
- If a topic appears in multiple review questions, it is almost certainly on the exam in some form.
- The question TYPE used in the review (proof, computation, conceptual) likely mirrors the exam. If the review asks students to prove a convergence theorem, expect a similar proof question.

**Medium-Probability Topics (50-70% confidence)**
- Topics that are heavily covered in the textbook but deliberately ABSENT from the review. Professors sometimes omit topics from the review specifically because they plan to test them — the review covers what students should already know, and the exam adds what they need to prove they know.
- Topics the professor emphasized in lectures (if the student can report this) but that do not appear in the review.
- Variations on review topics: if the review tests convergence of sequences, the exam may test convergence of series (same concept, different application).

**Lower-Probability Topics (20-40% confidence)**
- Topics mentioned briefly in the textbook but not emphasized in exercises.
- Topics from early chapters that the review seems to assume as prerequisites — they may appear as part of a multi-step problem.

**Structural Predictions**
- The number of questions on the exam is often close to the number on the review, or a predictable multiple (review has 5, exam has 8-10).
- Difficulty progression in the review hints at exam difficulty. If the review ends with a hard proof, expect the exam to also include a challenging question.
- Time-per-question in the review (estimated from complexity) predicts exam pacing.

**Confidence Calibration**
- With 1 review test: predictions are directional, not precise. Flag this uncertainty.
- With 2+ review tests or past exams: patterns become much more reliable. Cross-reference for recurring topics.
- Always include a "surprise factor" section: topics the student should prepare for even though they are not predicted, because professors occasionally add unexpected questions.

---

## Anti-Patterns

Avoid these when analyzing review tests:

- **Over-predicting from small samples**: A 5-question review test does not contain enough signal to predict a 30-question exam with precision. Acknowledge the uncertainty. Say "these topics are likely important" not "these topics WILL be on the exam."
- **Assuming the exam mirrors the review**: Professors often deliberately make the exam different from the review to test genuine understanding. The review shows the floor of what is expected, not the ceiling.
- **Ignoring gap topics**: Topics that are conspicuously absent from the review deserve special attention, not dismissal. If Chapter 5 is entirely missing from a review covering Chapters 1-6, that is a signal, not an oversight. Flag it prominently in the Gap Analysis.
- **Generating weak targeted questions**: The practice questions in Step 5 (Targeted Mock Test) should match predicted exam difficulty. If the review test has challenging proofs, do not generate easy fill-in-the-blank questions as "targeted practice." Match the predicted difficulty level.
- **Flat confidence levels**: Do not assign "medium confidence" to everything. Differentiate clearly. Some predictions are strong (topic appears 3 times in review), some are speculative (topic is absent but important). The student needs to know the difference to allocate study time.
- **Ignoring question type patterns**: If the review is 100% computation, do not predict that the exam will suddenly require proofs (unless there is external evidence). Question type distribution in the review is one of the strongest predictors.

---

## Integration

This skill connects to the exam prep flow (see `_shared/skill-integration-map.md`):

- **After `/review-test`**, suggest `/exam-prep [same range]` for comprehensive preparation materials — the prediction data from review-test analysis should inform which of the 6 exam-prep categories to emphasize
- **After `/review-test`**, suggest `/mock-test [same range]` to generate a practice exam weighted toward predicted topics, especially the gap topics identified in the analysis
- **After `/review-test`**, suggest `/study-guide [same range] [exam date]` if the student has time before the exam — the priority study plan from review-test feeds directly into scheduling
- **Feeds into `/mistake`**: if the student attempts the targeted mock questions and makes errors, `/mistake` can analyze their specific error patterns on predicted exam topics
- **Feeds from `/mock-test`**: if the student has already taken a mock test, their performance data helps calibrate which gap topics are genuinely weak vs already mastered
