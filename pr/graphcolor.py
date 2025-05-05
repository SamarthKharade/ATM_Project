# Function to check if the current color assignment is valid for vertex `v`
def is_valid(graph, color, v, c):
    # Check all adjacent vertices of vertex v
    for i in graph[v]:
        if color[i] == c:
            return False
    return True

# Backtracking function to assign colors
def graph_coloring_util(graph, color, m, v):
    # If all vertices are assigned a color, return True
    if v == len(graph):
        return True

    # Try all colors for vertex v
    for c in range(1, m + 1):
        # Check if assigning color c to vertex v is valid
        if is_valid(graph, color, v, c):
            color[v] = c  # Assign color c to vertex v

            # Recur to assign colors to the next vertex
            if graph_coloring_util(graph, color, m, v + 1):
                return True

            # Backtrack if no solution is found
            color[v] = 0

    return False

# Function to solve the Graph Coloring Problem
def graph_coloring(graph, m):
    color = [0] * len(graph)  # List to store the color assignment of vertices

    # Call the utility function to start coloring from vertex 0
    if not graph_coloring_util(graph, color, m, 0):
        print("Solution does not exist.")
        return False

    # Print the color assignment
    print("Solution exists: The color assignments are:")
    for v in range(len(graph)):
        print(f"Vertex {v} -> Color {color[v]}")
    return True

# Example usage
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    # Graph with 4 vertices and edges (0-1, 0-2, 1-2, 1-3)
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1],
        3: [1]
    }

    m = int(input("Enter the number of colors: "))
    
    # Try to solve the graph coloring problem
    graph_coloring(graph, m)
