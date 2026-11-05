---
name: visualize
description: Use when the user wants to see a concept visually or interactively — function behavior, epsilon-delta, limits, derivatives, integrals, series, linear transformations, 3D surfaces, vector fields, probability distributions, geometry, circuits, force diagrams — or when /study needs a visualization page for a unit.
---

Read `SocraTeX.config.md` from the working directory. If not found, read `${CLAUDE_PLUGIN_ROOT}/SocraTeX.config.md`. If neither exists, use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/core-rules.md` for Socratic method, LaTeX, subject detection, and session file rendering rules. Apply these throughout.

Parse $ARGUMENTS to identify what to visualize. If a textbook source is in play, take notation from it.

## What You Produce

One self-contained interactive HTML page per concept at `viz/<topic-slug>.html` in the working directory. The page is the visualization and nothing else: the dialogue, questions and explanations happen in chat.

**Before writing, read `${CLAUDE_PLUGIN_ROOT}/skills/visualize/example-epsilon-delta.html`** and build from it. Keep its tokens, shell, controls, motion loop and dark mode; replace the `Math` block, the stage and the controls' meaning. Read `${CLAUDE_PLUGIN_ROOT}/skills/visualize/viz-guide.md` for the library per topic, pinned CDN URLs and stage recipes.

## The Page

Exactly these elements, all text in `study_language`:

1. **Stage** — the figure fills the whole window.
2. **Title** (top-left) — the concept name, with the function or formula in KaTeX underneath.
3. **Status chip** (top-right; under the title on narrow screens) — one short phrase computed from the current state. For a yes/no condition, say whether it holds (`이 δ면 충분해요`); for a quantity, give the number (`S₄ = 3.750 · 오차 0.917`). Green when the condition holds or the quantity has reached the point of the lesson, red otherwise.
4. **Dock** (bottom, floating) — a segmented picker when there are several cases, then one slider per parameter, each labeled with its symbol and live value. Up to four controls.

Nothing else on the page: no explanation paragraphs, definition cards, prediction boxes, question lists, hints, legends or buttons beyond the controls.

## Motion

Use the example's loop: controls set `target`, the figure draws `view`, and one `requestAnimationFrame` loop eases `view` toward `target`.

- On load, and whenever a case switch changes the main curve or object, draw it in over about 0.7 s.
- Parameter changes glide (bands, points, surfaces follow the slider smoothly), while the status chip reports `target` immediately.
- When the status flips, the chip makes one short swap animation.
- Nothing loops or blinks on its own. `prefers-reduced-motion` turns all motion off.

## Correctness

- Every number on the page is computed from the current state; never hard-code a status or a "right" value.
- Sample densely near singularities; draw jumps as separate pieces with open and closed dots.
- Equal axis scale when angles or lengths matter (geometry, linear maps).
- Start in an informative state, often a failing one, so the first slider move teaches something.

## Verify

If a browser tool is available (Browser pane, Playwright, Chrome), load the page, read console errors, take a screenshot, and move every control once. If the tool refuses `file://` URLs, serve the working directory with `python3 -m http.server 8765 --bind 127.0.0.1` in the background, load `http://127.0.0.1:8765/viz/<slug>.html`, and stop the server afterwards. Fix every error and every overlap between the title, chip, dock and figure before handing the page over.

## Hand-off

- **Called by the student:** open the page (`open` on Mac, `xdg-open` on Linux, `start` on Windows; in the Claude Code desktop app, writing the file already shows it), then in chat send the path and one question about what they see when they move a specific control. Continue the dialogue in chat from their answers.
- **Called while building a `/study` plan** (pre-generation): do not open the page and do not message the student. Return only the path and whether verification passed.

Append the topic title, key formula and page path to the session file (per `render_mode`) when called by the student.

## Text Fallback

When `render_mode: vscode` and no browser can be opened, or the student asks for a quick sketch in chat, draw a small ASCII diagram (under 20 lines) with labels and end with a question about what would change if a parameter moved.

## Common Mistakes

| Mistake | Fix |
|---|---|
| Explanations, questions or cards on the page | The page has stage, title, chip and dock only; talk in chat |
| Jumping figure on slider change | Draw from `view` and ease it toward `target` |
| Status written by hand | Compute it from `target` on every input |
| Title or chip overlapping axis labels | Widen the bounding box so the corners above the plot are empty |
| Unpinned or extra libraries | Only the pinned URLs in `viz-guide.md` |
| Skipping the browser check | A page with a console error is not done |

## Integration

| Student state | Suggest |
|---|---|
| Wants the formal definition behind the picture | `/study [concept]` |
| Wants to push the picture to extremes | `/whatif [parameter change]` |
| Wants to see where the formula comes from | `/derive [formula]` |
| Ready to practice | `/exercise [topic]` |

See `${CLAUDE_PLUGIN_ROOT}/skills/_shared/skill-integration-map.md` for the full skill flow.
