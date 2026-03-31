# Skill Integration Map

How SocraTeX skills chain together. Reference this when writing the Integration section of any skill.

## The Natural Study Flow

```
/prereq ──> /study ──> /exercise ──> /quiz
   │           │           │           │
   │           ├─> /whatif  │           ├─> /mistake ──> /exercise (targeted)
   │           ├─> /derive  │           │
   │           └─> /feynman │           └─> /flashcard
   │                        │
   │                        └─> /solve (if stuck)
   │
   └── gaps found ──> /study (prerequisite topic)
```

## Exam Prep Flow

```
/study-guide (with exam date) ──> /exam-prep ──> /mock-test ──> /review-test
                                                      │              │
                                                      └──────────────┴──> /mistake ──> /exercise
```

## Cross-Discipline Flow

```
/study ──> /relate ──> /roadmap
              │
              └─> /compare (similar concepts across fields)
```

## Skill-to-Skill Suggestions

After each skill, suggest the natural next step:

| After | Suggest |
|-------|---------|
| `/prereq` (ready) | `/study [topic]` |
| `/prereq` (gaps) | `/study [prerequisite]` |
| `/study` | `/exercise`, `/quiz`, `/feynman`, or `/whatif` |
| `/exercise` (done) | `/quiz` for breadth, `/mistake` if errors found |
| `/exercise` (stuck) | `/solve` to see a worked example |
| `/solve` | `/exercise` to try a similar one yourself |
| `/derive` | `/exercise` to apply the derived formula |
| `/feynman` (gaps found) | `/study [weak topic]` |
| `/feynman` (solid) | `/exercise` or `/quiz` |
| `/whatif` | Resume current `/study` or `/exercise` |
| `/quiz` (score < 7/10) | `/mistake` then `/exercise` on weak areas |
| `/quiz` (score >= 7/10) | `/flashcard` then next topic |
| `/mock-test` | `/review-test` for analysis, `/mistake` for errors |
| `/exam-prep` | `/mock-test` to practice, `/flashcard` to memorize |
| `/mistake` | `/exercise` targeting identified weak areas |
| `/study-guide` | Follow the recommended study order with `/study` |
| `/flashcard` | `/quiz` to test, `/feynman` for deep understanding |
| `/summary` | `/flashcard` to memorize, `/quiz` to test |
| `/compare` | `/exercise` to practice distinguishing the concepts |
| `/relate` | `/roadmap` for broader learning path |
| `/roadmap` | `/prereq` for the next recommended topic |
