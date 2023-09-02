"""
This module implements Floyd-Warshall algorithm for finding shortest paths in a weighted graph.
"""

import sys

NO_PATH = sys.maxsize

def floyd(distance):
    """
    Iterative implementation of Floyd's algorithm
    """
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

def print_solution(dist):
    """Print the solution."""
    inf_value = float('inf')
    for row in dist:
        print(" ".join(str(cell) if cell != inf_value else "INF" for cell in row))

def main():
    """Main function."""
    dist = [
        [0, 1, NO_PATH, NO_PATH],
        [NO_PATH, 0, 2, NO_PATH],
        [NO_PATH, NO_PATH, 0, 3],
        [NO_PATH, NO_PATH, NO_PATH, 0]
    ]
    new_dist = floyd(dist)
    print("The shortest paths are:")
    print_solution(new_dist)

if __name__ == "__main__":
    main()
