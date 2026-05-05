import heapq

def manhattan_distance(state, goal):
    dist = 0
    for i in range(1, 9):
        curr_idx = state.index(i)
        goal_idx = goal.index(i)
        dist += abs(curr_idx // 3 - goal_idx // 3) + abs(curr_idx % 3 - goal_idx % 3)
    return dist

def get_neighbors(state):
    neighbors = []
    idx = state.index(0)
    r, c = idx // 3, idx % 3
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            n_idx = nr * 3 + nc
            new_state = list(state)
            new_state[idx], new_state[n_idx] = new_state[n_idx], new_state[idx]
            neighbors.append(tuple(new_state))
    return neighbors

def a_star_8_puzzle(start, goal):
    open_set = []
    heapq.heappush(open_set, (manhattan_distance(start, goal), 0, start, [start]))
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == goal:
            return path

        if current in visited:
            continue
        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + manhattan_distance(neighbor, goal)
                heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))
    return None

if __name__ == "__main__":
    start = (1, 2, 3, 4, 0, 5, 6, 7, 8)
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    path = a_star_8_puzzle(start, goal)
    print("Steps:", len(path) - 1 if path else -1)
