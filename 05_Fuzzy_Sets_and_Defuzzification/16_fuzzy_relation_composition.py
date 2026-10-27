"""Experiment 16 - Composition of fuzzy relations.

Description: Read compatible fuzzy-relation matrices R and S and calculate
both max-min and max-product composition.

Theory: For every output cell, examine all paths through the shared middle
dimension. Max-min keeps the maximum of the weaker link on each path, while
max-product keeps the maximum product of both link memberships.
"""

# Matrices: one line per row. S needs as many rows as R has columns.
rows = int(input("Rows of R: "))
R = []
for i in range(rows):
    R.append(list(map(float, input("Row " + str(i + 1) + " of R: ").split())))

S = []
for i in range(len(R[0])):
    S.append(list(map(float, input("Row " + str(i + 1) + " of S: ").split())))


def max_min(R, S):
    """Find max of minimum values for every output cell."""
    T = []
    for i in range(len(R)):
        row = []
        for j in range(len(S[0])):
            values = [min(R[i][k], S[k][j]) for k in range(len(S))]
            row.append(max(values))
        T.append(row)
    return T


def max_product(R, S):
    """Find max of products for every output cell."""
    T = []
    for i in range(len(R)):
        row = []
        for j in range(len(S[0])):
            values = [round(R[i][k] * S[k][j], 2) for k in range(len(S))]
            row.append(max(values))
        T.append(row)
    return T


print("R =", R)
print("S =", S)
print("Max-Min composition     =", max_min(R, S))
print("Max-Product composition =", max_product(R, S))

