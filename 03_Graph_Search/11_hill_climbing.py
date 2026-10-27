"""Experiment 11 - Hill Climbing.

Description: Read a graph with heuristic values and repeatedly move to the
child having the lowest heuristic until reaching the goal or a local minimum.

Theory: Hill climbing is greedy local search. It uses only h(n), keeps no
alternative frontier, and stops when no child improves the current heuristic;
therefore it is neither complete nor optimal.
"""

n = int(input("Number of nodes: "))
graph = {}
h = {}
for i in range(n):
    line = input("Node, h value and its children: ").split()
    graph[line[0]] = line[2:]
    h[line[0]] = float(line[1])

start = input("Start node: ")
goal = input("Goal node: ")


def hill_climbing(start, goal):
    """Always move to the child with the smallest heuristic."""
    current = start
    path = [current]
    while current != goal:
        choices = graph[current]
        best = min(choices, key=lambda node: h[node]) if choices else current
        if best == current or h[best] >= h[current]:
            print("Stuck at", current, "(local minimum)")
            return path
        current = best
        path.append(current)
    return path


path = hill_climbing(start, goal)
print("Path =", path)

