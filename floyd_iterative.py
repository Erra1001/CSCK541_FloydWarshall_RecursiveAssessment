"""Module for Floyd-Warshall algorithm with iterative implementation."""

def floyd(distance):
    """Iterative implementation of Floyd-Warshall algorithm.
    
    Args:
    distance (list): 2D list representing the graph
    
    Returns:
    list: 2D list representing shortest paths
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
    """Prints the shortest paths.
    
    Args:
    dist (list): 2D list representing shortest paths
    """
    inf_value = float('inf')
    for row in dist:
        print(" ".join(str(cell) if cell != inf_value else "INF" for cell in row))

def main():
    """Main function."""
    dist = [
        [0, 1, float('inf'), float('inf')],
        [float('inf'), 0, 2, float('inf')],
        [float('inf'), float('inf'), 0, 3],
        [float('inf'), float('inf'), float('inf'), 0]
    ]
    new_dist = floyd(dist)
    print("The shortest paths are:")
    print_solution(new_dist)

if __name__ == "__main__":
    main()
