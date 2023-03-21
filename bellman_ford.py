def bellman_ford(graph, start):
    # Initialize the distances dictionary with start vertex having distance 0 and all other vertices having infinity distance.
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # Iterate over all edges V-1 times, where V is the number of vertices in the graph.
    for _ in range(len(graph) - 1):
        # For each edge (u, v) with weight w in the graph, update the distance to v if the distance to u plus w is smaller than the current distance to v.
        for u in graph:
            for v, w in graph[u].items():
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
    
    # Check for negative-weight cycles.
    for u in graph:
        for v, w in graph[u].items():
            if distances[u] + w < distances[v]:
                raise ValueError("Negative weight cycle detected")
    
    return distances

graph = {
    'A': {'B': 3, 'C': 4, 'D': 2},
    'B': {'A': 3, 'C': 5, 'E': 9},
    'C': {'A': 4, 'B': 5, 'D': 1, 'E': 6},
    'D': {'A': 2, 'C': 1, 'F': 8},
    'E': {'B': 9, 'C': 6, 'F': 7},
    'F': {'D': 8, 'E': 7}
}

print(bellman_ford(graph, 'A'))