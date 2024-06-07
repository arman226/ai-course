class LogicConverter:
    def __init__(self):
        pass

    @staticmethod
    def eliminate_biconditional(expression):
        """
        Eliminate biconditional (↔) by rewriting P ↔ Q as (P → Q) ∧ (Q → P)
        """
        if isinstance(expression, list) and expression[0] == '↔':
            p = expression[1]
            q = expression[2]
            return ['∧', ['→', p, q], ['→', q, p]]
        return expression

    @staticmethod
    def eliminate_implication(expression):
        """
        Eliminate implication (→) by rewriting P → Q as ¬P ∨ Q
        """
        if isinstance(expression, list) and expression[0] == '→':
            p = expression[1]
            q = expression[2]
            return ['∨', ['¬', p], q]
        return expression

    @staticmethod
    def move_not_inward(expression):
        """
        Move NOTs inward using De Morgan's laws
        """
        if isinstance(expression, list) and expression[0] == '¬':
            sub_expr = expression[1]
            if isinstance(sub_expr, list):
                if sub_expr[0] == '¬':
                    return LogicConverter.move_not_inward(sub_expr[1])  # ¬(¬P) => P
                elif sub_expr[0] == '∧':
                    return ['∨', ['¬', sub_expr[1]], ['¬', sub_expr[2]]]  # ¬(P ∧ Q) => ¬P ∨ ¬Q
                elif sub_expr[0] == '∨':
                    return ['∧', ['¬', sub_expr[1]], ['¬', sub_expr[2]]]  # ¬(P ∨ Q) => ¬P ∧ ¬Q
        return expression

    @staticmethod
    def distribute_or_over_and(expression):
        """
        Distribute OR over AND to convert to CNF
        """
        if isinstance(expression, list) and expression[0] == '∨':
            p = expression[1]
            q = expression[2]
            if isinstance(p, list) and p[0] == '∧':
                a = p[1]
                b = p[2]
                return ['∧', ['∨', a, q], ['∨', b, q]]  # P ∨ (Q ∧ R) => (P ∨ Q) ∧ (P ∨ R)
            if isinstance(q, list) and q[0] == '∧':
                a = q[1]
                b = q[2]
                return ['∧', ['∨', p, a], ['∨', p, b]]  # (P ∧ Q) ∨ R => (P ∨ R) ∧ (Q ∨ R)
        return expression

    @staticmethod
    def to_cnf(expression):
        """
        Convert an arbitrary logical expression to CNF
        """
        expression = LogicConverter.eliminate_biconditional(expression)
        expression = LogicConverter.eliminate_implication(expression)
        expression = LogicConverter.move_not_inward(expression)
        expression = LogicConverter.distribute_or_over_and(expression)
        
        # Recursively process any sub-expressions
        if isinstance(expression, list):
            return [expression[0]] + [LogicConverter.to_cnf(sub_expr) for sub_expr in expression[1:]]
        return expression

# Example usage
if __name__ == "__main__":
    logic_expr = ['¬', ['→', 'P', 'Q']]  # ¬(P → Q)
    cnf_expr = LogicConverter.to_cnf(logic_expr)
    print(f"Original expression: {logic_expr}")
    print(f"CNF expression: {cnf_expr}")

    logic_expr = ['↔', 'R', 'S']  # (R ↔ S)
    cnf_expr = LogicConverter.to_cnf(logic_expr)
    print(f"Original expression: {logic_expr}")
    print(f"CNF expression: {cnf_expr}")
