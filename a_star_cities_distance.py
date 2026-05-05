import heapq

def a_star_cities(graph, heuristics, start, goal):
    open_set = []
    heapq.heappush(open_set, (heuristics[start], 0, start, [start]))
    visited = set()

    while open_set:
        f, cost, current, path = heapq.heappop(open_set)

        if current == goal:
            return path, cost

        if current in visited:
            continue
        visited.add(current)

        for neighbor, weight in graph.get(current, {}).items():
            if neighbor not in visited:
                new_cost = cost + weight
                new_f = new_cost + heuristics.get(neighbor, 0)
                heapq.heappush(open_set, (new_f, new_cost, neighbor, path + [neighbor]))
    return None, float('inf')

if __name__ == "__main__":
    graph = {'A': {'B': 1, 'C': 4}, 'B': {'C': 2, 'D': 5}, 'C': {'D': 1}, 'D': {}}
    heuristics = {'A': 7, 'B': 6, 'C': 2, 'D': 0}
    print("Path and Cost:", a_star_cities(graph, heuristics, 'A', 'D'))
