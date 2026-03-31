---
name: exam-prep
description: Use when the user needs comprehensive exam preparation materials for a chapter range — formulas, theorems, exercises, proof strategies, common mistakes
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Parse $ARGUMENTS as a chapter/section range (e.g., "ch1-ch5", "chapters 1 to 3", "sections 3.1-3.4"). Find textbook .md files — check `textbook_path` from config first, then `books/`, then the working directory, or use files provided in the conversation. Read all .md files in that range.

After reading, detect the subject from the content. If `subject` in config is not `auto`, use that instead. Adapt categories to the detected subject (e.g., for physics: include unit analysis and dimensional checks; for chemistry: include reaction mechanisms).

Generate these 6 categories, ALL with LaTeX:

**1. Formula Cheat Sheet**
Extract every important formula, equation, and identity. Organize by topic. Use $$...$$ blocks.

**2. Theorem Summary**
Each theorem with: statement, proof sketch (2-3 lines), and when to use it.

**3. Must-Do Exercises**
List exercises that cover core concepts. Prioritize those testing key theorems. Include exercise numbers and brief descriptions.

**4. Proof Strategies**
Common proof/derivation patterns in this range. Show the template structure. Adapt to subject: math (epsilon-delta, induction), physics (conservation laws, free-body diagrams), chemistry (stoichiometry, equilibrium), etc.

**5. Common Mistakes**
Pitfalls students frequently hit. "Do NOT confuse X with Y" format.

**6. Concept Map**
Text-based relationship diagram: definitions → theorems → applications → connections.

Write the complete output to `session.md` in the working directory (overwrite — this is a reference document, not incremental). Apply language/term settings throughout.

---

## Style Learning

Follow `_shared/style-analysis-guide.md` for full methodology.

When the student has provided past exams or problem sets, analyze their format before generating any of the 6 categories:
- Match the textbook's theorem numbering in the Theorem Summary (e.g., "Theorem 3.2.1" not "Theorem 1")
- Organize the Formula Cheat Sheet the way the textbook organizes topics — by chapter if the textbook is chapter-based, by theme if it cross-references
- Use the textbook's notation conventions throughout (check variable names, derivative notation, set notation)
- Reference actual textbook exercise numbers in Must-Do Exercises, not invented ones
- If a past exam is available, weight the 6 categories toward its emphasis (e.g., a proof-heavy exam means more detailed Proof Strategies)

When no style sample is available, acknowledge it: "I'm generating in a standard format. Share a past exam and I'll match that style."

---

## Anti-Patterns

Avoid these common quality failures:

**Formula Cheat Sheet**
- DO NOT list every formula from the chapters. Prioritize: formulas that appear in multiple exercises, formulas students frequently misremember, formulas that combine concepts. A cheat sheet with 50 formulas is useless — aim for 15-25 high-value ones, organized by when you need them.

**Theorem Summary**
- DO NOT write proof sketches that are just "apply the definition." A useful sketch shows the key insight: "Construct the subsequence by choosing $n_k$ such that $|a_{n_k} - L| < 1/k$, then use the Archimedean property."

**Proof Strategies**
- DO NOT give abstract advice like "use induction." Show the template:
  - "**Base case**: Verify $P(1)$ directly by computing..."
  - "**Inductive step**: Assume $P(k)$. To show $P(k+1)$, start from the left side and factor out..."
  - "**Key move**: The step where most students get stuck is [specific manipulation]"
- For physics: show the strategy template (draw FBD, choose coordinate system, apply Newton's 2nd law, solve)
- For chemistry: show the reaction analysis template (balance, identify limiting reagent, compute moles, convert)

**Common Mistakes**
- DO NOT write generic warnings like "be careful with signs" or "check your algebra." Write specific pitfalls:
  - "When differentiating $e^{f(x)}$, students forget the chain rule factor $f'(x)$, writing $e^{f(x)}$ instead of $f'(x) \cdot e^{f(x)}$"
  - "When applying L'Hopital's Rule, students forget to verify the $\frac{0}{0}$ or $\frac{\infty}{\infty}$ condition first"
  - "In free-body diagrams, students often forget the normal force when the surface is inclined"

**Concept Map**
- DO NOT produce a flat list of terms. Show connections with arrows and relationships:
  - "completeness $\Rightarrow$ every Cauchy sequence converges $\Rightarrow$ Bolzano-Weierstrass $\Rightarrow$ compactness"
  - Group by dependency: which definitions feed into which theorems, which theorems enable which applications

**Subject Adaptation**
- DO NOT use the same 6 categories for every subject without adaptation. Physics needs unit analysis and dimensional checks. Chemistry needs reaction mechanism summaries. Statistics needs distribution comparison tables. Add subject-specific content alongside the universal 6 categories.

---

## Output Quality Checklist

Before presenting the 6-part output, verify each section meets minimum quality:

- [ ] **Formula Cheat Sheet**: 15-25 formulas, organized by topic, not a raw dump. Each formula has a one-line "when to use" note.
- [ ] **Theorem Summary**: Each theorem has statement, genuine proof sketch (not just "by definition"), and a concrete use case.
- [ ] **Must-Do Exercises**: References actual textbook exercise numbers. Covers all major topics in the range. Includes brief reason why each is important.
- [ ] **Proof Strategies**: Shows concrete templates with blanks to fill in, not abstract advice. At least 3 distinct strategies.
- [ ] **Common Mistakes**: Each mistake is specific, includes the wrong answer students write and the correct version. Minimum 5 mistakes.
- [ ] **Concept Map**: Shows genuine relationships (implication, dependency, analogy), not a flat list. Has at least 2 levels of connection.

If any section fails its check, revise it before writing to the session file.

---

## Integration

This skill connects to the exam prep flow (see `_shared/skill-integration-map.md`):

- **After `/exam-prep`**, suggest `/mock-test [same range]` to practice under timed conditions
- **After `/exam-prep`**, suggest `/flashcard [same range]` to memorize key formulas and theorem statements
- **After `/exam-prep`**, suggest `/study-guide [same range] [exam date]` if the student has an upcoming exam and needs a day-by-day schedule
- **If `/mistake` data exists** for this student, cross-reference their personal error patterns with Common Mistakes — highlight the ones they are specifically prone to
- **Feeds into `/mock-test`**: the formula sheet and proof strategies become reference material during mock test review
- **Feeds from `/review-test`**: if a review test analysis exists, weight the 6 categories toward predicted exam topics
