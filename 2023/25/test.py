import random
from copy import deepcopy

def karger_min_cut(graph):
    """
    Implements Karger's algorithm to find the minimum cut of a graph.

    Parameters:
        graph (dict): A dictionary where keys are nodes and values are lists of nodes
                      that the key node is connected to (adjacency list).

    Returns:
        int: The size of the minimum cut.
    """
    # Create a deepcopy of the graph to avoid modifying the original
    graph = deepcopy(graph)

    while len(graph) > 2:
        # Randomly select an edge (u, v)
        u = random.choice(list(graph.keys()))
        v = random.choice(graph[u])

        # Merge node v into node u
        # Add all edges of v to u, excluding self-loops
        graph[u].extend(graph[v])
        graph[u] = [x for x in graph[u] if x != u]  # Remove self-loops

        # Redirect all edges pointing to v to point to u
        for neighbor in graph[v]:
            graph[neighbor] = [u if x == v else x for x in graph[neighbor]]

        # Remove v from the graph
        del graph[v]

    # The graph now has exactly two nodes; the edges between them form the cut
    remaining_edges = list(graph.values())[0]
    return len(remaining_edges)

# Example usage
if __name__ == "__main__":
    # Define a graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C']
    }

    # Run Karger's algorithm multiple times to find the minimum cut
    min_cut = float('inf')
    for _ in range(100):  # Increase iterations for higher probability of correctness
        cut = karger_min_cut(graph)
        min_cut = min(min_cut, cut)

    print("Minimum Cut:", min_cut)