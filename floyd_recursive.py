"""Implementation of Floyd-Warshall algorithm using recursion."""

def floyd_recursive(dist, i_val, j_val, k_val, memo_cache):
    """Recursively compute shortest paths."""
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

def print_solution(dist):
    """Print the solution."""
    inf_value = float('inf')
    for row in dist:
        print(" ".join(str(cell) if cell != inf_value else "INF" for cell in row))

def main():
    """Main function."""
    inf_value = float('inf')
    dist = [
        [0, 1, inf_value, inf_value],
        [inf_value, 0, 2, inf_value],
        [inf_value, inf_value, 0, 3],
        [inf_value, inf_value, inf_value, 0]
    ]
    num = len(dist)
    new_dist = [[inf_value for _ in range(num)] for _ in range(num)]
    memo_cache = {}
    for i_val in range(num):
        for j_val in range(num):
            new_dist[i_val][j_val] = floyd_recursive(dist, i_val, j_val, num-1, memo_cache)
    print("The shortest paths are:")
    print_solution(new_dist)

if __name__ == "__main__":
    main()
