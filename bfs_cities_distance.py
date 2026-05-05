from collections import deque

def bfs_cities(graph, start, goal):
    queue = deque([(start, [start], 0)])
    visited = {start}

    while queue:
        current, path, cost = queue.popleft()

        if current == goal:
            return path, cost

        for neighbor, weight in graph.get(current, {}).items():
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor], cost + weight))
    return None, float('inf')

if __name__ == "__main__":
    graph = {'A': {'B': 1, 'C': 4}, 'B': {'C': 2, 'D': 5}, 'C': {'D': 1}, 'D': {}}
    print("Path and Cost:", bfs_cities(graph, 'A', 'D'))
