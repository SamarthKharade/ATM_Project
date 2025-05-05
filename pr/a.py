import heapq

# Heuristic: number of misplaced tiles
def heuristic(state, goal):
    return sum([1 if state[i] != goal[i] and state[i] != 0 else 0 for i in range(9)])

# Find possible moves for the blank (0)
def get_neighbors(state):
    neighbors = []
    index = state.index(0)
    row, col = index // 3, index % 3

    # Up, Down, Left, Right moves
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        new_row, new_col = row + dx, col + dy
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            # Swap blank with the target
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(tuple(new_state))
    return neighbors

# A* algorithm
def astar(start, goal):
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), 0, start, []))  # (f, g, state, path)
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == goal:
            return path + [current]

        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                heapq.heappush(open_set, (g + 1 + heuristic(neighbor, goal), g + 1, neighbor, path + [current]))

    return None

# Main
if __name__ == "__main__":
    print("8-Puzzle A* Solver")

    # Initial and goal state (0 represents the blank)
    start = (1, 2, 3,
             4, 0, 5,
             6, 7, 8)

    goal = (1, 2, 3,
            4, 5, 6,
            7, 8, 0)

    solution = astar(start, goal)

    if solution:
        print("\nSteps to reach the goal:")
        for step in solution:
            print(f"{step[0:3]}\n{step[3:6]}\n{step[6:9]}\n")
    else:
        print("No solution found.")
