"""Experiment 07 - Hebbian Learning, Unipolar Continuous.

Description: Apply the same one-pass Hebbian update as Experiment 05, then
read the learned neuron's output through a 0-to-1 sigmoid.

Theory: The activation changes only how the answer is displayed; learning
still depends solely on c*target*input. Values below and above 0.5 represent
the two unipolar classes.
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


def predict(x):
    net = sum(wi * xi for wi, xi in zip(w, x)) + b
    return 1 / (1 + math.exp(-net))


print("Initial w =", w, "b =", b)
for x, t in zip(X, T):
    w = [wi + c * t * xi for wi, xi in zip(w, x)]
    b += c * t
    print("x =", x, "t =", t, "w =", [round(v, 3) for v in w], "b =", round(b, 3))

print("Final w =", [round(v, 3) for v in w], "b =", round(b, 3))
for x in X:
    print(x, "->", round(predict(x), 3))

