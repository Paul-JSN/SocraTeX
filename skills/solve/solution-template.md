# Solution Template

Standard structure for a complete worked solution. Used by `/solve` to ensure consistency and quality.

## 1. Problem Statement

Restate the problem clearly in LaTeX. Remove ambiguity from the original phrasing.
If the problem comes from a textbook, cite the source (chapter, exercise number).

## 2. Given / Find / Assumptions

| Subject | Section Label | Content |
|---------|--------------|---------|
| Physics / Engineering | **Given** / **Find** | List all known quantities with units, identify what to solve for |
| Math | **Assumptions** | Domain restrictions, continuity requirements, relevant conditions |
| Statistics | **Given** / **Hypotheses** | Data, sample sizes, significance level, null and alternative hypotheses |
| Chemistry | **Given** / **Find** | Substances, concentrations, conditions (T, P), target quantity |

## 3. Strategy Selection

State WHICH technique, law, or theorem you will use and WHY:
- Why this approach over alternatives
- What conditions make it applicable here
- If multiple steps require different techniques, outline the roadmap

Example: "We use integration by parts because the integrand is a product of a polynomial and an exponential — the polynomial will reduce in degree with each application."

## 4. Step-by-Step Solution

For each step:
1. **State the action** — what you are doing and why
2. **Show the math** — full LaTeX, no skipped algebra
3. **Transition** — briefly explain how this leads to the next step

Keep steps granular. If a single algebraic manipulation involves multiple operations, split it. The student should be able to follow every transition without guessing.

## 5. Answer

Box the final result:

$$\boxed{\text{answer with units}}$$

For multi-part problems, box each sub-answer separately.

## 6. Verification

Perform at least one sanity check:
- **Units**: does the answer have the correct dimensions?
- **Magnitude**: is the number reasonable for the physical context?
- **Boundary/limiting cases**: does the answer reduce to a known result in a special case?
- **Back-substitution**: plug the answer back into the original equation
- **Dimensional analysis**: verify both sides of any equation match

## 7. Alternative Approaches

Briefly mention 1-2 other valid methods:
- Name the technique
- Note whether it would be simpler or more complex
- If one approach generalizes better, say so

This helps the student build a repertoire of strategies, not just memorize one path.
