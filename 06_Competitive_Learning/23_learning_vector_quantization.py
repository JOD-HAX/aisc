"""Experiment 23 - Learning Vector Quantization (LVQ).

Description: Read labeled inputs and labeled prototypes, then attract a winning
prototype toward a same-class sample or repel it from a different-class sample.

Theory: LVQ is supervised competitive learning. The nearest prototype wins,
but the known class label determines the update sign. Final classification uses
the class belonging to the nearest learned prototype.
"""

n = int(input("Number of inputs: "))
X = []
T = []
for i in range(n):
    row = list(map(float, input("Input " + str(i + 1) + " (x1 x2 class): ").split()))
    X.append(row[:-1])
    T.append(int(row[-1]))

m = int(input("Number of neurons: "))
W = []
C = []
for i in range(m):
    row = list(map(float, input("Neuron " + str(i) + " (w1 w2 class): ").split()))
    W.append(row[:-1])
    C.append(int(row[-1]))

alpha = float(input("Learning rate: "))
decay = float(input("Learning rate multiplier after each epoch (0.5 halves it, 1 keeps it): "))
epochs = int(input("Epochs: "))


def distance(x, w):
    """Return squared Euclidean distance."""
    return sum((xi - wi) ** 2 for xi, wi in zip(x, w))


for epoch in range(1, epochs + 1):
    for x, t in zip(X, T):
        winner = min(range(m), key=lambda i: distance(x, W[i]))
        sign = 1 if C[winner] == t else -1
        W[winner] = [
            wi + sign * alpha * (xi - wi)
            for xi, wi in zip(x, W[winner])
        ]
    alpha *= decay
    print("Epoch", epoch, "W =", [[round(v, 2) for v in w] for w in W])

print("Final W =", [[round(v, 2) for v in w] for w in W])
for x in X:
    winner = min(range(m), key=lambda i: distance(x, W[i]))
    print(x, "-> class", C[winner])
