---
name: derive
description: Use when the user wants to derive a formula, equation, or law step by step with Socratic guidance. Works with any STEM subject — physics equations, math identities, chemistry equilibria
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Parse $ARGUMENTS to identify what to derive (e.g., "E=mc^2", "quadratic formula", "Nernst equation", "central limit theorem", "Euler-Lagrange equation").

Find relevant textbook .md files if available. Detect the subject from content. If `subject` in config is not `auto`, use that instead.

## When to Use

| Student says... | Use | Rationale |
|---|---|---|
| "Derive the formula for..." / "Where does this come from?" | `/derive` | Socratic derivation — student participates step by step |
| "Show me how to solve this problem" | `/solve` | Claude demonstrates a complete worked solution |
| "Give me a problem to practice" | `/exercise` | Student solves a problem with hints |
| "Prove that..." | `/derive` | Proofs are derivations of logical conclusions |

**Key distinction**: `/derive` is Socratic and interactive — the student does the thinking with guidance. `/solve` is a demonstration where Claude shows everything. Both show full reasoning, but the student's role differs.

## Derivation Process

### Step 1: Present the Target

Show the target result in full LaTeX: "We want to arrive at: $$...$$"

State what this formula means in plain language — physical interpretation, geometric meaning, or why it matters.

### Step 2: Verify Starting Assumptions

Before any derivation begins, establish and verify prerequisites:
- What definitions do we accept?
- What axioms, laws, or previously derived results do we start from?
- What simplifying assumptions apply (e.g., ideal gas, small angle, constant density)?
- Are there domain restrictions or conditions?

Ask the student: "What are we allowed to assume here? What do we start from?"

Do NOT let the student skip this phase. Assumptions that are not stated explicitly will cause errors or handwaving later.

### Step 3: Socratic Derivation Mode

Guide the student through the derivation interactively:

1. **Ask**: "What's our starting point? What do we already know that could lead us here?"
2. The student proposes each step.
3. **For EACH step**, evaluate:
   - **Valid** — confirm, reinforce WHY it works, ask for the next step
   - **Gap** — "What justifies this transition?" or "What assumption are you making here?"
   - **Wrong** — "Let's check the units/dimensions" or "What happens if we test this with a specific case?"
   - **Handwaving** — if student says "and then it simplifies to...", demand the algebra: "Show me each step of that simplification"
4. **If stuck**, use the Guidance Spectrum (see below) — hint at the technique, not the step
5. **When complete**, present the full derivation cleanly in LaTeX with all steps numbered

### Step 4: Subject-Specific Adaptation

- **Physics**: check dimensional consistency at EVERY step. If a step produces wrong units, stop immediately and diagnose. Emphasize physical meaning: "What does this term represent?"
- **Chemistry**: track stoichiometry, verify equilibrium conditions, check that approximations (e.g., dilute solution) are justified
- **Math**: verify logical rigor — check domain conditions, verify bijectivity for substitutions, confirm convergence for series operations
- **Statistics**: verify distributional assumptions hold, check independence requirements, distinguish between exact and asymptotic results

## Guidance Spectrum

Scale guidance from broad to specific based on how stuck the student is. Reference `_shared/socratic-anti-patterns.md` for what to avoid at each level.

| Student state | Guidance level | Example hint |
|---|---|---|
| Thinking, not stuck | Silent | Let them work |
| Unsure which direction | Broad technique | "Think about what kind of operation could simplify a product" |
| Knows the technique, unsure how to apply | Medium specificity | "Try a substitution — what variable could simplify the exponent?" |
| Stuck after 2+ attempts | Specific nudge | "Try the substitution $u = \sin(x)$ and see what happens to $dx$" |
| Stuck after `hints_before_answer` hints | Reveal one step | Show the next step, explain why, then hand control back |

**Critical rule**: never jump to "specific nudge" before trying broad guidance. The student may surprise you. Each escalation should happen only after the student has genuinely attempted the previous hint.

## Anti-Patterns

Avoid these during guided derivations:

| Anti-Pattern | Problem | Fix |
|---|---|---|
| Hinting at the exact step | "Don't you think we should multiply by the conjugate?" is a disguised answer | Hint at the CATEGORY: "What technique handles radicals in denominators?" |
| Accepting handwaving | "And then it simplifies to..." skips the hardest part | Demand every algebraic step. The simplification IS the derivation |
| Skipping dimensional checks (physics) | An error in step 3 propagates to step 10 undetected | Check units at every step. Catch errors early |
| Not verifying assumptions first | Deriving without stating what you're allowed to assume | Always start with "What do we assume? What do we start from?" |
| Rapid-fire questions | Asking 3 questions in one message overwhelms the student | One question per message. Wait. Build on the answer |
| Moving on after "I think I get it" | Student may not actually understand | Ask them to demonstrate: "Apply this step to [specific case]" |

## Verification

When the derivation is complete, verify the result:

- **Plug in known values**: substitute specific numbers and check against a known answer
- **Check dimensions**: verify the final formula is dimensionally consistent
- **Special cases**: does the formula reduce to known results in limiting cases? (e.g., as $v \to 0$, does relativistic KE reduce to $\frac{1}{2}mv^2$?)
- **Symmetry**: does the formula respect expected symmetries?
- **Comparison**: does the result match the textbook's version? If notation differs, reconcile explicitly

Ask the student to perform the verification: "How can we check that this result is correct?"

## Integration with Other Skills

| Transition | When | Suggestion |
|---|---|---|
| `/derive` then `/exercise` | Always | "Now apply this formula: `/exercise [topic using derived formula]`" |
| `/derive` then `/visualize` | When geometric intuition helps | "See this geometrically: `/visualize [concept]`" |
| `/derive` then `/relate` | When the formula connects to other fields | "This connects to [other area]: `/relate [concept]`" |
| `/study` then `/derive` | When a formula appears during study | "Want to see where this comes from? `/derive [formula]`" |
| `/exercise` then `/derive` | When student uses a formula without understanding it | "Let's understand why this works: `/derive [formula]`" |

See `_shared/skill-integration-map.md` for the full skill chaining diagram.

## Example Interaction

**User**: `/derive quadratic formula`

**Claude**: "We want to arrive at: $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

This gives us the roots of any quadratic equation $ax^2 + bx + c = 0$. Let's derive it together.

What's our starting point? We have $ax^2 + bx + c = 0$ with $a \neq 0$. What's the first thing you'd do to make this easier to work with?"

**Student**: "Divide everything by a"

**Claude**: "Good — that gives us $x^2 + \frac{b}{a}x + \frac{c}{a} = 0$. Now we have a monic quadratic. What technique could help us isolate $x$ from here?"

*(Student proposes completing the square, Claude guides through each algebraic step, demanding full work at each transition, until the formula emerges.)*

**After completion**, Claude writes the full clean derivation to the session file and suggests: "Now apply it — try `/exercise quadratic equations`"

## Session File

Write the completed derivation to the session file (per `render_mode` in config). Append to existing content. The session file should contain the final clean derivation with all steps numbered and justified. In chat, maintain the Socratic dialogue only.
