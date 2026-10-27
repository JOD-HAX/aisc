"""Experiment 06 - Hebbian Learning, Bipolar Binary.

Description: Read -1/+1 associations and apply one Hebbian pass before
classifying the inputs with a bipolar step.

Theory: The signed product target*input can strengthen or weaken a weight.
Unlike the unipolar case, every -1/+1 sample contributes, so a zero starting
bias can learn the sample AND or OR gate.
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
    return 1 if net > 0 else -1


print("Initial w =", w, "b =", b)
for x, t in zip(X, T):
    w = [wi + c * t * xi for wi, xi in zip(w, x)]
    b += c * t
    print("x =", x, "t =", t, "w =", w, "b =", b)

print("Final w =", w, "b =", b)
for x in X:
    print(x, "->", predict(x))

