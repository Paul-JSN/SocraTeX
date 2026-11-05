---
name: study
description: Use when the user wants to learn new material from a textbook, PDF, lecture notes or course folder — a chapter, section or page range — or wants to continue a study session from where they left off. Works with any STEM subject — math, physics, chemistry, statistics, engineering, economics
---

Read `SocraTeX.config.md` from the working directory. If not found, read `${CLAUDE_PLUGIN_ROOT}/SocraTeX.config.md`. If neither exists, use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto. Apply these throughout.

Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/core-rules.md` for Socratic method, LaTeX, subject detection, sources, and session file rendering rules. Apply these throughout. Where this file and core rules differ, this file wins for `/study`.

## 1. Decide: Resume, List, or Plan

- **$ARGUMENTS empty and `progress/` holds a plan with `Status: in progress`** → resume it (section 5). If several are in progress, list them one line each and ask which.
- **$ARGUMENTS empty and no plan** → list the study materials found (see Sources in core rules) with their chapters or page counts. Stop.
- **$ARGUMENTS names material and a range** ("materials/rudin.pdf p.47-58", "chapter 3", "3.2-3.4", "lecture 5 notes") → if `progress/` already has a plan for the same source and range, resume it (section 5) unless the student says to start over. Otherwise build a plan (section 2).

## 2. Build the Lesson Plan

1. Read the whole range before teaching anything. PDFs: use the Read tool with `pages`, at most 20 pages per call. If the student gave printed page numbers, find the offset to PDF page numbers and record it; if the PDF has no printed numbers, the offset is 0.
2. Detect the subject from the content (or use `subject` from config if not `auto`).
3. Split the range into 5-12 **units**, one idea each, and fill `${CLAUDE_PLUGIN_ROOT}/skills/study/lesson-plan-template.md` for every unit.
   - Statement: the source's wording, with its formulas in LaTeX.
   - Hook and Check: specific numbers or a specific function, using examples that no other unit teaches.
   - Visual: up to one unit in two; choose the units where moving a parameter shows the mechanism best, and name the page `viz/u<N>-<topic-slug>.html`.
4. Save it to `progress/<source-slug>-<range-slug>.md` in the working directory (create `progress/` if missing), e.g. `progress/rudin-p47-58.md`.
5. In chat: the plan path on one line, the numbered unit titles, and one question: ready to start with U1?

## 3. Teach One Unit

Run these steps in order. **Each step is its own message, and each message ends with exactly one question and then stops.**

- **A. Hook** — ask the unit's hook question before showing the statement. If the student says they don't know, give one concrete number to compute and ask again; that counts as an attempt.
- **B. Statement** — present the statement as a LaTeX formula with a `study_language` gloss, then ask what it says intuitively. Append the unit heading and statement to the session file (create and open it on first write).
- **C. Dialogue** — guide with questions (see `${CLAUDE_PLUGIN_ROOT}/skills/study/questioning-techniques.md`). Count attempts per question you ask; the count starts at zero for each new question. When an answer is partly right, say which part is right and ask a question that isolates the wrong part. When attempts on one question reach `hints_before_answer`, explain that point in at most four sentences and ask the student to apply it to a concrete case.
- **D. Visual** (units marked `Visual:`) — build the page now by the `/visualize` process (`${CLAUDE_PLUGIN_ROOT}/skills/visualize/SKILL.md`), then send the path plus one question about what the student sees when they move a specific control. Continue the dialogue from what the student reports seeing.
- **E. Critical thinking** — pose the unit's trigger. The student must produce something: a counterexample, the flaw in a proof, the reason a hypothesis is needed, or a link to an earlier unit.
- **F. Check** — ask the unit's check question (see Verification). Pass → G. Fail → back to C with a question that isolates the gap.
- **G. Record and move on** — tick the unit, set `Resume at:` to the next unit's step A, append a Session Log line (what they got, where they stalled, attempts used), add anything shaky to Weak Points, then in one line name the next unit and ask its hook.

### Message Shape

A teaching message is: at most six lines of prose, plus at most one display formula or one short list, plus one question on its own last line. Longer reference material (worked examples, tables, full proofs) goes to the session file. This shape applies to every message in a `/study` session, including explanations the student asks for.

### Student Requests

The student's explicit request outranks the attempt minimum in core rules. Pace changes are saved in the plan's `Pace:` field so they carry over; one-time requests are not.

| Student says | Do |
|---|---|
| "faster", "빠르게", "빨리", "I know this" | Pace `fast`: merge A+B into one message; at D send the page path as an optional link and go on without waiting; still run E and F |
| "slower", "천천히", "I'm lost" | Pace `slow`: split C into smaller questions; give a numeric example before every abstract one; at F require two different checks |
| "just explain", "그냥 설명해줘" (one-time) | Explain the current point within Message Shape, ending with the F question in the same message, and append the statement to the session file. After F: E (for a Visual unit, add the page path to the E message as an optional link), then G. Log that the unit was explained, not discovered |
| "I get it", "이해함", "다음" | If the F question has not been asked yet, ask it once. If it was already asked, or the student declines it, mark the unit `[~] unchecked`, log it as a weak point, and go to G |
| "skip", "넘어가" | Mark `[~] skipped`, log it as a weak point, go to G |

## 4. End of Session

When the student stops: set `Last session`, set `Resume at:` to the exact unit, step and open question, append a Session Log line, and set `Status: done` only when every unit is `[x]` or `[~]`. Close with one line saying `/study` resumes here, and the open question. If the plan is finished, suggest the next step from Integration instead.

## 5. Resume

Read the plan, go to `Resume at:`, say in one line where we are and what was open ("U3 of 7, check question: you had computed the error at x = 2.1"), then ask the open question recorded there. If the resume was triggered by naming the material again, add one line saying the student can say "start over" to rebuild the plan. Apply the saved `Pace:`. Use the plan's Weak Points as the E trigger of the first unit where one applies.

## Anti-Patterns

Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/socratic-anti-patterns.md` before every study session. The most critical for `/study`:

