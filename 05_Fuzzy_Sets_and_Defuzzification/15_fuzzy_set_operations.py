"""Experiment 15 - Five fuzzy operations on two sets.

Description: Read two equally sized fuzzy sets and calculate their union,
intersection, complement, algebraic sum, and algebraic product.

Theory: A fuzzy membership lies between 0 and 1. Standard union uses maximum,
intersection uses minimum, complement uses 1-A, algebraic sum uses A+B-AB,
and algebraic product uses AB for each corresponding element.
"""

# Membership values of each set, one number per element.
A = list(map(float, input("Membership values of A: ").split()))
B = list(map(float, input("Membership values of B: ").split()))

union = [max(a, b) for a, b in zip(A, B)]
intersection = [min(a, b) for a, b in zip(A, B)]
complement = [round(1 - a, 2) for a in A]
algebraic_sum = [round(a + b - a * b, 2) for a, b in zip(A, B)]
algebraic_product = [round(a * b, 2) for a, b in zip(A, B)]

print("A                 =", A)
print("B                 =", B)
print("Union             =", union)
print("Intersection      =", intersection)
print("Complement of A   =", complement)
print("Algebraic sum     =", algebraic_sum)
print("Algebraic product =", algebraic_product)

