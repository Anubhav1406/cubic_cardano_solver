# Cubic Equation Solver using Cardano's Method

This project implements a complete solver for cubic equations using **Cardano’s method**, extended to handle **complex coefficients** and **high-precision arithmetic**.

Unlike typical implementations that rely on libraries or numerical approximations, this approach reconstructs the solution **from first principles**, including proper handling of complex cube roots, branch selection, and numerical refinement.

---

## 🧠 Idea

We solve the general cubic:

ax³ + bx² + cx + d = 0

by transforming it into a simpler form called the **depressed cubic**:

μ³ = Aμ + B

This is achieved by eliminating the quadratic term through a carefully chosen shift:

x = μ - b / (3a)

We then express:

μ = α + β

which reduces the problem to solving a quadratic in terms of α³ and β³.

---

## ⚙️ Method

### Steps:

1. **Normalize equation**

   * Divide by `a`

2. **Eliminate quadratic term**

   * Use substitution: `x = μ - b/(3a)`

3. **Reduce to depressed cubic**

   * μ³ = Aμ + B

4. Substitute μ = α + β

   We expand:

   μ³ = α³ + β³ + 3αβ(α + β)

   To simplify the expression, we **choose** α and β such that:

   αβ = A / 3

   This cancels the middle term, reducing the equation to:

   α³ + β³ = B

5. **Solve quadratic**

   * u² - Bu + A³/27 = 0

6. **Compute cube roots (complex)**

   * Convert to polar form
   * Generate all cube roots

7. **Match valid root pairs**

   * Ensure αβ = A/3

8. **Recover roots**

   * x = α + β - b/(3a)

9. **Newton refinement (2 iterations)**

   * Improve numerical accuracy of computed roots

---

## 🚀 Features

* Handles **complex coefficients**
* Uses **high-precision arithmetic (mpmath)**
* Correctly resolves **multi-valued cube roots**
* Implements **root pairing logic** for valid solutions
* Includes **Newton-based refinement**
* Includes **automated residual verification across 50+ stress-tested cases**
* Fully derived and explained in notebook

---

## 🧪 Testing & Validation

To ensure correctness and numerical stability, the solver was evaluated using an automated test pipeline.

### Test Setup

* A file `Testcases.txt` stores multiple cubic equations (real and complex coefficients)
* A script `test.py` feeds each testcase into the solver
* Output is redirected and analyzed via:

python test.py > output.txt

### Output Format

For each testcase:

* Line 1: coefficients (a, b, c, d)
* Next 3 lines: computed roots
* Final line: residual errors
  → |f(r₁)|, |f(r₂)|, |f(r₃)|

---

## 📊 Validation Results

* Residual errors consistently observed in the range:

  * ~10⁻⁵⁰ for high-precision cases
  * ~10⁻¹⁷ near floating-point limits

* Correct handling of:

  * Repeated roots (with minimal imaginary artifacts)
  * Ill-conditioned polynomials
  * Large and small coefficient scales
  * Complex-valued coefficients

---

## ⚠️ Numerical Notes

* Small imaginary components (~1e-6 or lower) may appear for theoretically real roots due to floating-point and branch cut effects
* Residual verification confirms correctness despite such artifacts

---

## 📊 Example Input

1 0 -1 1

or complex:

1+2j 0 -3 4j

---

## 📌 Output

* All three roots (real or complex)
* Residual error for each root

Example:

Roots:
r1 = 1.3247
r2 = -0.6624 + 0.5623j
r3 = -0.6624 - 0.5623j

Residuals |f(r)|:
~ 1e-50

---

## ⚠️ Key Insight

The challenge in Cardano’s method is not solving the equation itself, but:

* handling **complex cube roots**
* selecting the correct **branch combinations**
* maintaining **numerical stability**

A naive implementation often produces incorrect roots due to improper pairing.

---

## 🛠️ Requirements

pip install mpmath

---

## ▶️ Run

python cubic_cardano_solver.py

---

## 📁 Files

cubic_cardano_solver.py        → clean implementation
cubic_cardano_derivation.ipynb → full derivation and explanation
test.py                        → automated testing pipeline
Testcases.txt                  → input dataset for testing

---

## 🧩 What Makes This Interesting

This project shows how:

* A nonlinear cubic can be reduced to a **quadratic in disguise**
* Algebraic manipulation leads directly to a **computational algorithm**
* Classical mathematics can be combined with numerical refinement for high-precision results
* Analytical solutions can be made computationally robust with careful implementation

---

## 🧠 Author’s Note

This implementation focuses on understanding *why* the method works, not just applying it.

Cardano’s formula is often presented as a final result, but its real power lies in the transformation process — reducing complexity step by step until the solution becomes accessible.

This project attempts to reconstruct that journey while ensuring practical numerical reliability.