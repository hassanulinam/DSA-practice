from collections import deque


def bfs(graph: dict[int, list[int]], start: int) -> list[int]:
    result: list[int] = []
    visited = set()
    q = deque([start])
    visited.add(start)
    while q:
        node = q.popleft()
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

    return result


def dfs_traversal(graph: dict[int, list[int]], start: int):
    result: list[int] = []
    visited = set()

    def dfs(node: int):
        visited.add(node)
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return result


def __main__():
    graph = {
        1: [2, 3],
        2: [1, 4],
        3: [1],
        4: [2],
    }
    print("BFS:", bfs(graph, list(graph.keys())[0]))
    print("DFS:", dfs_traversal(graph, list(graph.keys())[0]))


__main__()
