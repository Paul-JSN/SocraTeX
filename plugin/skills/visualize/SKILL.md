---
name: visualize
description: Use when the user wants ASCII diagrams or visual representations of concepts — epsilon-delta, circuits, force diagrams, molecular structures, function behavior, probability distributions, etc.
---

Read `SocraTeX.config.md` from the working directory. If not found, read `${CLAUDE_PLUGIN_ROOT}/SocraTeX.config.md`. If neither exists, use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/core-rules.md` for Socratic method, LaTeX, subject detection, and session file rendering rules. Apply these throughout.

Parse $ARGUMENTS to identify what to visualize (e.g., "epsilon-delta", "free-body diagram", "orbital diagram", "probability distribution", "circuit diagram", "function continuity").

Detect the subject from context or content.

## When to Use

| Student says... | Use | Rationale |
|---|---|---|
| "Draw this" / "Can you show me visually?" | `/visualize` | ASCII diagram + explanation |
| "Compare X and Y" | `/compare` | Structured comparison, not just a diagram |
| "Explain this concept" | `/study` | Full Socratic study, not just visual |
| "Show me how to solve this" | `/solve` | Worked solution, not diagram |

**Key distinction**: `/visualize` creates a visual representation to build intuition. `/study` teaches the concept with dialogue. Often used together: `/study` for understanding, `/visualize` for intuition.

## Visualization Types

Choose the best format based on the concept:

**For functions/sequences** — ASCII graph sketch:
```
  y
  |     *
  |   *   *
  |  *     *
  | *       *---
  +------------- x
```

**For set relationships** — Containment diagrams:
```
+--- R --------------------+
| +--- Q ----------------+ |
| | +--- Z ------------+ | |
| | | +--- N --------+ | | |
| | | | 1, 2, 3, ... | | | |
| | | +--------------+ | | |
| | +------------------+ | |
| +----------------------+ |
+---------------------------+
```

**For epsilon-delta / limit concepts** — Annotated number line:
```
------[---(--L--)---]------
      a-d  a-e L a+e  a+d
```

**For circuits/systems** — Block or circuit diagrams:
```
  V --[R1]--+--[R2]-- GND
             |
            [C1]
             |
            GND
```

**For force/motion** — Free-body diagrams:
```
        N ^
          |
    f <-- o --> F
          |
        mg v
```

**For molecular/orbital** — Structural diagrams:
```
    H   H
     \ /
  H - C - H
```

**For probability** — Distribution sketches:
```
       /\
      /  \
    /    \
  /________\
  m-2s m m+2s
```

**For logical relationships** — Flow diagrams with arrows.

## After the Visualization

1. **Label everything**: explain what each part represents
2. **Connect to formal definition**: present the formal definition in LaTeX alongside the diagram
3. **Probe understanding**: "Does this match your intuition? What would happen if we changed [parameter]?"

Write visualization + explanation to the session file (per `render_mode` in config).

---

## Anti-Patterns

### Diagram Without Explanation
An ASCII diagram by itself is just art. Every diagram must be accompanied by:
- What each symbol/element represents
- How the diagram maps to the formal definition
- At least one question that tests whether the student actually understands the visual

### Overly Complex Diagrams
ASCII art has limits. If the diagram requires 30+ lines to be readable, simplify it. Focus on the essential structure, not every detail.

- BAD: A 40-line circuit diagram with every component labeled
- GOOD: A simplified circuit showing the key topology, with a note: "simplified — omitting [details]"

### Wrong Level of Abstraction
- BAD: Drawing a detailed molecular orbital diagram when the student just wants to see bond angles
- GOOD: Matching the diagram's complexity to the concept being taught

Ask yourself: what is the ONE thing this diagram should make clear?

### No Formal Connection
A visual without the corresponding LaTeX formula teaches intuition but not rigor. Always pair:
- The visual (intuition) with
- The formal definition (rigor)

### Static Only
Diagrams should suggest what CHANGES when parameters vary. Use annotations like "if epsilon shrinks, this band narrows" or show two diagrams side by side (before/after).

## Verification

After creating the visualization:
- Check that the diagram is actually readable in a monospace font
- Verify that labels match the formal definition
- Confirm the diagram accurately represents the concept (not misleading)
- Test: could a student reconstruct the key idea from the diagram alone?

## Integration

| Student state | Suggest |
|---|---|
| Wants to understand the formal definition | `/study [concept]` for Socratic dialogue |
| Wants to explore what changes | `/whatif [parameter change]` to see dynamic behavior |
| Wants to see the derivation | `/derive [formula shown in diagram]` |
| Wants to practice | `/exercise [topic]` with problems that require visual reasoning |
| Wants to compare two visual concepts | `/compare [concept A vs B]` with diagrams for each |

See `${CLAUDE_PLUGIN_ROOT}/skills/_shared/skill-integration-map.md` for the full skill flow.
