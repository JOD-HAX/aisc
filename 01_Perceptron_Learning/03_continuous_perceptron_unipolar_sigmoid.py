"""Experiment 03 - Continuous Perceptron, Unipolar Sigmoid.

Description: Train a smooth 0-to-1 neuron from user-entered samples and stop
when total squared error is small or the epoch limit is reached.

Theory: Sigmoid activation has derivative output*(1-output). Gradient learning
multiplies the error by this derivative and the input, producing gradual weight
and bias changes on every sample.
"""

import math

n = int(input("Number of samples: "))
X = []
T = []
for i in range(n):
    row = list(map(float, input("Sample " + str(i + 1) + " (x1 x2 target): ").split()))
    X.append(row[:-1])
    T.append(row[-1])

w = list(map(float, input("Initial weights: ").split()))
b = float(input("Initial bias: "))
c = float(input("Learning rate: "))
max_epochs = int(input("Max epochs: "))


def predict(x):
    """Return a smooth value between 0 and 1."""
    net = sum(wi * xi for wi, xi in zip(w, x)) + b
    return 1 / (1 + math.exp(-net))


for epoch in range(1, max_epochs + 1):
    error = 0
    for x, t in zip(X, T):
        o = predict(x)
        delta = c * (t - o) * o * (1 - o)
        w = [wi + delta * xi for wi, xi in zip(w, x)]
        b += delta
        error += 0.5 * (t - o) ** 2
    if epoch % 500 == 0:
        print("Epoch", epoch, "w =", w, "b =", b, "error =", round(error, 4))
    if error < 0.01:
        break

print("Stopped at epoch", epoch)
print("Final w =", w, "b =", b)
for x in X:
    o = predict(x)
    print(x, "->", round(o, 3), "class", 1 if o > 0.5 else 0)

