"""Experiment 10 - Depth-First Iterative Deepening (DFID).

Description: Repeatedly run depth-limited search with limits 0, 1, 2, and so
on until the goal is found or the user-supplied maximum depth is reached.

Theory: DFID combines the low memory use of DFS with the shallowest-goal
behavior of breadth-first search by restarting DLS at successively deeper
limits.
"""

n = int(input("Number of nodes: "))
graph = {}
for i in range(n):
    line = input("Node and its children: ").split()
    graph[line[0]] = line[1:]

start = input("Start node: ")
goal = input("Goal node: ")
max_depth = int(input("Maximum depth: "))


def dls(node, depth, path):
    """Return a path if the goal is found at this depth."""
    path = path + [node]
    if node == goal:
        return path
    if depth == 0:
        return None
    for child in graph[node]:
        answer = dls(child, depth - 1, path)
        if answer:
            return answer
    return None


def dfid(start, goal, max_depth):
    """Try DLS with limits 0, 1, 2, ..."""
    for limit in range(max_depth + 1):
        print("Trying limit", limit)
        path = dls(start, limit, [])
        if path:
            return path
    return None


result = dfid(start, goal, max_depth)
if result:
    print("Goal found, path =", result)
else:
    print("Goal not found")

