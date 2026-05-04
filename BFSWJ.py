from collections import deque

def water_jug_bfs(cap_a, cap_b, goal):
    # Queue stores: (jug_a, jug_b, path_so_far)
    queue = deque()
    queue.append((0, 0, [(0, 0)]))
    visited = set()
    visited.add((0, 0))

    while queue:
        a, b, path = queue.popleft()  # FIFO — first in, first out

        if a == goal or b == goal:
            print(f"\nGoal reached! {goal}L found.")
            print(f"Steps taken: {len(path) - 1}")
            print("Path (shortest):")
            for i, state in enumerate(path):
                print(f"  Step {i}: Jug A={state[0]}L, Jug B={state[1]}L")
            return

        # All 6 possible operations
        next_states = [
            (cap_a, b),              # Fill A
            (a, cap_b),              # Fill B
            (0, b),                  # Empty A
            (a, 0),                  # Empty B
            (a - min(a, cap_b - b),  # Pour A → B
             b + min(a, cap_b - b)),
            (a + min(b, cap_a - a),  # Pour B → A
             b - min(b, cap_a - a)),
        ]

        for na, nb in next_states:
            if (na, nb) not in visited:
                visited.add((na, nb))
                queue.append((na, nb, path + [(na, nb)]))

    print("No solution found.")

# Run it
water_jug_bfs(4, 3, 2)