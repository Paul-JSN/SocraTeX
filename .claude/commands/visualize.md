---
name: socratex-visualize
description: Use when the user wants ASCII diagrams or visual representations of math concepts like epsilon-delta, set relationships, or function behavior
---

Read `socratex.config.md` for language settings.

Parse $ARGUMENTS to identify what to visualize (e.g., "epsilon-delta", "open cover", "sequence convergence", "function continuity at a point").

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

**For logical relationships** — Flow diagram with arrows.

After the visualization:
1. Explain what each part represents
2. Connect it to the formal definition in LaTeX
3. Ask: "Does this match your intuition? What would happen if we changed [parameter]?"

Write visualization + explanation to `session.md` and `session.html`.
