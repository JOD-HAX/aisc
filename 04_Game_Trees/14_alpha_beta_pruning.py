"""Experiment 14 - Alpha-Beta Pruning.

Description: Evaluate the same game tree as Min-Max while skipping branches
that cannot change the root decision.

Theory: Alpha is MAX's best guaranteed lower bound and beta is MIN's best
guaranteed upper bound. When alpha is at least beta, the remaining children
cannot affect the final choice and are pruned.
"""

leaves = list(map(float, input("Leaf values: ").split()))
b = int(input("Children per node: "))
is_max = input("Who plays at the root (max/min): ") == "max"


def alphabeta(values, is_max, alpha, beta):
    """Run Min-Max and stop when alpha becomes greater than beta."""
    if len(values) == 1:
        return values[0]
    size = len(values) // b
    if is_max:
        value = -1000
        for i in range(b):
            child = values[i * size:(i + 1) * size]
            value = max(value, alphabeta(child, False, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                print("Pruned remaining children of MAX node", values)
                break
        return value

    value = 1000
    for i in range(b):
        child = values[i * size:(i + 1) * size]
        value = min(value, alphabeta(child, True, alpha, beta))
        beta = min(beta, value)
        if alpha >= beta:
            print("Pruned remaining children of MIN node", values)
            break
    return value


best = alphabeta(leaves, is_max, -1000, 1000)
print("Value of root =", best)

