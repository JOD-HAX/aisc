"""Experiment 05 - Hebbian Learning, Unipolar Binary.

Description: Read 0/1 training associations and apply one pass of the Hebbian
rule before classifying the same inputs with a hard step.

Theory: Hebbian learning adds c*target*input to every weight and c*target to
the bias. It does not use prediction error. With 0/1 targets, zero-target
samples teach nothing, so a suitable negative starting bias is important.
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


def predict(x):
    net = sum(wi * xi for wi, xi in zip(w, x)) + b
    return 1 if net > 0 else 0


print("Initial w =", w, "b =", b)
for x, t in zip(X, T):
    w = [wi + c * t * xi for wi, xi in zip(w, x)]
    b += c * t
    print("x =", x, "t =", t, "w =", w, "b =", b)

print("Final w =", w, "b =", b)
for x in X:
    print(x, "->", predict(x))

