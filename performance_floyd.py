"""
Performance measurement for Floyd-Warshall algorithm implementations.
"""

import timeit
import random

# Recursive implementation code
RECURSIVE_CODE = """
def floyd_recursive(dist, i_val, j_val, k_val, memo_cache):
    if k_val == -1:
        return dist[i_val][j_val]
    if (i_val, j_val, k_val) in memo_cache:
        return memo_cache[(i_val, j_val, k_val)]
    without_k = floyd_recursive(dist, i_val, j_val, k_val - 1, memo_cache)
    with_k = (
        floyd_recursive(dist, i_val, k_val, k_val - 1, memo_cache) +
        floyd_recursive(dist, k_val, j_val, k_val - 1, memo_cache)
    )
    memo_cache[(i_val, j_val, k_val)] = min(without_k, with_k)
    return memo_cache[(i_val, j_val, k_val)]

def main():
    dist = [
        [0, 1, float('inf'), float('inf')],
        [float('inf'), 0, 2, float('inf')],
        [float('inf'), float('inf'), 0, 3],
        [float('inf'), float('inf'), float('inf'), 0]
    ]
    num = len(dist)
    new_dist = [[float('inf') for _ in range(num)] for _ in range(num)]
    memo_cache = {}
    for i_val in range(num):
        for j_val in range(num):
            new_dist[i_val][j_val] = floyd_recursive(dist, i_val, j_val, num-1, memo_cache)

if __name__ == "__main__":
    main()
"""

# Iterative implementation code
ITERATIVE_CODE = """
import sys

NO_PATH = sys.maxsize

def floyd(distance):
    max_length = len(distance[0])
    for intermediate in range(max_length):
        for start_node in range(max_length):
            for end_node in range(max_length):
                if start_node == end_node:
                    distance[start_node][end_node] = 0
                    continue
                distance[start_node][end_node] = min(
                    distance[start_node][end_node],
                    distance[start_node][intermediate] + distance[intermediate][end_node]
                )
    return distance

def main():
    dist = [
        [0, 1, NO_PATH, NO_PATH],
        [NO_PATH, 0, 2, NO_PATH],
        [NO_PATH, NO_PATH, 0, 3],
        [NO_PATH, NO_PATH, NO_PATH, 0]
    ]
    new_dist = floyd(dist)

if __name__ == "__main__":
    main()
"""

# Random graph generation
GRAPH_SIZE = 4
random_graph = [
    [random.randint(0, 10) for _ in range(GRAPH_SIZE)]
    for _ in range(GRAPH_SIZE)
]

# Measure performance
recursive_time = timeit.timeit(stmt=RECURSIVE_CODE, number=1000)
iterative_time = timeit.timeit(stmt=ITERATIVE_CODE, number=1000)

print("Recursive Implementation Time:", recursive_time)
print("Iterative Implementation Time:", iterative_time)
