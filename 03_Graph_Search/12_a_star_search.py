"""Experiment 12 - A* Search Algorithm.

Description: Read a weighted graph and heuristic values, then find a least-cost
path by expanding the open node with the smallest f = g + h.

Theory: g is the path cost already paid and h estimates the remaining cost.
With an admissible heuristic and standard assumptions, testing the goal when
it is popped from the priority queue yields an optimal route.
"""

import heapq

n = int(input("Number of nodes: "))
graph = {}
h = {}
for i in range(n):
    line = input("Node, h value, then child cost pairs: ").split()
    h[line[0]] = float(line[1])
    graph[line[0]] = {}
    for j in range(2, len(line), 2):
        graph[line[0]][line[j]] = float(line[j + 1])

start = input("Start node: ")
goal = input("Goal node: ")


def a_star(start, goal):
    """Choose the node with the smallest f = cost + heuristic."""
    open_list = [(h[start], 0, start, [start])]
    visited = set()
    while open_list:
        _, g, node, path = heapq.heappop(open_list)
        if node == goal:
            return path, g
        if node in visited:
            continue
        visited.add(node)
        for child, cost in graph[node].items():
            new_cost = g + cost
            heapq.heappush(open_list, (new_cost + h[child], new_cost, child, path + [child]))
    return None, 0


path, cost = a_star(start, goal)
print("Path =", path)
print("Total cost =", cost)
