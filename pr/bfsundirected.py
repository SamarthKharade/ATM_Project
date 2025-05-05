from collections import deque
visited = {}
sequence = []
queue = deque()

def traversal_graph(graph, source):
    visited[source] = True
    
    if source in queue:
        queue.remove(source)

    if source not in sequence:
        sequence.append(source)

    for neighbor in graph[source]:
        if not visited.get(neighbor, False):
            queue.append(neighbor)

    while queue:
        next_vertex = queue.popleft()
        traversal_graph(graph, next_vertex)
  
    return sequence
    
 

if __name__ == "__main__":
    graph = {}
    n = int(input("Enter the number of vertices in the graph: "))

    for i in range(n):
        vertex = input("Enter the vertex: ")
        graph[vertex] = []
        m = int(input(f"Enter the number of edges for vertex {vertex}: "))
        for j in range(m):
            edge = input(f"Enter edge {j+1} for vertex {vertex}: ")
            graph[vertex].append(edge)

    print("Graph is:", graph)

    source = input("Enter the source vertex for DFS traversal: ")
    visited = {v: False for v in graph}  # Dictionary for visited tracking

    result = traversal_graph(graph, source)
    print("DFS Traversal sequence is:", result)
