# Common STEM Mistakes by Subject

Reference for the `/mistake` skill. Use this to supplement the student's actual error analysis with preventive warnings about mistakes they haven't made yet.

## Mathematics

### Algebra & Precalculus
- Distributing exponents over sums: $(a+b)^2 \neq a^2 + b^2$
- Canceling terms instead of factors: $\frac{x+3}{x} \neq 3$
- Forgetting domain restrictions when simplifying (dividing by zero)
- Log/exponent confusion: $\log(a+b) \neq \log a + \log b$

### Calculus
- Chain rule omission: $\frac{d}{dx}\sin(3x) \neq \cos(3x)$ (missing factor of 3)
- Treating $dx$ as optional notation rather than part of the integral
- Swapping limit and integral/sum without justification
- Confusing convergence of terms $a_n \to 0$ with convergence of series $\sum a_n$
- Integration by parts: choosing $u$ and $dv$ poorly, leading to more complex integrals

### Linear Algebra
- Assuming $AB = BA$ (matrix multiplication is not commutative)
- Confusing row space with column space
- Forgetting that $\det(A+B) \neq \det A + \det B$
- Applying scalar rules to matrices: $(A+B)^2 \neq A^2 + 2AB + B^2$

### Analysis
- Confusing pointwise and uniform convergence
- Assuming continuous implies differentiable
- Swapping $\forall \exists$ and $\exists \forall$ quantifier order in epsilon-delta proofs

## Physics

### Mechanics
- Sign errors in free-body diagrams (wrong direction for normal force, tension)
- Confusing velocity and acceleration directions
- Using $v = v_0 + at$ when acceleration is not constant
- Forgetting to convert units (mixing kg/g, m/cm)
- Applying energy conservation when non-conservative forces do work

### Electromagnetism
- Confusing electric field $\vec{E}$ direction (away from positive, toward negative)
- Sign errors in Lenz's law (induced EMF opposes change)
- Using Coulomb's law for non-point charges without integration
- Forgetting that $V$ is a scalar while $\vec{E}$ is a vector

### Thermodynamics
- Confusing heat and temperature
- Sign convention errors: $Q > 0$ means heat INTO the system
- Applying ideal gas law when conditions aren't ideal
- Forgetting that entropy of the universe always increases (not just the system)

### Waves & Optics
- Confusing transverse and longitudinal wave properties
- Sign errors in thin lens equation
- Forgetting phase changes on reflection

## Chemistry

### Stoichiometry
- Not balancing equations before calculating
- Forgetting to identify the limiting reagent
- Molar mass errors (using atomic number instead of atomic mass)
- Volume ratio errors (assuming equal volumes mean equal moles)

### Equilibrium
- Confusing $K$ and $Q$ (equilibrium constant vs reaction quotient)
- Thinking a catalyst changes equilibrium position (it doesn't)
- Le Chatelier's principle: confusing adding a reactant with increasing concentration when volume changes

### Acid-Base
- Confusing strong/weak with concentrated/dilute
- Forgetting water's autoionization contribution at very low concentrations
- pH calculation errors: $\text{pH} = -\log[\text{H}^+]$, not $\log[\text{H}^+]$

### Organic Chemistry
- Confusing nucleophile/electrophile roles
- Forgetting stereochemistry implications (SN1 vs SN2 inversion)
- Drawing resonance structures that violate octet rule

## Statistics

### Probability
- Adding probabilities of non-mutually-exclusive events without subtracting overlap
- Confusing $P(A|B)$ with $P(B|A)$ (prosecutor's fallacy)
- Assuming independence without justification

### Hypothesis Testing
- Confusing Type I and Type II errors
- Interpreting p-value as probability the null is true
- Using z-test when sample is small and population variance unknown (should use t-test)
- One-tailed vs two-tailed test mismatch with the research question

### Regression
- Interpreting correlation as causation
- Extrapolating beyond the data range
- Ignoring heteroscedasticity or non-normality of residuals
- Confusing $R^2$ with goodness of fit when comparing models with different numbers of predictors

## Cross-Subject Patterns

These mistakes appear across all STEM subjects:

| Pattern | Example |
|---------|---------|
| Unit neglect | Mixing meters and centimeters, forgetting mol vs molecules |
| Sign errors | Dropped negatives in derivatives, forces, charges, $\Delta G$ |
| Implicit assumption | "Obviously this is linear" without checking |
| Formula memorization without understanding | Applying a formula outside its valid conditions |
| Off-by-one in discrete contexts | Fencepost errors in sums, series indices, combinatorics |
| Notation conflation | Using the same symbol for two different things within one problem |
