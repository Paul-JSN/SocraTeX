# Problem Generation Guide

How to generate good practice problems that reinforce learning without being trivially similar to textbook examples.

## Difficulty Scaling Techniques

### Level 1: Change Parameters
Keep the same structure, swap numbers or variables. Useful for building fluency, but limited learning value on its own.
- Textbook: "Find $\int_0^1 x^2 \, dx$" --> Generated: "Find $\int_0^2 x^3 \, dx$"
- This is the MINIMUM acceptable change. Never generate a problem that differs only by one constant.

### Level 2: Add Constraints or Conditions
Introduce a boundary, edge case, or restriction that forces deeper thinking.
- Textbook: "Find the eigenvalues of $A$." --> Generated: "Find the eigenvalues of $A$. For which values of $k$ is $A - kI$ singular?"
- Physics: "Find the acceleration" --> "Find the acceleration, then determine when the object momentarily stops."

### Level 3: Combine Concepts
Require the student to connect two or more ideas from the same chapter or across chapters.
- Textbook covers limits and continuity separately --> Generated: "Give an example of a function that has a limit at $x=2$ but is not continuous there. Then modify it to be continuous but not differentiable."
- Chemistry: stoichiometry + equilibrium --> "Given initial concentrations and $K_{eq}$, find the equilibrium concentrations using an ICE table."

### Level 4: Reverse the Problem
Give the answer and ask for the setup, or ask the student to construct an example.
- Textbook: "Prove this sequence converges." --> Generated: "Construct a sequence that converges to 3 but is never equal to 3."
- Physics: "Given forces, find acceleration." --> "The acceleration is $2 \, \text{m/s}^2$ at angle $30°$. What combination of forces could produce this?"

## "Similar But Different" Patterns

The goal: a problem that LOOKS familiar but requires a different insight or technique.

| Pattern | Example |
|---------|---------|
| Same technique, different domain | Integration by parts on $\int x \sin x \, dx$ --> $\int x^2 e^x \, dx$ (requires applying IBP twice) |
| Same setup, surprising behavior | Convergent series with positive terms --> series with alternating signs that converges conditionally |
| Familiar structure, hidden trap | $\lim_{x \to 0} \frac{\sin x}{x} = 1$ --> $\lim_{x \to 0} \frac{\sin(x^2)}{x}$ (looks similar, requires different handling) |
| Generalize a specific result | "Prove for $n=3$" --> "Prove for general $n$" |

## Subject-Specific Problem Types

- **Math**: proof construction, counterexample generation, compute-and-interpret, "which theorem applies?"
- **Physics**: setup-and-solve, limiting-case analysis, dimensional analysis check, compare-two-scenarios
- **Chemistry**: predict products, balance and calculate yields, explain observations, design a synthesis
- **Statistics**: choose the right test, interpret output, identify violated assumptions, sample size determination
- **Engineering**: model a system, analyze stability, design to meet a spec, troubleshoot a failure mode

## What to Avoid

- **Trivial parameter swaps only**: changing $x^2$ to $x^3$ teaches nothing new
- **Unrealistic setups**: "A frictionless elephant on an inclined plane" -- keep physical problems plausible
- **Problems that require knowledge not yet covered**: check what chapter the student is on
- **Carbon copies with different variable names**: if the steps are identical, the problem is not different enough
- **Ambiguous problem statements**: every generated problem must have a clear, unique answer (or explicitly ask for multiple valid answers)

## Calibrating to Student Performance

- Student solved quickly with no hints --> scale up one difficulty level
- Student needed 2+ hints --> generate another problem at the same level
- Student failed after all hints --> drop one level and reinforce the prerequisite concept
- See `_shared/style-analysis-guide.md` for matching the textbook's own difficulty curve

## Sequencing Problems Within a Session

When generating multiple problems in one session, follow this structure:
1. **Warm-up**: one Level 1 problem to confirm the student remembers the basics
2. **Core practice**: two or three Level 2 problems targeting the main concept
3. **Stretch**: one Level 3 or Level 4 problem to push the student beyond routine application
4. Adjust this plan dynamically based on calibration signals above
