"""Experiment 13 - Min-Max Algorithm.

Description: Read the leaf values of a full, uniform game tree and calculate
the value that the root player can guarantee under optimal play.

Theory: MAX chooses the largest child value and MIN chooses the smallest.
The recursive function divides the leaf list equally among each node's b
children and alternates the player at every level.
"""

leaves = list(map(float, input("Leaf values: ").split()))
b = int(input("Children per node: "))
is_max = input("Who plays at the root (max/min): ") == "max"


def minimax(values, is_max):
    """Alternate MAX and MIN until a leaf is reached."""
    if len(values) == 1:
        return values[0]
    size = len(values) // b
    answers = [
        minimax(values[i * size:(i + 1) * size], not is_max)
        for i in range(b)
    ]
    return max(answers) if is_max else min(answers)


best = minimax(leaves, is_max)
print("Value of root =", best)

