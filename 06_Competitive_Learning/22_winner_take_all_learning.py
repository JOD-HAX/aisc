"""Experiment 22 - Winner-Take-All Learning.

Description: Read unlabeled input vectors and starting neuron weights, then
move only the closest neuron toward each input over several epochs.

Theory: Squared Euclidean distance selects the winner. The update moves that
prototype by alpha*(input-weight); competing losers do not change. Decaying
alpha allows large early movement and smaller later adjustments.
"""

n = int(input("Number of inputs: "))
X = []
for i in range(n):
    X.append(list(map(float, input("Input " + str(i + 1) + ": ").split())))

m = int(input("Number of neurons: "))
W = []
for i in range(m):
    W.append(list(map(float, input("Weights of neuron " + str(i) + ": ").split())))

alpha = float(input("Learning rate: "))
decay = float(input("Learning rate multiplier after each epoch (0.5 halves it, 1 keeps it): "))
epochs = int(input("Epochs: "))


def distance(x, w):
    """Return squared Euclidean distance."""
    return sum((xi - wi) ** 2 for xi, wi in zip(x, w))


for epoch in range(1, epochs + 1):
    for x in X:
        winner = min(range(m), key=lambda i: distance(x, W[i]))
        W[winner] = [wi + alpha * (xi - wi) for xi, wi in zip(x, W[winner])]
    alpha *= decay
    print("Epoch", epoch, "W =", [[round(v, 2) for v in w] for w in W])

print("Final W =", [[round(v, 2) for v in w] for w in W])
for x in X:
    winner = min(range(m), key=lambda i: distance(x, W[i]))
    print(x, "-> winner neuron", winner)

