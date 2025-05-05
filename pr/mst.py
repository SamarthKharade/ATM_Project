import sys

def prim_mst(graph):
    num_vertices = len(graph)
    selected = [False] * num_vertices  # Track vertices included in MST
  
    
    selected[0] = True  # Start from the first vertex

    edges = 0
    print("Edge : Weight")

    while edges < num_vertices - 1:
        minimum = sys.maxsize

        x = 0
        y = 0

        for i in range(num_vertices):
            if selected[i]:
                for j in range(num_vertices):
                    if not selected[j] and graph[i][j]:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j

        print(f"{x} - {y} : {graph[x][y]}")
        selected[y] = True
        edges += 1

# Example usage
if __name__ == "__main__":
    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]

    prim_mst(graph)
