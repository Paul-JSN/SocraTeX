---
name: whatif
description: Use when the user asks "what if" or wants to explore hypothetical scenarios — changing variables, removing constraints, or testing edge cases. Context-isolated so it doesn't disrupt study flow. Works with any STEM subject
---

This skill provides context isolation, like `/btw`. The what-if exploration must NOT derail the current study session.

Use the Agent tool to spawn a sub-agent that handles the what-if scenario independently. The sub-agent should:

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, render_mode=desktop, subject=auto.

Parse $ARGUMENTS to identify the scenario. This can be:
- Numerical: "what if mass = 100kg?", "what if x = 0?"
- Conceptual: "what if gravity didn't exist?", "what if all functions were continuous?"
- Constraint removal: "what if we drop the assumption that...?"

Find relevant textbook content if available. Detect the subject.

## When to Use

| Student says... | Use | Rationale |
|---|---|---|
| "What if X changed?" / "What happens when Y = 0?" | `/whatif` | Hypothetical exploration |
| "Compare X and Y" | `/compare` | Side-by-side comparison, not scenario exploration |
| "Derive the formula for..." | `/derive` | Formal derivation, not speculation |
| "Explain this concept" | `/study` | Learning, not exploring edge cases |

**Key distinction**: `/whatif` explores hypotheticals ("what would happen if..."). `/compare` contrasts two real concepts. `/derive` proves a result formally.

## Exploration Process

### Phase 1: Setup
Present the original formula/law/concept in LaTeX. State the current assumptions.
Then state the what-if change clearly: "We're changing [X] to [Y]. Everything else stays the same."

### Phase 2: Predict
Ask the student: "Before we work this out — what do you THINK will happen?" Wait for their prediction. This is critical — predictions activate deeper learning.

### Phase 3: Explore
Work through the consequences step by step. Adapt to scenario type:
- **Numerical what-ifs**: compute with the new values, compare to baseline. Show the math.
- **Conceptual what-ifs**: trace the logical chain ("if A changes, then B must change because..."). Identify cascading effects.
- **Constraint removal**: show what breaks and why the constraint exists. Find counterexamples that the constraint prevents.

### Phase 4: Insight
- Compare prediction vs result: "You predicted [X], but we got [Y]"
- Ask: "Why did [surprising thing] happen?"
- Connect back to the underlying principle
- State what this reveals about the original concept

After the sub-agent finishes, display the result and state:

"Back to our study session —"

Resume from where the student left off.

This is interactive chat — do NOT write to session.md.

---

## Anti-Patterns

### Shallow Exploration
- BAD: "If mass doubles, force doubles. Done."
- GOOD: "If mass doubles, force doubles — but what does that mean physically? Does the acceleration change? Does the trajectory change? What if we're near the speed of light?"

Always push beyond the first-order consequence. The insight is in the second and third-order effects.

### Breaking Character (Answering Without Asking)
The prediction phase is not optional. If you skip straight to the answer, the student learns nothing about their own intuition.

### Not Connecting Back
A what-if exploration that doesn't connect back to the original concept is just a calculation exercise. Always end with: "This tells us that [original concept] works because..."

### Unrealistic Scenarios Without Acknowledgment
Some what-ifs are physically impossible. That's fine — but acknowledge it: "This can't happen in reality because [reason], but it's useful to think about because it reveals [insight]."

### Losing Context Isolation
The what-if must not contaminate the study session. If the student was studying Chapter 3, they should return to Chapter 3 after the exploration, not be derailed into a tangent.

## Verification

After the exploration:
- Check that the prediction phase actually happened (student made a prediction)
- Verify that the math/logic is correct in the exploration
- Confirm that the insight connects back to the original concept
- Ensure context isolation was maintained

## Integration

| Student state | Suggest |
|---|---|
| What-if revealed a gap in understanding | `/study [concept]` to fill the gap |
| Student wants to explore more edge cases | Another `/whatif [different scenario]` |
| Student wants to formalize the insight | `/derive [formula]` to prove it rigorously |
| Student wants to practice with varied parameters | `/exercise [topic]` with parameter variation |
| What-if connected to another field | `/relate [concept]` for cross-discipline connections |

See `_shared/skill-integration-map.md` for the full skill flow.
