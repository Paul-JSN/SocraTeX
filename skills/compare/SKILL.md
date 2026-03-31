---
name: compare
description: Use when the user wants to compare two concepts side by side — definitions, differences, counterexamples, when to use which. Works with any STEM subject
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Parse $ARGUMENTS to identify the two concepts to compare (e.g., "uniform vs pointwise convergence", "kinetic vs potential energy", "SN1 vs SN2 reactions", "Bayesian vs frequentist").

Find relevant textbook content if available. Detect the subject.

## When to Use

| Student says... | Use | Rationale |
|---|---|---|
| "What's the difference between X and Y?" | `/compare` | Side-by-side structured comparison |
| "What if X changed?" | `/whatif` | Hypothetical exploration, not comparison |
| "How does X connect to other fields?" | `/relate` | Cross-discipline connections, not pairwise comparison |
| "Explain X" | `/study` | Learning one concept, not contrasting two |

**Key distinction**: `/compare` contrasts two specific concepts. `/relate` maps one concept to many fields. `/whatif` explores hypotheticals.

## Comparison Generation

Follow the structure in `compare/comparison-template.md`:

### 1. Definitions Side by Side
Both definitions in LaTeX, formatted for easy visual comparison. Use a table for parallel structure.

### 2. Key Differences
Numbered list of precise differences. Each difference should be:
- Specific (not "they're different")
- Illustrated with math or an example
- Stated in terms of WHAT differs and WHY it matters

### 3. Similarities
What they share — common ancestor concept, cases where they coincide, shared structure.

### 4. The Critical Counterexample
The ONE example that makes the distinction crystal clear. This is the most important part. Show a concrete object where one concept holds but not the other.

### 5. When to Use Which
Practical decision guide: "Use A when..." / "Use B when..." / "The distinction matters when..."

### 6. Common Confusion Points
What students typically mix up between the two, and how to keep them straight.

Write the full comparison to the session file (per `render_mode` in config). Apply language/term settings.

---

## Anti-Patterns

### No Counterexample
A comparison without a counterexample is incomplete. The counterexample IS the comparison — it makes the abstract distinction concrete.

- BAD: "Uniform convergence is stronger than pointwise convergence"
- GOOD: "The sequence $f_n(x) = x^n$ on $[0,1]$ converges pointwise to $f(x) = 0$ for $x \in [0,1)$ and $f(1) = 1$, but NOT uniformly because $\sup|f_n - f| = 1$ for all $n$"

### Listing Without Explaining
- BAD: "Difference 1: A uses X, B uses Y. Difference 2: A requires P, B requires Q."
- GOOD: "A uses X because [reason], while B uses Y because [different reason]. This matters when [context]."

Every difference needs a "why it matters."

### Symmetric Treatment When Asymmetric
Sometimes one concept is strictly stronger/weaker than the other. Don't pretend they're equal when they're not. State the relationship: "A implies B, but B does not imply A."

### Forgetting "When Does It Matter?"
Students need to know not just WHAT the difference is, but WHEN the difference matters. If the distinction only matters in edge cases, say so. If it matters everywhere, say that too.

### Comparing Incomparable Concepts
If the student asks to compare concepts that aren't meaningfully comparable (e.g., "eigenvalues vs photosynthesis"), say so. Suggest what they might actually mean, or redirect to `/relate` if the connection is cross-disciplinary.

## Verification

After generating the comparison:
- Verify both definitions are correct (check against textbook)
- Confirm the counterexample actually demonstrates the claimed distinction
- Check that the "when to use which" section gives actionable guidance
- Ensure the comparison is balanced (not biased toward one concept)

## Integration

| Student state | Suggest |
|---|---|
| Understood the comparison | `/exercise [topic]` with problems that require choosing between the two concepts |
| Confused by one of the concepts | `/study [specific concept]` to build understanding first |
| Wants to go deeper | `/derive [key formula]` for either concept |
| Wants to see connections beyond this pair | `/relate [concept]` for cross-discipline mapping |
| Wants to test understanding | `/quiz [topic]` or `/feynman [concept]` |

See `_shared/skill-integration-map.md` for the full skill flow.
