def heuristic(state, goal):
    """Count misplaced tiles (not counting the blank)"""
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])

def get_neighbors(state):
    """Generate all states reachable by sliding one tile"""
    neighbors = []
    blank = state.index(0)   # find where the blank (0) is
    row, col = blank // 3, blank % 3

    # Possible moves: up, down, left, right
    moves = []
    if row > 0: moves.append(blank - 3)   # slide tile from above down
    if row < 2: moves.append(blank + 3)   # slide tile from below up
    if col > 0: moves.append(blank - 1)   # slide tile from left right
    if col < 2: moves.append(blank + 1)   # slide tile from right left

    for pos in moves:
        new_state = list(state)
        # Swap blank with the adjacent tile
        new_state[blank], new_state[pos] = new_state[pos], new_state[blank]
        neighbors.append(tuple(new_state))

    return neighbors

def hill_climbing(initial, goal):
    current = tuple(initial)
    goal    = tuple(goal)
    steps   = 0

    print("Hill Climbing — 8 Puzzle")
    print(f"Initial h = {heuristic(current, goal)}\n")

    while True:
        h_current = heuristic(current, goal)

        # Print current state
        print(f"Step {steps} | h = {h_current}")
        for i in range(0, 9, 3):
            print(current[i:i+3])
        print()

        # Goal check
        if h_current == 0:
            print("Goal reached!")
            return True

        # Generate neighbors and find the best one
        neighbors = get_neighbors(current)
        best_neighbor = None
        best_h = h_current   # only move if we improve

        for neighbor in neighbors:
            h = heuristic(neighbor, goal)
            if h < best_h:
                best_h = h
                best_neighbor = neighbor

        # If no better neighbor found → stuck
        if best_neighbor is None:
            print(f"Stuck at local optimum! h = {h_current}, cannot improve.")
            print("Hill Climbing FAILED — goal not reached.")
            return False

        # Move to best neighbor
        current = best_neighbor
        steps += 1

# ── Define states ──────────────────────────────────────────
initial_state = [1, 2, 3,
                 4, 6, 0,
                 7, 5, 8]

goal_state    = [1, 2, 3,
                 4, 5, 6,
                 7, 8, 0]

hill_climbing(initial_state, goal_state)