"""Experiment 02 - Discrete Perceptron, Bipolar Binary.

Description: Train a single perceptron from user-entered -1/+1 samples and
parameters.

Theory: This uses the same error-correction rule as the unipolar perceptron,
but the step returns -1 for a non-positive net and +1 for a positive net.
Because target-output can be +/-2, bipolar corrections can be larger.
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
    """Return -1 or +1 for one input."""
    net = sum(wi * xi for wi, xi in zip(w, x)) + b
    return 1 if net > 0 else -1


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

