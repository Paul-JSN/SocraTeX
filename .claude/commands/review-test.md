---
description: Analyze a review test to predict exam patterns and generate targeted prep
---

Read `socratex.config.md` for language settings.

$ARGUMENTS should be a file path to a review test, or the student can paste the review test content directly.

If a file path is given, read that file. Otherwise, use the pasted content.

**Analysis Steps:**

1. **Question Type Breakdown** — Categorize each question (definition, proof, computation, conceptual, true/false).

2. **Topic Coverage** — Map each question to textbook chapters/sections. Identify heavily tested topics.

3. **Gap Analysis** — Compare review test topics against the full syllabus range. Flag topics NOT in the review that could still appear on the exam.

4. **Pattern Prediction** — Based on the review + textbook exercises, predict likely exam question types and topics. Assign confidence levels (high/medium/low).

5. **Targeted Mock Test** — Generate 5-8 practice questions focused on predicted exam topics, especially the gaps.

6. **Priority Study Plan** — Ordered list of what to study first, based on prediction confidence and the student's likely weak spots.

Write the full analysis to `session.md` (overwrite). All math in LaTeX.
