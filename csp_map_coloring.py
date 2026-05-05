def solve_map_coloring(graph, colors):
    solution = {}

    def is_safe(node, color):
        for neighbor in graph.get(node, []):
            if solution.get(neighbor) == color:
                return False
        return True

    def solve(nodes, idx):
        if idx == len(nodes): return True
        node = nodes[idx]

        for color in colors:
            if is_safe(node, color):
                solution[node] = color
                if solve(nodes, idx + 1): return True
                del solution[node]
        return False

    if solve(list(graph.keys()), 0):
        return solution
    return None

if __name__ == "__main__":
    graph = {'WA': ['NT', 'SA'], 'NT': ['WA', 'SA', 'Q'], 'SA': ['WA', 'NT', 'Q', 'NSW', 'V'], 'Q': ['NT', 'SA', 'NSW'], 'NSW': ['Q', 'SA', 'V'], 'V': ['SA', 'NSW']}
    colors = ['Red', 'Green', 'Blue']
    print(solve_map_coloring(graph, colors))
