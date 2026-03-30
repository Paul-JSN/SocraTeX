---
name: visualize
description: Use when the user wants ASCII diagrams or visual representations of concepts — epsilon-delta, circuits, force diagrams, molecular structures, function behavior, etc.
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Parse $ARGUMENTS to identify what to visualize (e.g., "epsilon-delta", "free-body diagram", "orbital diagram", "probability distribution", "circuit diagram", "function continuity").

Create a visualization using the best fit:

**For functions/sequences** — ASCII graph sketch:
```
  y
  |     *
  |   *   *
  |  *     *
  | *       *---
  +------------- x
```

**For set relationships** — Venn/containment diagrams:
```
┌─── ℝ ──────────────┐
│ ┌─── ℚ ──────────┐ │
│ │ ┌─── ℤ ──────┐ │ │
│ │ │ ┌─── ℕ ──┐ │ │ │
│ │ │ │ 1,2,3.. │ │ │ │
│ │ │ └────────┘ │ │ │
│ │ └────────────┘ │ │
│ └────────────────┘ │
└────────────────────┘
```

**For epsilon-delta / limit concepts** — Annotated number line:
```
──────[───(──L──)───]──────
      a-δ  a-ε L a+ε  a+δ
```

**For circuits/systems** — Block or circuit diagrams:
```
  V ──[R1]──┬──[R2]── GND
             │
            [C1]
             │
            GND
```

**For force/motion** — Free-body diagrams:
```
        N ↑
          |
    f ←── ● ──→ F
          |
        mg ↓
```

**For molecular/orbital** — Structural diagrams:
```
    H   H
     \ /
  H - C - H
```

**For probability** — Distribution sketches:
```
       ╱╲
      ╱  ╲
    ╱    ╲
  ╱________╲
  μ-2σ μ μ+2σ
```

**For logical relationships** — Flow diagram with arrows.

After the visualization:
1. Explain what each part represents
2. Connect it to the formal definition in LaTeX
3. Ask: "Does this match your intuition? What would happen if we changed [parameter]?"

Write visualization + explanation to `session.md` and `session.html` in the working directory.
