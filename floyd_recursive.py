"""
Implementation of Floyd-Warshall algorithm using recursion.
"""

# Initialize constants
INF = float('inf')

def floyd_recursive(dist, i_val, j_val, k_val):
    """
    Recursively compute shortest paths.

    Parameters:
    dist (list of lists): The distance matrix.
    i_val (int): The starting vertex.
    j_val (int): The destination vertex.
    k_val (int): The intermediate vertex.

    Returns:
    float: The shortest distance from i_val to j_val through k_val.
    """
    if k_val == -1:
        return dist[i_val][j_val]

    without_k = floyd_recursive(dist, i_val, j_val, k_val - 1)
    with_k = (
        floyd_recursive(dist, i_val, k_val, k_val - 1) +
        floyd_recursive(dist, k_val, j_val, k_val - 1)
    )

    return min(without_k, with_k)

def print_solution(dist):
    """
    Print the solution.

    Parameters:
    dist (list of lists): The distance matrix.
    """
    inf = float('inf')
    for row in dist:
        print(" ".join(str(cell) if cell != inf else "INF" for cell in row))

def main():
    """
    Main function.
    """
    inf = float('inf')
    dist = [
        [0, 7, inf, 8],
        [inf, 0, 5, 7],
        [inf, inf, 0, 2],
        [inf, inf, inf, 0]
    ]
    num = len(dist)
    new_dist = [[inf for _ in range(num)] for _ in range(num)]
    for i_val in range(num):
        for j_val in range(num):
            new_dist[i_val][j_val] = floyd_recursive(dist, i_val, j_val, num - 1)
    print("The shortest paths are:")
    print_solution(new_dist)

if __name__ == "__main__":
    main()
