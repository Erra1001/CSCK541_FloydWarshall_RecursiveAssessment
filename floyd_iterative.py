"""
This module implements the Floyd-Warshall algorithm for finding shortest paths in a weighted graph.
This version has been adapted to follow PEP-8 standards and may differ slightly from the original
PDF version. Specifically, it:
1. Uses float('inf') instead of sys.maxsize to represent unreachable paths.
2. Directly returns the distance matrix instead of printing it.
3. Utilizes nested for loops instead of itertools.product for the main loop.

However, the core logic for finding the shortest paths remains the same.
"""

# Initialize constants
INF = float('inf')

def floyd_warshall(input_graph):
    """
    Implement the Floyd-Warshall algorithm to find the shortest path for all vertex pairs.
    """
    # Get the number of vertices
    num_vertices = len(input_graph)

    # Initialize the solution matrix with the given graph
    dist_matrix = [row[:] for row in input_graph]

    # Update the solution matrix
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                # Update dist_matrix[i][j] only if vertex k is on the shorter path
                # from dist_matrix[i][j]
                if dist_matrix[i][j] > dist_matrix[i][k] + dist_matrix[k][j]:
                    dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]

    return dist_matrix

if __name__ == '__main__':
    # Test graph represented as an adjacency matrix
    graph = [
        [0, 7, INF, 8],
        [INF, 0, 5, INF],
        [INF, INF, 0, 2],
        [INF, INF, INF, 0]
    ]

    # Get the shortest paths matrix
    shortest_paths = floyd_warshall(graph)

    # Display the shortest paths
    print("The shortest paths are:")
    for row in shortest_paths:
        print(" ".join(map(str, [str(x).upper() if x == INF else x for x in row])))
