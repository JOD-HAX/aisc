"""Experiment 08 - Hebbian Learning, Bipolar Continuous.

Description: Apply one-pass bipolar Hebbian learning and display each answer
through a smooth -1-to-1 sigmoid.

Theory: Signed -1/+1 targets teach in both directions. The activation does not
alter the learned weights; its sign is read as the final bipolar class.
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
    return 2 / (1 + math.exp(-net)) - 1


print("Initial w =", w, "b =", b)
for x, t in zip(X, T):
    w = [wi + c * t * xi for wi, xi in zip(w, x)]
    b += c * t
    print("x =", x, "t =", t, "w =", [round(v, 3) for v in w], "b =", round(b, 3))

print("Final w =", [round(v, 3) for v in w], "b =", round(b, 3))
for x in X:
    print(x, "->", round(predict(x), 3))