- **Lecturing.** More than six lines before a question.
- **Several steps in one message.** The student only answers the last question. One step, one question.
- **Ticking a unit without F.** A good answer in C is not the check; run F.
- **Teaching from memory.** Statements come from the source pages in the plan. When going beyond the source, say: "This is not in your material, but…"

## Verification

Use one of these as the F question (two different ones at pace `slow`):

1. **Application**: "Apply this to [specific concrete case]."
2. **Counterexample**: "Give me a case where this does NOT apply."
3. **Prediction**: "If I changed [variable/condition], what would happen?"
4. **Restatement**: "State this in your own words without using [key term]."

## Integration

| Student state | Suggest |
|---|---|
| Plan finished, all units passed | `/exercise [range]` to practice, or `/quiz [range]` |
| Weak points logged | `/mistake` or `/exercise [weak unit]` |
| Wants to go deeper | `/whatif [scenario]`, `/derive [key formula]` |
| Wants to test themselves | `/feynman [concept]` |
| Struggled with prerequisites | `/prereq [unit]`, then `/study [prerequisite]` |
| Exam coming | `/exam-prep [range]` |

See `${CLAUDE_PLUGIN_ROOT}/skills/_shared/skill-integration-map.md` for the full flow.

## Example

U2 of a plan on limits, studying in Korean, steps A → B:

```
Claude: U2. 극한의 엄밀한 정의
        먼저 예측부터 해볼게요. f(x)=x², a=1에서 f(x)를 1과 0.1 이내로
        가깝게 만들려면, x는 1에서 얼마나 가까워야 할까요?

Student: 0.1 이내?

Claude: 직접 확인해 봐요. x = 1.09이면 |x² − 1|은 얼마예요?

Student: 0.1881... 넘네.

Claude: 그러니까 "얼마나 가까워야 하는지"는 목표 0.1에 따라 정해지는 값이에요.
        교재는 이 관계를 이렇게 적어요:
        $$\forall\varepsilon>0\ \exists\delta>0:\ 0<|x-a|<\delta \Rightarrow |f(x)-L|<\varepsilon$$
        ε과 δ 중 누가 먼저 정해지고, 왜 그 순서여야 할까요?
```
