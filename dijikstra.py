import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}  # Set all initial distances to infinity
    #print(distances)
    distances[start] = 0  # Set the starting vertex's distance to 0
    pq = [(0, start)]  # Add the starting vertex to the heap with priority 0
   
    visited = set()  # Keep track of visited vertices
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)  # Get the vertex with the smallest distance
        
        print (current_distance, current_vertex)
        #print(pq)
        if current_vertex in visited:
            continue  # Skip if we've already visited this vertex
        
        visited.add(current_vertex)  # Mark the vertex as visited
        
        for neighbor, weight in graph[current_vertex].items():  # Check each neighboring vertex
            distance = current_distance + weight  # Calculate the distance to the neighboring vertex
            
            if distance < distances[neighbor]:  # If the new distance is less than the previously calculated distance
                distances[neighbor] = distance  # Update the distance
                heapq.heappush(pq, (distance, neighbor))  # Add the neighboring vertex to the heap with the updated distance
        #print(distances)       
    return distances


graph = {
    'A': {'B': 3, 'C': 4, 'D': 2},
    'B': {'A': 3, 'C': 5, 'E': 9},
    'C': {'A': 4, 'B': 5, 'D': 1, 'E': 6},
    'D': {'A': 2, 'C': 1, 'F': 8},
    'E': {'B': 9, 'C': 6, 'F': 7},
    'F': {'D': 8, 'E': 7}
}

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)
print(distances)
