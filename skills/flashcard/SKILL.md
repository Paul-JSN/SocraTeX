---
name: flashcard
description: Use when the user wants to generate Q&A flashcards from studied content for review or Anki export. Works with any STEM subject
---

Read `socratex.config.md` from the working directory. If not found, read `${CLAUDE_PLUGIN_ROOT}/socratex.config.md`. If neither exists, use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/core-rules.md` for Socratic method, LaTeX, subject detection, and session file rendering rules. Apply these throughout.

Parse $ARGUMENTS to determine scope:
- A topic or chapter range — generate flashcards from that content
- "all" or empty — generate from all studied material in this session
- A number (e.g., "20") — generate that many cards

Find textbook .md files — check `textbook_path` from config first, then `books/`, then the working directory, or use files provided in the conversation. Detect the subject from content.

## When to Use

| Student says... | Use | Rationale |
|---|---|---|
| "Make me flashcards" / "I want to review" | `/flashcard` | Generate Q&A pairs for memorization |
| "Summarize what I studied" | `/summary` | Prose summary, not Q&A format |
| "Test me on this" | `/quiz` | Interactive assessment, not study cards |
| "What are the key formulas?" | `/study-guide` or `/summary` | Reference sheet, not flashcard format |

**Key distinction**: `/flashcard` produces discrete Q&A pairs optimized for spaced repetition. `/summary` produces connected prose. `/quiz` is interactive with scoring.

## Card Generation

**Card types to mix:**
- **Definition** — Front: "What is [term]?" / Back: formal definition in LaTeX
- **Formula** — Front: "Write the formula for [concept]" / Back: $$formula$$ with conditions
- **Concept** — Front: "Explain why [statement] is true/false" / Back: reasoning
- **Application** — Front: "When would you use [technique]?" / Back: context + conditions
- **Distinction** — Front: "What is the difference between [A] and [B]?" / Back: key differences

Subject-specific card types:
- **Physics**: "What are the units of [quantity]?" / "What law applies when [situation]?"
- **Chemistry**: "What is the product of [reaction]?" / "What conditions favor [direction]?"
- **Statistics**: "What distribution models [scenario]?" / "What assumptions does [test] require?"

**Target mix**: ~30% definitions, ~25% formulas, ~20% concepts, ~15% applications, ~10% distinctions.

**Format — Markdown table:**
| # | Front | Back |
|---|-------|------|
| 1 | What is convergence? | A sequence $\{a_n\}$ converges to $L$ if... |

**After the table, generate Anki-importable format:**
```
Front<tab>Back
```
One card per line, tab-separated. Wrap in a code block so the student can copy it. LaTeX should use Anki's `\(` and `\)` delimiters for inline, `\[` and `\]` for block. Escape any literal tabs or newlines within card content — replace tabs with spaces and newlines with `<br>` to prevent malformed TSV imports.

Apply `show_original_terms` and `term_format` from config.

Write the flashcard set to the session file (per `render_mode` in config).

---

## Anti-Patterns

### Trivial Cards
- BAD front: "What chapter covers limits?" (tests memory of book structure, not math)
- BAD front: "True or false: derivatives are important" (no meaningful test)
- GOOD front: "State the formal definition of a limit" (tests actual knowledge)

Every card must test understanding of the concept, not recognition of textbook layout.

### Cards That Are Too Long
Flashcard backs should be concise. If the back requires a paragraph, break it into multiple cards.

- BAD back: A full proof of the fundamental theorem of calculus
- GOOD back: "If $F'(x) = f(x)$ and $f$ is continuous on $[a,b]$, then $\int_a^b f(x)\,dx = F(b) - F(a)$"

### All One Type
A set of 20 definition cards is boring and tests only recall. Mix card types to test different cognitive levels (recall, application, distinction, reasoning).

### Missing Conditions
Formula cards without validity conditions are dangerous — they teach students to apply formulas blindly.

- BAD: "Integration by parts formula: $\int u\,dv = uv - \int v\,du$"
- GOOD: "Integration by parts: $\int u\,dv = uv - \int v\,du$ (requires $u, v$ differentiable, integral on RHS must exist)"

### Cards That Give Away the Answer
- BAD front: "The chain rule says $\frac{d}{dx}f(g(x)) = $ ?" (the name gives it away)
- GOOD front: "How do you differentiate a composition of two functions?"

## Verification

After generating the set:
- Check that every formula card includes conditions/domain
- Verify card backs are accurate against the textbook
- Confirm the mix of card types (not all one type)
- Test: could a student who only memorized these cards pass a basic quiz on the topic?

## Integration

| Student state | Suggest |
|---|---|
| Flashcards generated, wants to test | `/quiz [same topic]` for active assessment |
| Wants deeper understanding | `/study [topic]` or `/feynman [concept]` |
| Found gaps while reviewing cards | `/exercise [weak topic]` for practice |
| Preparing for exam | `/exam-prep [range]` for comprehensive review |
| Wants to add to existing set | `/flashcard [new topic]` — append to the session file |

See `${CLAUDE_PLUGIN_ROOT}/skills/_shared/skill-integration-map.md` for the full skill flow.
