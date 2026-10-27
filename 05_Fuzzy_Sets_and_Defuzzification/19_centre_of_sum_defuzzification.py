"""Experiment 19 - Centre of Sum Defuzzification.

Description: Read two fuzzy output sets over common sample points and find the
center of gravity after adding their memberships.

Theory: Centre of sum uses x* = sum(x*(mu1+mu2))/sum(mu1+mu2). Unlike a max
union, overlapping parts contribute once from each fuzzy set.
"""

x = list(map(float, input("Points x: ").split()))
mu1 = list(map(float, input("Membership mu1 at each x: ").split()))
mu2 = list(map(float, input("Membership mu2 at each x: ").split()))

total_mu = [a + b for a, b in zip(mu1, mu2)]
x_star = sum(xi * m for xi, m in zip(x, total_mu)) / sum(total_mu)
print("Centre of sum x* =", round(x_star, 3))

