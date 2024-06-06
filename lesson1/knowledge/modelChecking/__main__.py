from itertools import product


def enumerate_models(symbols):
    """
    Enumerate all possible models given a list of symbols.
    """
    num_symbols = len(symbols)
    models = []

    for p in product([True, False], repeat=num_symbols):
        model = dict(zip(symbols, p))
        models.append(model)

    return models

def entails(KB, alpha):
    """
    Determine if KB entails alpha using model enumeration.
    """
    symbols = set()
    symbols.update(KB)
    symbols.update(alpha)

    models = enumerate_models(list(symbols))


    for model in models:
        satisfies_KB = all(eval(expression, model) for expression in KB)
        if satisfies_KB and not eval(alpha, model):
            return False

    return True

# Example usage:
KB = ['P', 'Q', '(not P or Q)']
alpha = 'Q'

print("KB entails alpha:", entails(KB, alpha))
