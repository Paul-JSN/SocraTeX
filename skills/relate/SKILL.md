---
name: relate
description: Use when the user wants to see how a concept connects to other fields, subjects, or real-world applications. Cross-disciplinary bridges for deeper understanding
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Parse $ARGUMENTS to identify the concept (e.g., "eigenvalues", "entropy", "gradient", "equilibrium", "Fourier transform").

Detect the current subject context from conversation or textbook content.

Generate a cross-discipline connection map:

**1. Within This Subject**
How this concept connects to other topics in the same subject. Show prerequisite and downstream relationships.

**2. Across Subjects**
Map the concept to analogues in other STEM fields. Use a table:

| Field | Analogue | Connection |
|-------|----------|------------|
| Math | Eigenvalues of a matrix | Same linear algebra foundation |
| Physics | Normal modes of vibration | Physical interpretation of eigenvalues |
| Engineering | Resonant frequencies | Design application |

**3. Real-World Applications**
2-3 concrete examples of where this concept appears in practice. Be specific — not "engineering" but "structural analysis of bridges."

**4. Historical Context** (brief)
One sentence on where/why this concept was developed. Helps build intuition about its purpose.

**5. "Aha" Question**
End with a thought-provoking question that reveals a deep connection: "Why do you think [concept A] and [concept B] share the same mathematical structure?"

Write the connection map to `session.md` in the working directory (overwrite). All formulas in LaTeX.
