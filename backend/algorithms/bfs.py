from collections import deque

graph = {
    "S": ["A", "E"],
    "A": ["S", "B", "F"],
    "B": ["A", "C"],
    "C": ["B", "D"],
    "D": ["C", "G"],
    "E": ["S"],
    "F": ["A", "G"],
    "G": ["F", "D"]
}

def bfs(start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None