"""Experiment 21 - Centre of Area Defuzzification.

Description: Read a sampled fuzzy output set and find the first x position at
which cumulative membership reaches half of the total.

Theory: Centre of area here means the discrete bisector: half the sampled area
lies on each side. It differs from the centroid, which is a balance point
weighted by position.
"""

x = list(map(float, input("Points x: ").split()))
mu = list(map(float, input("Membership mu at each x: ").split()))

total_area = sum(mu)
half = total_area / 2

running = 0
x_star = x[-1]
for xi, m in zip(x, mu):
    running += m  # Add areas from left to right.
    if running >= half:
        x_star = xi
        break

print("Total area =", round(total_area, 2), "Half =", round(half, 2))
print("Centre of area x* =", x_star)
