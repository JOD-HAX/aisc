"""Experiment 18 - Centroid Defuzzification.

Description: Read sampled output positions and memberships and calculate the
center of gravity of the combined fuzzy set.

Theory: The discrete centroid is x* = sum(mu(x)*x)/sum(mu(x)). Every point of
the output curve contributes in proportion to its membership value.
"""

x = list(map(float, input("Points x: ").split()))
mu = list(map(float, input("Membership mu at each x: ").split()))

x_star = sum(xi * m for xi, m in zip(x, mu)) / sum(mu)
print("Centroid x* =", round(x_star, 3))

