"""Experiment 09 - Depth-Limited Search (DLS).

Description: Read a directed graph, start node, goal node, and maximum depth,
then perform depth-first search without crossing that limit.

Theory: DLS is recursive DFS with a countdown. Each recursive step reduces the
remaining limit by one; reaching zero forces backtracking unless the current
node is already the goal.
"""

n = int(input("Number of nodes: "))
graph = {}
for i in range(n):
    line = input("Node and its children: ").split()
    graph[line[0]] = line[1:]

start = input("Start node: ")
goal = input("Goal node: ")
limit = int(input("Depth limit: "))


def dls(node, depth, path):
    """Return the path if the goal is found within the limit."""
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


path = dls(start, limit, [])
if path:
    print("Limit", limit, "-> goal found, path =", path)
else:
    print("Limit", limit, "-> goal not found")

