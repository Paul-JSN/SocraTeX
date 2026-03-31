# Socratic Questioning Techniques

Reference guide for question sub-techniques used across all interactive SocraTeX skills. Each technique includes concrete STEM examples to illustrate proper usage.

## 1. Clarification Questions

Purpose: Force the student to define vague terms and sharpen their thinking.

Template: "What do you mean by...?" / "Can you put that another way?"

| Subject | Example |
|---------|---------|
| Math | Student says "the function blows up." Ask: "What do you mean by 'blows up'? Does it approach infinity, oscillate, or become undefined?" |
| Physics | Student says "the force cancels out." Ask: "Which specific forces are you referring to, and what do you mean by 'cancel' — zero net force, or something else?" |
| Chemistry | Student says "the reaction goes to completion." Ask: "What does 'completion' mean here? Is the equilibrium constant relevant?" |

## 2. Probing Assumptions

Purpose: Surface hidden assumptions the student is making without realizing it.

Template: "What are we assuming here?" / "Is that always true?"

| Subject | Example |
|---------|---------|
| Statistics | Student applies a t-test. Ask: "What assumptions does the t-test require? Have we checked whether this data satisfies them?" |
| Math | Student says $\sum a_n b_n$ converges. Ask: "What are you assuming about $a_n$ and $b_n$ individually? Does convergence of each guarantee convergence of the product?" |
| Engineering | Student models a beam as rigid. Ask: "Under what conditions is the rigid-body assumption valid here? What happens if the beam deflects significantly?" |

## 3. Probing Evidence and Reasoning

Purpose: Demand justification rather than accepting claims at face value.

Template: "How do we know that?" / "What's the evidence for that step?"

| Subject | Example |
|---------|---------|
| Physics | Student writes $E = \frac{1}{2}mv^2$. Ask: "How do we know kinetic energy takes this form? Where does this come from?" |
| Chemistry | Student says "NaCl dissolves because it's ionic." Ask: "Plenty of ionic compounds are insoluble. What specifically about NaCl and water makes this work?" |
| Math | Student claims a series converges. Ask: "Which convergence test did you apply, and can you show me the conditions are met?" |

## 4. Exploring Implications and Consequences

Purpose: Push the student to follow their reasoning to its logical conclusion, especially to find contradictions.

Template: "If that's true, then what follows?" / "What would that predict about...?"

| Subject | Example |
|---------|---------|
| Physics | Student says heavier objects fall faster. Ask: "If that's true, what happens if I tie a heavy and light object together? Is the combined object heavier or lighter than the heavy one alone? Does it fall faster or slower?" |
| Economics | Student says raising minimum wage always causes unemployment. Ask: "If that's true, what does the model predict about cities that recently raised their wage? Can we check?" |
| Statistics | Student says $p = 0.03$ means there's a 3% chance the null hypothesis is true. Ask: "If that's what p-values mean, then what would $p = 0.99$ tell us? Does that match how we actually use p-values?" |

## 5. Questioning the Question

Purpose: Step back and examine why we are asking a particular question or solving a particular problem. Builds metacognitive awareness.

Template: "Why is this question important?" / "What would change if we knew the answer?"

| Subject | Example |
|---------|---------|
| Math | Before proving a theorem, ask: "Why do we care whether this space is complete? What breaks if it isn't?" |
| Chemistry | Before balancing a redox reaction, ask: "Why does it matter which species is oxidized vs reduced? What does that tell us about the chemistry?" |
| Engineering | Before optimizing a transfer function, ask: "What physical behavior are we actually trying to achieve? What happens to the real system if we get this wrong?" |

## Choosing the Right Technique

Match the technique to the moment in the dialogue:

| Student behavior | Best technique |
|------------------|---------------|
| Uses vague or informal language | Clarification |
| Skips a logical step or assumes something unstated | Probing assumptions |
| Makes a claim without justification | Probing evidence |
| Gives a confident but potentially wrong answer | Exploring implications (to surface contradictions) |
| Is mechanically correct but does not see the bigger picture | Questioning the question |

## Usage Notes

- Use one technique per message. Do not stack multiple question types.
- Match the technique to the moment: use clarification early, implications when the student is confident, assumptions when they skip steps.
- If a technique is not producing insight after 2 attempts, switch to a different one.
- Combine with verification checks from the `/study` skill: after questioning reveals understanding, confirm with an application or counterexample test.
- See `_shared/socratic-anti-patterns.md` for what NOT to do when questioning.
