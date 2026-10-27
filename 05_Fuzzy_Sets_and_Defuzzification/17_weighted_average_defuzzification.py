"""Experiment 17 - Weighted Average Defuzzification.

Description: Read representative peaks and firing heights for output fuzzy
sets and convert them into one crisp value.

Theory: Weighted average uses x* = sum(height*peak)/sum(height). Sets with
larger firing strengths pull the final value more strongly toward their peaks.
"""

peaks = list(map(float, input("Peak of each set: ").split()))
heights = list(map(float, input("Height of each set: ").split()))

x_star = sum(p * h for p, h in zip(peaks, heights)) / sum(heights)
print("Weighted average x* =", round(x_star, 3))

