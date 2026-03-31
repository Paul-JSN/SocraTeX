# Style Analysis Guide

How to analyze and replicate the style of a textbook, problem set, or past exam. Used by skills that generate problems or prep materials (exercise, mock-test, exam-prep, quiz).

## When to Analyze Style

1. **Always from textbook** — when reading textbook exercises, automatically note their style
2. **From user samples** — when the student provides a past exam, problem set, or homework, analyze it explicitly before generating output

## What to Analyze

### Problem Format
- How are problems numbered? (1.1, 1.2... vs Problem 1, Problem 2... vs Exercise 3.4.1)
- Are problems grouped by topic or mixed?
- Do problems have sub-parts (a, b, c)?
- Are hints or partial answers given?
- Is there a difficulty indicator (★, ★★, ★★★)?

### Question Types
- What mix of question types? Count them:
  - Definitions ("Define..." / "State the theorem...")
  - Proof/Derivation ("Prove that..." / "Show that..." / "Derive...")
  - Computation ("Calculate..." / "Find..." / "Evaluate...")
  - Conceptual ("Explain why..." / "True or False..." / "Give an example...")
  - Application ("A ball is thrown..." / "Consider a circuit...")
- What percentage is each type? Match this distribution in generated output.

### Difficulty Distribution
- What fraction are routine exercises? (drill, direct application)
- What fraction require combining concepts?
- What fraction are challenging/proof-based?
- Is there a progression from easy to hard within each section?
- Typical split: note the exact ratio in the textbook, don't assume 30/50/20

### Notation Conventions
- What variable names does the textbook prefer? ($f$, $g$ vs $\phi$, $\psi$ vs custom)
- How does it write vectors? ($\vec{v}$, $\mathbf{v}$, $\boldsymbol{v}$)
- How does it write sets? ($\{x : ...\}$ vs $\{x \mid ...\}$)
- Does it use specific theorem numbering? (Theorem 3.2.1 vs Theorem 3.4)
- What notation system for derivatives? ($f'$, $\frac{df}{dx}$, $D_x f$, $\dot{x}$)

### Point Distribution (for exams/tests)
- Total points per exam?
- Points per question type?
- Is partial credit indicated?
- Time allocation per question?

### Language and Tone
- Formal or conversational?
- Does it use "we" or "one" or direct address?
- How much context/setup before each problem?
- Does it include real-world motivation?

## How to Apply the Analysis

### For `/exercise`
- Generate problems that LOOK like they belong in the textbook
- Match the numbering format, sub-part structure, and difficulty curve
- Use the same variable names and notation conventions
- If the textbook uses "Show that..." for proofs, use "Show that..." (not "Prove that...")

### For `/mock-test`
- Match the exact question type distribution from past exams (if provided)
- Match the point distribution and time allocation
- Match the difficulty mix — don't default to 30/50/20 if the actual exams use 20/60/20
- If past exams always have exactly 5 questions, generate exactly 5

### For `/exam-prep`
- Organize formulas the way the textbook organizes them (by chapter vs by topic)
- Use the textbook's theorem numbering in the theorem summary
- Match exercise references to actual textbook exercise numbers

### For `/quiz`
- Match the question styles found in the textbook's review sections (if any)
- If the textbook uses "True/False with justification", do that (not just T/F)

## When No Style Sample is Available

Fall back to sensible defaults:
- Standard academic problem format
- 30% routine, 50% moderate, 20% challenging
- Mix of computation, proof, and conceptual
- Formal but clear language

But always acknowledge: "I'm generating in a standard format. If you have a past exam or problem set, share it and I'll match that style."
