# Subject Adaptation Guide

Reference for adapting SocraTeX skill behavior to the detected subject. All skills that do subject detection should consult this guide.

## Detection Signals

| Subject | Key Indicators |
|---------|---------------|
| Math | theorem, proof, lemma, corollary, epsilon-delta, ∀, ∃, ℝ, ℤ, convergence, continuous, differentiable |
| Physics | force, mass, velocity, acceleration, energy, momentum, units (m/s, N, J, kg), Newton, Maxwell |
| Chemistry | reaction, molecule, equilibrium, molar, pH, element symbols (H, O, C, Na), bond, orbital |
| Statistics | distribution, probability, hypothesis, p-value, confidence interval, regression, sample, variance |
| Economics | utility, marginal, equilibrium, demand, supply, elasticity, cost function, profit maximization |
| Engineering | transfer function, impedance, bandwidth, signal, circuit, control system, Laplace, Fourier |

## How Each Subject Changes Behavior

### Proof / Derivation Style

| Subject | Style |
|---------|-------|
| Math | Formal logical proof. State theorem, assumptions, each step with justification. ε-δ, induction, contradiction |
| Physics | Physical derivation. Start from a law, apply to specific system, check units at each step, verify with limiting cases |
| Chemistry | Mechanism-based. Show electron movement, track atoms, balance everything, verify stoichiometry |
| Statistics | Assumption → model → computation → interpretation. Always check assumptions first, always interpret in context last |
| Economics | Model setup → optimization → equilibrium conditions. State assumptions explicitly, check second-order conditions |
| Engineering | System modeling → transform domain → analysis → back-transform. Block diagrams, transfer functions |

### Problem-Solving Approach

| Subject | First Step | Verification |
|---------|-----------|-------------|
| Math | "What technique applies?" | Check boundary cases, verify conditions |
| Physics | "Draw a diagram. List knowns and unknowns" | Check units, test limiting cases (m→0, t→∞) |
| Chemistry | "Write the balanced equation" | Conservation of mass, charge balance |
| Statistics | "State the null and alternative hypotheses" | Check assumptions, interpret in context |
| Economics | "Write the objective function and constraints" | Check second-order conditions, economic interpretation |
| Engineering | "Draw the block diagram / circuit diagram" | Stability check, frequency response |

### Notation Conventions

| Subject | Convention |
|---------|-----------|
| Math | $f: \mathbb{R} \to \mathbb{R}$, $\forall \epsilon > 0$, $\sum_{n=1}^{\infty}$ |
| Physics | $\vec{F} = m\vec{a}$, units always: $v = 3.0 \text{ m/s}$, significant figures |
| Chemistry | $\ce{2H2 + O2 -> 2H2O}$, $K_{eq}$, $\Delta G$, $[\text{H}^+]$ |
| Statistics | $H_0: \mu = \mu_0$, $\bar{x}$, $s^2$, $P(X \leq x)$, $\hat{\beta}$ |
| Economics | $\max_{x} U(x)$ s.t. $p \cdot x \leq m$, $MR = MC$, $\frac{\partial}{\partial x}$ |
| Engineering | $H(s) = \frac{Y(s)}{X(s)}$, $j\omega$, $|H(j\omega)|$ dB |

### Visualization Style

| Subject | Primary Diagrams |
|---------|-----------------|
| Math | Graphs, set diagrams, number lines, ε-δ illustrations |
| Physics | Free-body diagrams, circuit diagrams, vector fields, phase diagrams |
| Chemistry | Molecular structures, orbital diagrams, energy level diagrams, reaction coordinate plots |
| Statistics | Distributions, scatter plots, box plots, Q-Q plots |
| Economics | Supply-demand curves, indifference curves, production possibility frontiers |
| Engineering | Block diagrams, Bode plots, root locus, circuit schematics |

### Common Mistakes by Subject

| Subject | Top Mistakes |
|---------|-------------|
| Math | Forgetting conditions on theorems, wrong direction of implication, sign errors in algebra |
| Physics | Unit inconsistency, wrong reference frame, forgetting vector nature of forces |
| Chemistry | Unbalanced equations, confusing molarity/molality, wrong oxidation states |
| Statistics | P-value misinterpretation, confusing correlation/causation, ignoring assumptions |
| Economics | Confusing marginal/average, ignoring constraints, wrong optimization direction |
| Engineering | Stability assumptions, forgetting initial conditions, impedance mismatch |
