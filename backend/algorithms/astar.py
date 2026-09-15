import heapq

graph = {
    "S": {"A": 1, "E": 4},
    "A": {"B": 2, "F": 5},
    "B": {"C": 2},
    "C": {"D": 1},
    "D": {"G": 3},
    "E": {},
    "F": {"G": 1},
    "G": {}
}

heuristic = {
    "S": 7,
    "A": 6,
    "B": 4,
    "C": 3,
    "D": 2,
    "E": 5,
    "F": 1,
    "G": 0
}

def astar(start, goal):

    priority_queue = [(0, start, [start], 0)]
    visited = set()

    while priority_queue:

        f_cost, current, path, g_cost = heapq.heappop(priority_queue)

        if current == goal:
            return path, g_cost

        if current in visited:
            continue

        visited.add(current)

        for neighbor, cost in graph[current].items():

            new_g = g_cost + cost
            new_f = new_g + heuristic[neighbor]

            heapq.heappush(
                priority_queue,
                (new_f, neighbor, path + [neighbor], new_g)
            )

    return None, None