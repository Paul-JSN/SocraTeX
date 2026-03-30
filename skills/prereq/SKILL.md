---
name: prereq
description: Use when the user wants to check prerequisite knowledge before studying a topic. Identifies what the student needs to know first and tests readiness. Works with any STEM subject
---

If `socratex.config.md` exists, read it for settings. Otherwise use defaults: study_language=en, show_original_terms=false, difficulty=adaptive, hints_before_answer=3, render_mode=desktop, subject=auto.

Parse $ARGUMENTS to identify the target topic (e.g., "chapter 5", "Fourier transform", "thermodynamics", "multiple regression").

Find relevant textbook content if available. Detect the subject. Adapt prerequisite expectations to the subject's conventions.

**1. Prerequisite Map**

Identify all concepts the student should know before tackling this topic. Organize by layer:

```
Target: [topic]
├── Must know (blocking): [concepts that make this topic impossible without them]
├── Should know (helpful): [concepts that make this topic much easier]
└── Nice to know (context): [background that deepens understanding]
```

For each prerequisite, give a one-line description of why it matters for the target topic.

**2. Quick Readiness Check**

Ask 3-5 rapid diagnostic questions that test the "must know" prerequisites. These should be quick to answer — not full exercises, just concept checks:
- "What is [prerequisite concept]?"
- "True or false: [statement about prerequisite]"
- "Fill in: [key formula or definition]"

Give immediate feedback after each answer.

**3. Verdict**

Based on the readiness check:
- **Ready** → "You're good to go. Start with `/study [topic]`"
- **Gaps found** → List specific gaps and recommend: "Review [prerequisite] first with `/study [prerequisite]`, then come back"
- **Major gaps** → "You need to build up to this. Here's the recommended study path: [ordered list]"

This is interactive chat — do NOT write to session.md.
