# Inference Rules and Theorem Proving in Propositional Logic

## Introduction

Inference rules are the logical tools used to derive conclusions from premises. They are fundamental to logical reasoning, automated theorem proving, and artificial intelligence. This document provides an overview of several common inference rules, their definitions, and examples.

## Inference Rules

### Definition

Inference rules are principles or laws used to derive **valid conclusions** from premises. They are the foundation of logical reasoning and are used in various fields such as mathematics, computer science, and philosophy.

### Modus Ponens

**Definition**: If `P` implies `Q` (P → Q) and `P` is true, then `Q` must also be true.

**Symbolic Representation**:

1. P → Q
2. P

---

∴ Q

**Example**:

1. If it is raining, then the ground is wet.
2. It is raining.

---

∴ The ground is wet.

### Modus Tollens

**Definition**: If `P` implies `Q` (P → Q) and `Q` is false, then `P` must also be false.

**Symbolic Representation**:

1. P → Q
2. ¬Q

---

∴ ¬P

**Example**:

1. If it is raining, then the ground is wet.
2. The ground is not wet.

---

∴ It is not raining.

### Double Negation Elimination

**Definition**: If `P` is true, then `¬¬P` (not not `P`) is also true, and vice versa.

**Symbolic Representation**:

1. ¬¬P

---

∴ P

**Example**:

1. It is not true that it is not raining.

---

∴ It is raining.

### Biconditional Elimination

**Definition**: If `P` if and only if `Q` (P ↔ Q), then `P` implies `Q` and `Q` implies `P`.

**Symbolic Representation**:

1. P ↔ Q

---

∴ (P → Q) ∧ (Q → P)

**Example**:

1. The light is on if and only if the switch is up.

---

∴ If the light is on, the switch is up, and if the switch is up, the light is on.

### Implication Elimination (Material Implication)

**Definition**: If `P` implies `Q` (P → Q), it is equivalent to saying that `¬P` or `Q` is true.

**Symbolic Representation**:

1. P → Q

---

∴ ¬P ∨ Q

**Example**:

1. If it is raining, then the ground is wet.

---

∴ It is not raining or the ground is wet.

### De Morgan's Law

**Definition**: The negation of a conjunction is the disjunction of the negations, and vice versa.

**Symbolic Representation**:

1. ¬(P ∧ Q) ↔ (¬P ∨ ¬Q)
2. ¬(P ∨ Q) ↔ (¬P ∧ ¬Q)

**Example**:

1. It is not true that it is raining and cold.

---

∴ It is not raining or it is not cold.

### Reversed De Morgan's Law

**Definition**: The disjunction of the negations is the negation of the conjunction, and vice versa.

**Symbolic Representation**:

1. (¬P ∨ ¬Q) ↔ ¬(P ∧ Q)
2. (¬P ∧ ¬Q) ↔ ¬(P ∨ Q)

**Example**:

1. It is not raining or it is not cold.

---

∴ It is not true that it is raining and cold.

### Distributive Property

**Definition**: The conjunction distributes over the disjunction and vice versa.

**Symbolic Representation**:

1. P ∧ (Q ∨ R) ↔ (P ∧ Q) ∨ (P ∧ R)
2. P ∨ (Q ∧ R) ↔ (P ∨ Q) ∧ (P ∨ R)

**Example**:

1. It is raining and (the ground is wet or it is cold).

---

∴ (It is raining and the ground is wet) or (it is raining and it is cold).

## Theorem Proving

Theorem proving is the process of deriving a conclusion from a set of premises using inference rules. It involves systematically applying these rules to show that a given statement (theorem) logically follows from the premises.

### Steps in Theorem Proving:

1. **Identify the premises and the conclusion**: Clearly state the given information and what you need to prove.
2. **Apply inference rules**: Use the appropriate inference rules to derive new statements from the premises.
3. **Chain deductions**: Continue applying inference rules until you reach the conclusion.
4. **Verify the proof**: Ensure that each step logically follows from the previous ones and that the conclusion is reached.

### Example:

**Premises**:

1. If it is raining, then the ground is wet. (P → Q)
2. If the ground is wet, then the grass is growing. (Q → R)
3. It is raining. (P)

**Conclusion**:
∴ The grass is growing. (R)

**Proof**:

1. P → Q (Premise)
2. Q → R (Premise)
3. P (Premise)
4. Q (Modus Ponens on 1 and 3)
5. R (Modus Ponens on 2 and 4)

In this example, we have shown that the grass is growing (R) based on the given premises using the inference rules of Modus Ponens.

## Conclusion

Inference rules are essential tools in logical reasoning and theorem proving. By understanding and applying these rules, one can systematically derive conclusions from premises and solve complex logical problems.
