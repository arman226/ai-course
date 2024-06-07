# Clauses and Conjunctive Normal Form (CNF)

## Introduction

In the context of propositional logic, **Conjunctive Normal Form (CNF)** is a way of structuring logical formulas. This format is particularly useful for automated theorem proving and logical inference. This document provides an overview of clauses, CNF, the process of converting logical formulas to CNF, and the method of inference by resolution.

## Clauses

### Definition

A **clause** is a disjunction (logical OR) of literals, where a literal is either a variable or its negation. For example:

- (P ∨ Q ∨ ¬R) is a clause.
- (¬A ∨ B) is also a clause.

### Types of Clauses

- **Unit Clause**: Contains a single literal. Example: (P)
- **Horn Clause**: Contains at most one positive literal. Example: (¬P ∨ ¬Q ∨ R)
- **Definite Clause**: A Horn clause with exactly one positive literal. Example: (¬P ∨ R)
- **Goal Clause**: A Horn clause with no positive literals. Example: (¬P ∨ ¬Q)

## Conjunctive Normal Form (CNF)

### Definition

A formula is in **Conjunctive Normal Form (CNF)** if it is a conjunction (logical AND) of clauses, where each clause is a disjunction of literals. For example:

- (P ∨ Q) ∧ (¬P ∨ R) ∧ (R ∨ ¬Q)

### Importance

CNF is significant in various areas of computer science, including:

- **Satisfiability Testing**: Algorithms like the DPLL algorithm and SAT solvers use CNF.
- **Resolution**: A rule of inference that works with CNF to derive conclusions from premises.

## Conversion to CNF

To convert a logical formula to CNF, follow these steps:

1. **Eliminate Bi-conditional (↔) and Implication (→)**:

   - Replace P ↔ Q with (P → Q) ∧ (Q → P)
   - Replace P → Q with ¬P ∨ Q

2. **Move NOTs inward** (using De Morgan's laws) until they apply directly to literals:

   - ¬(P ∨ Q) becomes (¬P ∧ ¬Q)
   - ¬(P ∧ Q) becomes (¬P ∨ ¬Q)
   - ¬(¬P) becomes P

3. **Distribute ORs over ANDs**:
   - Apply distributive laws to ensure the formula is in a conjunction of disjunctions.
   - Example: Distribute P ∨ (Q ∧ R) to (P ∨ Q) ∧ (P ∨ R)

### Example Conversion

Convert the formula (¬(P → Q) ∨ (R ↔ S)) to CNF.

1. Eliminate implications:
   ¬(¬P ∨ Q) ∨ ((R → S) ∧ (S → R))
2. Apply De Morgan's law:
   (P ∧ ¬Q) ∨ ((¬R ∨ S) ∧ (¬S ∨ R))
3. Distribute OR over AND:
   ((P ∧ ¬Q) ∨ (¬R ∨ S)) ∧ ((P ∧ ¬Q) ∨ (¬S ∨ R))
4. Distribute:
   (P ∨ ¬R ∨ S) ∧ (¬Q ∨ ¬R ∨ S) ∧ (P ∨ ¬S ∨ R) ∧ (¬Q ∨ ¬S ∨ R)

## Inference by Resolution

### Definition

**Resolution** is a rule of inference used for propositional and first-order logic. It involves combining pairs of clauses to produce new clauses until either a contradiction is found or no new clauses can be produced.

### Resolution Rule

If you have two clauses (A ∨ B) and (¬B ∨ C), you can resolve them to get (A ∨ C). The literal B and its negation ¬B cancel each other out.

### Resolution Process

1. **Convert all formulas to CNF**.
2. **Negate the statement you want to prove** and add it to the set of clauses.
3. **Apply the resolution rule** to derive new clauses.
4. **Repeat** until you derive an empty clause (contradiction) or no new clauses can be derived.

### Example

Given clauses:

1. (¬P ∨ Q)
2. (¬Q ∨ R)
3. P

To prove R:

1. Negate the goal: ¬R
2. Add ¬R to the set of clauses:

   - (¬P ∨ Q)
   - (¬Q ∨ R)
   - P
   - ¬R

3. Resolve:
   - From (¬Q ∨ R) and ¬R, derive ¬Q.
   - From (¬P ∨ Q) and ¬Q, derive ¬P.
   - From ¬P and P, derive an empty clause (contradiction).

Since a contradiction is found, R is proven.

## Conclusion

Understanding clauses, CNF, and inference by resolution is fundamental for logical reasoning and automated theorem proving. These concepts are widely used in fields such as computer science, artificial intelligence, and mathematical logic.

## References

- Introduction to Artificial Intelligence by Russell and Norvig
- Logic for Computer Science by Gallier
