"""Experiment 20 - Height Defuzzification.

Description: Read two sampled output fuzzy sets, find each set's peak and
height, and calculate their height-weighted average.

Theory: The height method represents each fuzzy set only by its maximum
membership and the x position of that maximum. It is faster but ignores the
rest of each curve's shape.
"""

x = list(map(float, input("Points x: ").split()))
mu1 = list(map(float, input("Membership mu1 at each x: ").split()))
mu2 = list(map(float, input("Membership mu2 at each x: ").split()))

peaks, heights = [], []
for mu in [mu1, mu2]:
    height = max(mu)
    heights.append(height)
    peaks.append(x[mu.index(height)])

x_star = sum(p * h for p, h in zip(peaks, heights)) / sum(heights)
print("Height method x* =", round(x_star, 3))

