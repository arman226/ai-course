class Logic:
    def __init__(self):
        pass

    @staticmethod
    def modus_ponens(p, p_implies_q):
        """
        Modus Ponens: If 'P' implies 'Q' (P → Q) and 'P' is true, then 'Q' must also be true.
        
        :param p: Boolean, value of P
        :param p_implies_q: Boolean, value of P → Q
        :return: Boolean, value of Q
        """
        if p and p_implies_q:
            return True
        return False

    @staticmethod
    def modus_tollens(p_implies_q, not_q):
        """
        Modus Tollens: If 'P' implies 'Q' (P → Q) and 'Q' is false, then 'P' must also be false.
        
        :param p_implies_q: Boolean, value of P → Q
        :param not_q: Boolean, value of ¬Q
        :return: Boolean, value of ¬P
        """
        if p_implies_q and not_q:
            return False
        return True

    @staticmethod
    def double_negation_elimination(not_not_p):
        """
        Double Negation Elimination: If '¬¬P' is true, then 'P' is true.
        
        :param not_not_p: Boolean, value of ¬¬P
        :return: Boolean, value of P
        """
        return not_not_p

    @staticmethod
    def biconditional_elimination(p_biconditional_q):
        """
        Biconditional Elimination: If 'P' if and only if 'Q' (P ↔ Q), then 'P' implies 'Q' and 'Q' implies 'P'.
        
        :param p_biconditional_q: Boolean, value of P ↔ Q
        :return: Tuple(Boolean, Boolean), values of P → Q and Q → P
        """
        p_implies_q = p_biconditional_q
        q_implies_p = p_biconditional_q
        return p_implies_q and q_implies_p

    @staticmethod
    def implication_elimination(p_implies_q):
        """
        Implication Elimination: If 'P' implies 'Q' (P → Q), it is equivalent to saying that '¬P' or 'Q' is true.
        
        :param p_implies_q: Tuple(Boolean, Boolean), values of P and Q
        :return: Boolean, value of ¬P ∨ Q
        """
        not_p_or_q = not p_implies_q[0] or p_implies_q[1]
        return not_p_or_q

    @staticmethod
    def de_morgans_law(not_p_and_q):
        """
        De Morgan's Law: The negation of a conjunction is the disjunction of the negations.
        
        :param not_p_and_q: Tuple(Boolean, Boolean), values of ¬P and Q
        :return: Boolean, value of ¬(P ∧ Q) ↔ ¬P ∨ ¬Q
        """
        return not not_p_and_q[0] or not not_p_and_q[1]

    @staticmethod
    def reversed_de_morgans_law(not_p_or_q):
        """
        Reversed De Morgan's Law: The disjunction of the negations is the negation of the conjunction.
        
        :param not_p_or_q: Tuple(Boolean, Boolean), values of ¬P and Q
        :return: Boolean, value of (¬P ∨ ¬Q) ↔ ¬(P ∧ Q)
        """
        return not (not not_p_or_q[0] and not not_p_or_q[1])

    @staticmethod
    def distributive_property_and(p, q_or_r):
        """
        Distributive Property (AND over OR): P ∧ (Q ∨ R) ↔ (P ∧ Q) ∨ (P ∧ R)
        
        :param p: Boolean, value of P
        :param q_or_r: Tuple(Boolean, Boolean), values of Q and R
        :return: Boolean, value of (P ∧ Q) ∨ (P ∧ R)
        """
        return (p and q_or_r[0]) or (p and q_or_r[1])

    @staticmethod
    def distributive_property_or(p, q_and_r):
        """
        Distributive Property (OR over AND): P ∨ (Q ∧ R) ↔ (P ∨ Q) ∧ (P ∨ R)
        
        :param p: Boolean, value of P
        :param q_and_r: Tuple(Boolean, Boolean), values of Q and R
        :return: Boolean, value of (P ∨ Q) ∧ (P ∨ R)
        """
        return (p or q_and_r[0]) and (p or q_and_r[1])

    @staticmethod
    def theorem_proving(p, p_implies_q, q_implies_r):
        """
        Theorem Proving: Given premises P, P → Q, and Q → R, prove R.
        
        :param p: Boolean, value of P
        :param p_implies_q: Boolean, value of P → Q
        :param q_implies_r: Boolean, value of Q → R
        :return: Boolean, value of R
        """
        q = Logic.modus_ponens(p, p_implies_q)
        r = Logic.modus_ponens(q, q_implies_r)
        return r

# Example usage
logic = Logic()

# Modus Ponens example
p = True
p_implies_q = True
print(f"Modus Ponens: {logic.modus_ponens(p, p_implies_q)}")  # Should return True

# Modus Tollens example
p_implies_q = True
not_q = True
print(f"Modus Tollens: {logic.modus_tollens(p_implies_q, not_q)}")  # Should return False

# Double Negation Elimination example
not_not_p = True
print(f"Double Negation Elimination: {logic.double_negation_elimination(not_not_p)}")  # Should return True

# Biconditional Elimination example
p_biconditional_q = True
print(f"Biconditional Elimination: {logic.biconditional_elimination(p_biconditional_q)}")  # Should return True

# Implication Elimination example
p_implies_q = (True, True)
print(f"Implication Elimination: {logic.implication_elimination(p_implies_q)}")  # Should return True

# De Morgan's Law example
not_p_and_q = (False, False)
print(f"De Morgan's Law: {logic.de_morgans_law(not_p_and_q)}")  # Should return True

# Reversed De Morgan's Law example
not_p_or_q = (False, False)
print(f"Reversed De Morgan's Law: {logic.reversed_de_morgans_law(not_p_or_q)}")  # Should return True

# Distributive Property (AND over OR) example
p = True
q_or_r = (False, True)
print(f"Distributive Property (AND over OR): {logic.distributive_property_and(p, q_or_r)}")  # Should return True

# Distributive Property (OR over AND) example
p = False
q_and_r = (True, False)
print(f"Distributive Property (OR over AND): {logic.distributive_property_or(p, q_and_r)}")  # Should return False

# Theorem Proving example
p = True
p_implies_q = True
q_implies_r = True
print(f"Theorem Proving: {logic.theorem_proving(p, p_implies_q, q_implies_r)}")  # Should return True
