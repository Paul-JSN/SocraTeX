---
name: relate
description: Use when the user wants to see how a concept connects to other fields, subjects, or real-world applications. Cross-disciplinary bridges for deeper understanding
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Parse $ARGUMENTS to identify the concept (e.g., "eigenvalues", "entropy", "gradient", "equilibrium", "Fourier transform").

Detect the current subject context from conversation or textbook content.

## When to Use

| Student says... | Use | Rationale |
|---|---|---|
| "How does X connect to other fields?" / "Where is X used?" | `/relate` | Cross-discipline connection map |
| "What's the difference between X and Y?" | `/compare` | Pairwise comparison, not broad connections |
| "What if X changed?" | `/whatif` | Hypothetical exploration |
| "What should I learn after this?" | `/roadmap` | Learning path, not concept connections |

**Key distinction**: `/relate` maps one concept to many fields (breadth). `/compare` contrasts two specific concepts (depth). `/roadmap` plans a learning path (sequence).

## Connection Map Generation

### 1. Within This Subject
How this concept connects to other topics in the same subject. Show prerequisite and downstream relationships. Use LaTeX for any formulas that illustrate the connection.

### 2. Across Subjects
Map the concept to analogues in other STEM fields:

| Field | Analogue | Connection |
|-------|----------|------------|
| ... | ... | ... |

Be specific about HOW the concepts are related — not just "same math" but "both solve eigenvalue problems because [reason]."

### 3. Real-World Applications
2-3 concrete examples of where this concept appears in practice. Be specific:
- NOT "engineering" — instead "structural analysis of bridges (resonant frequencies = eigenvalues of the stiffness matrix)"
- NOT "medicine" — instead "CT scan reconstruction (Fourier transform converts X-ray projections into cross-sectional images)"

### 4. Historical Context (brief)
One sentence on where/why this concept was developed. Helps build intuition about its purpose.

### 5. "Aha" Question
End with a thought-provoking question that reveals a deep connection: "Why do you think [concept A] and [concept B] share the same mathematical structure?"

Write the connection map to the session file (per `render_mode` in config). All formulas in LaTeX.

---

## Anti-Patterns

### Surface-Level Connections
- BAD: "Eigenvalues appear in physics and engineering"
- GOOD: "In quantum mechanics, eigenvalues of the Hamiltonian operator $\hat{H}\psi = E\psi$ are the allowed energy levels. This is why atoms emit discrete spectral lines, not continuous light."

Every connection must explain the MECHANISM, not just state the existence.

### Too Many Connections Without Depth
Listing 15 fields where a concept appears, each in one sentence, teaches nothing. Better to show 3-4 connections deeply than 10 superficially.

### Forced Connections
Not every concept connects meaningfully to every field. If the connection is tenuous, don't include it. Quality over quantity.

### No Mathematical Bridge
When two fields use the same concept, show the mathematical structure they share. "Both use eigenvalues" is not enough — show the equation in both contexts and highlight the structural parallel.

### Missing the "Aha"
The "Aha" question is not optional decoration. It's the point of the skill — to spark insight about WHY concepts recur across fields. If the question doesn't provoke genuine thought, it's too weak.

## Verification

After generating the connection map:
- Verify that each cross-discipline analogue is accurate (not a false parallel)
- Check that real-world applications are specific and correct
- Confirm the mathematical bridge is properly shown (equations in both contexts)
- Test the "Aha" question: does it actually require thought, or is the answer obvious?

## Integration

| Student state | Suggest |
|---|---|
| Interested in a specific connection | `/study [connected topic]` in the other field |
| Wants to compare two connected concepts | `/compare [concept A vs concept B]` |
| Wants to explore edge cases | `/whatif [scenario in the connected field]` |
| Wants to formalize the connection | `/derive [shared formula]` |
| Wants to practice applying the concept | `/exercise [topic]` with cross-disciplinary problems |

See `_shared/skill-integration-map.md` for the full skill flow.
