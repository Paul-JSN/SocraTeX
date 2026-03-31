---
name: solve
description: Use when the user wants to see a complete worked solution — Claude demonstrates the full solving process step by step. Unlike /exercise (student solves), here Claude shows how. Works with any STEM subject
---

Read `socratex.config.md` from the working directory. If not found, read `${CLAUDE_PLUGIN_ROOT}/socratex.config.md`. If neither exists, use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/core-rules.md` for Socratic method, LaTeX, subject detection, and session file rendering rules. Apply these throughout.

Parse $ARGUMENTS to identify the problem. This can be:
- An exercise number from the textbook
- A problem pasted directly
- A topic (e.g., "integration by parts example", "projectile motion problem")

Find relevant textbook content if available. Detect the subject. Adapt the solution style to the subject's conventions.

## When to Use

| Student says... | Use | Rationale |
|---|---|---|
| "Show me how to solve this" / "Solve this problem" | `/solve` | Claude demonstrates the full solution |
| "Give me a problem to practice" / "I want to try" | `/exercise` | Student solves with Socratic hints |
| "Derive the formula for..." / "Where does this equation come from?" | `/derive` | Guided derivation of a formula/law (student participates) |
| "I'm stuck on this exercise" | `/solve` first, then `/exercise` for a similar one | See worked example, then practice |

**Key distinction**: `/solve` = Claude shows the work. `/exercise` = student does the work. `/derive` = student derives a formula with guidance.

## Solution Process

Present the problem statement clearly in LaTeX.

Follow the structure in `${CLAUDE_PLUGIN_ROOT}/skills/solve/solution-template.md`:

### Step 1: Problem Setup
- Restate the problem unambiguously
- List givens, unknowns, and assumptions
- For physics: draw an ASCII diagram with coordinate system and labeled quantities
- For chemistry: write the balanced equation first

### Step 2: Strategy Selection
- State which technique, law, or theorem applies and WHY
- Explain what makes this approach appropriate (not just "we use X")
- If multiple techniques could work, briefly justify the choice
- Flag if the technique might be beyond the student's current level: "This uses [X], which you may not have covered yet — let me know if you'd like background"

### Step 3: Step-by-Step Solution
For each step:
1. State what you're about to do and WHY (not just the mechanics, but the reasoning)
2. Show the math/work in LaTeX — no skipped algebra
3. Briefly explain the transition to the next step

### Step 4: Subject-Specific Style
- **Math**: rigorous steps, cite theorems used, check conditions before applying
- **Physics**: identify knowns/unknowns, state which law/principle applies, check units at every step
- **Chemistry**: balanced equation first, identify limiting reagents, track units (mol, g, M)
- **Statistics**: state hypotheses, check assumptions explicitly, compute test statistic, interpret in context
- **Engineering**: define system boundaries, state simplifying assumptions, verify with dimensional analysis

### Step 5: Conclusion
1. Box the final answer: $$\boxed{answer}$$
2. Sanity check: "Does this make sense?" — verify units, magnitude, boundary behavior, or back-substitute
3. Alternative approaches: briefly mention 1-2 other valid methods
4. Suggest next step: "Want to try a similar problem yourself? Run `/exercise [topic]`"

## Anti-Patterns

Avoid these when writing solutions:

| Anti-Pattern | Problem | Fix |
|---|---|---|
| Skipping the "why" | Showing mechanics without reasoning teaches procedure, not understanding | Every step must explain WHY, not just WHAT |
| Not checking reasonableness | A 500 kg baseball should raise a red flag | Always run at least one sanity check (units, magnitude, limiting case) |
| Using advanced techniques without flagging | Student may not know the method yet | Explicitly note: "This uses [technique]. If unfamiliar, see [topic]" |
| Overly terse steps | "Simplifying, we get..." skips the learning | Show every algebraic transition. If a step involves 3+ operations, split it |
| No strategy explanation | Jumping into computation without saying which tool and why | Always state the approach and justify the choice before computing |
| One-path thinking | Only showing one method implies it's the only way | Mention alternatives even briefly — builds problem-solving flexibility |

## Solution Quality Checklist

Before presenting a solution, verify against `${CLAUDE_PLUGIN_ROOT}/skills/solve/solution-template.md`:
- [ ] Problem restated clearly (no ambiguity from original)
- [ ] Givens/unknowns/assumptions listed explicitly
- [ ] Strategy stated and justified BEFORE computation begins
- [ ] Every step has reasoning, not just mechanics
- [ ] No algebraic transitions skipped
- [ ] Subject-appropriate conventions followed (units, diagrams, notation)
- [ ] Final answer boxed with units
- [ ] At least one sanity check performed
- [ ] Alternative approach mentioned
- [ ] Next step suggested (/exercise)

## Style Matching

Reference `${CLAUDE_PLUGIN_ROOT}/skills/_shared/style-analysis-guide.md` to match the textbook's solution style:
- Use the same notation conventions (variable names, vector notation, derivative notation)
- Follow the textbook's level of formality
- If the textbook shows solutions in a particular format, replicate it
- Match the textbook's language patterns ("we observe that..." vs "note that..." vs "it follows that...")

## Verification Requirements

The answer MUST pass at least one of these checks:
- **Unit analysis**: verify dimensions on both sides of every equation
- **Magnitude check**: is the number physically/mathematically reasonable?
- **Limiting cases**: does the answer reduce to known results when a parameter goes to 0, 1, or infinity?
- **Back-substitution**: plug the answer back into the original equation
- **Symmetry**: does the answer respect expected symmetries of the problem?

If a check fails, revisit the solution before presenting it.

## Integration with Other Skills

| Transition | When | Suggestion |
|---|---|---|
| `/solve` then `/exercise` | Always | "Want to try a similar problem? `/exercise [same topic]`" |
| `/solve` then `/derive` | When the solution uses a non-obvious formula | "Want to see where this formula comes from? `/derive [formula]`" |
| `/solve` then `/visualize` | When geometric intuition helps | "Want to see this graphically? `/visualize [concept]`" |
| `/solve` then `/relate` | When the problem connects to other fields | "This connects to [other field]. Try `/relate [concept]`" |
| `/exercise` then `/solve` | When student is stuck | Student ran `/exercise` and couldn't finish — `/solve` shows the way |

## Example Interaction

**User**: `/solve Find the eigenvalues of A = [[2, 1], [1, 2]]`

**Claude** (in session file):

> **Problem**: Find the eigenvalues of $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.
>
> **Strategy**: Eigenvalues satisfy $\det(A - \lambda I) = 0$. Since $A$ is $2 \times 2$, this yields a quadratic in $\lambda$. We also note $A$ is real symmetric, so eigenvalues are guaranteed real.
>
> **Step 1**: Form $A - \lambda I = \begin{pmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{pmatrix}$
>
> **Step 2**: Compute determinant: $(2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3$
>
> **Step 3**: Factor: $(\lambda - 1)(\lambda - 3) = 0$, so $\lambda_1 = 1,\ \lambda_2 = 3$
>
> $$\boxed{\lambda_1 = 1, \quad \lambda_2 = 3}$$
>
> **Check**: $\lambda_1 + \lambda_2 = 4 = \text{tr}(A)$ and $\lambda_1 \cdot \lambda_2 = 3 = \det(A)$. Consistent.
>
> **Alternative**: Since $A = I + \mathbf{1}\mathbf{1}^T$, eigenvalues shift by 1 from those of the rank-1 matrix $\mathbf{1}\mathbf{1}^T$.

**Claude** (in chat): "Want to try finding eigenvectors for these eigenvalues? Run `/exercise eigenvalues and eigenvectors`"

## Session File

Write the full worked solution to the session file (per `render_mode` in config). Overwrite with new content. In chat, give a brief intro and the next-step suggestion only.
