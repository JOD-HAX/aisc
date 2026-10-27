"""Experiment 01 - Discrete Perceptron (Unipolar).

Description: Read arbitrary training samples, starting parameters, learning
rate, and epoch limit, then train a single 0/1 perceptron.

Theory: The neuron applies a hard step to net = bias + sum(weight*input). On a
mistake, the perceptron rule adds c*(target-output)*input to each weight and
c*(target-output) to the bias until an epoch has no errors.
"""

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
    """Return 0 or 1 for one input."""
    net = sum(wi * xi for wi, xi in zip(w, x)) + b
    return 1 if net > 0 else 0


for epoch in range(1, max_epochs + 1):
    errors = 0
    for x, t in zip(X, T):
        o = predict(x)
        change = c * (t - o)
        if change != 0:
            w = [wi + change * xi for wi, xi in zip(w, x)]
            b += change
            errors += 1
    print("Epoch", epoch, "w =", w, "b =", b, "errors =", errors)
    if errors == 0:
        break

print("Final w =", w, "b =", b)
for x in X:
    print(x, "->", predict(x))

