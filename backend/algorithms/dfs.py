graph = {
    "S": ["A", "E"],
    "A": ["B", "F"],
    "B": ["C"],
    "C": ["D"],
    "D": ["G"],
    "E": [],
    "F": ["G"],
    "G": []
}

def dfs(node, goal, visited=None, path=None):

    if visited is None:
        visited = set()

    if path is None:
        path = []

    visited.add(node)
    path.append(node)

    if node == goal:
        return path

    for neighbor in graph[node]:
        if neighbor not in visited:
            result = dfs(neighbor, goal, visited, path.copy())
            if result:
                return result

    return None