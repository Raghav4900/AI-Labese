def water_jug_dfs(cap_a, cap_b, goal):
    # Stack stores: (jug_a, jug_b, path_so_far)
    stack = [(0, 0, [(0, 0)])]
    visited = set()
    visited.add((0, 0))

    while stack:
        a, b, path = stack.pop()  # LIFO — last in, first out

        if a == goal or b == goal:
            print(f"\nGoal reached! {goal}L found.")
            print("Path:")
            for i, state in enumerate(path):
                print(f"  Step {i}: {state}")
            return

        # Generate all possible next states
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

        for state in next_states:
            if state not in visited:
                visited.add(state)
                stack.append((state[0], state[1], path + [state]))

    print("No solution found.")

# Run it
water_jug_dfs(4, 3, 2)