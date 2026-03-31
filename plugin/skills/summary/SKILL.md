---
name: summary
description: Use when the user wants a concise summary of studied content — key concepts, formulas, and takeaways in a compact format. Works with any STEM subject
---

Read `socratex.config.md` from the working directory. If not found, read `${CLAUDE_PLUGIN_ROOT}/socratex.config.md`. If neither exists, use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/core-rules.md` for Socratic method, LaTeX, subject detection, and session file rendering rules. Apply these throughout.

Parse $ARGUMENTS:
- A topic or chapter range — summarize that content from textbook files
- Empty — summarize what was covered in this study session

Find textbook .md files if a range is specified. Detect the subject from content.

## When to Use

| Student says... | Use | Rationale |
|---|---|---|
| "Summarize what I studied" / "Give me the highlights" | `/summary` | Concise reference |
| "Make me flashcards" | `/flashcard` | Q&A pairs for spaced repetition, not prose |
| "Make me a study plan" | `/study-guide` | Comprehensive plan with schedule, not a summary |
| "What are all the formulas?" | `/study-guide` (formula sheet section) or `/summary` | Depends on scope |

**Key distinction**: `/summary` is a concise backward-looking reference. `/study-guide` is a forward-looking plan. `/flashcard` is Q&A format for active recall.

## Summary Generation

Generate a concise summary (shorter than study-guide — this is a quick reference, not a comprehensive overview):

**1. Core Concepts** (3-5 bullet points)
One sentence each. What are the essential ideas? Subject-adapted:
- Math: state the theorem or definition precisely
- Physics: state the law and its physical meaning
- Chemistry: state the principle and when it applies
- Statistics: state the method and what question it answers

**2. Key Formulas/Laws**
The critical formulas in LaTeX $$...$$ blocks. Only the ones worth memorizing — not every formula, just the important ones. Include conditions for validity.

**3. Key Results/Theorems**
Statement only (no proofs). One line each. If there are conditions, state them.

**4. Connections**
How these concepts relate to each other. 2-3 sentences showing the logical flow.

**5. What to Review**
Based on difficulty of the material, flag concepts that need more practice. If the student struggled with something during the session, mention it here.

Apply `show_original_terms` and `term_format` from config.

Write the summary to the session file (per `render_mode` in config).

---

## Anti-Patterns

### Too Long
A summary that's as long as the original material defeats the purpose. Target roughly 1/5 to 1/10 the length of the source content.

- BAD: Re-stating every definition and theorem from the chapter
- GOOD: The 3-5 most important ideas, the critical formulas, and how they connect

### Too Vague
- BAD: "This chapter covers limits and continuity"
- GOOD: "A function $f$ is continuous at $a$ if $\lim_{x \to a} f(x) = f(a)$. The three key limit laws are..."

Summaries must contain actual content, not descriptions of content.

### Missing Formulas
A STEM summary without LaTeX formulas is incomplete. The formulas ARE the summary for many topics.

### No Prioritization
Not all concepts are equally important. The summary should make clear which concepts are foundational (must know) vs. supplementary (nice to know).

### Ignoring Session Context
If the student struggled with specific concepts during the session, the "What to Review" section must mention those. Don't generate a generic summary when you have data about the student's actual performance.

## Verification

After generating:
- Check that all critical formulas from the source material are included
- Verify formulas are correct (compare against textbook)
- Confirm the summary is genuinely concise (not a restatement of everything)
- Check that "What to Review" reflects the student's actual session performance (if available)

## Integration

| Student state | Suggest |
|---|---|
| Summary generated, wants to test | `/quiz [topic]` for a quick assessment |
| Wants flashcards from this content | `/flashcard [same range]` |
| Wants to practice | `/exercise [topic from summary]` |
| Found gaps in the summary | `/study [gap topic]` to re-learn |
| Preparing for exam | `/exam-prep [range]` for comprehensive prep |
| Wants to go deeper on one concept | `/derive [formula]` or `/whatif [concept]` |

See `${CLAUDE_PLUGIN_ROOT}/skills/_shared/skill-integration-map.md` for the full skill flow.
