from collections import deque

n = 7
edges = [(0, 1), (1, 2), (3, 2), (4, 5), (6, 1)]


def build_graph_undirected(
    n: int, edges: list[tuple[int, int]]
) -> dict[int, list[int]]:
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


def get_nconnected_components_dfs(n: int, edges: list[tuple[int, int]]) -> int:
    total = 0
    graph = build_graph_undirected(n, edges)
    visited = set()

    def dfs(node: int) -> None:
        visited.add(node)
        for nb in graph[node]:
            if nb not in visited:
                dfs(nb)

    for node in range(n):
        if node not in visited:
            total += 1
            dfs(node)

    return total


def get_nconnected_components_bfs(n: int, edges: list[tuple[int, int]]) -> int:
    total = 0
    visited = set()
    graph = build_graph_undirected(n, edges)

    def bfs(node: int) -> None:
        q = deque([node])
        visited.add(node)
        while q:
            curr = q.popleft()
            for nb in graph[curr]:
                if nb not in visited:
                    visited.add(nb)
                    q.append(nb)

    for node in range(n):
        if node not in visited:
            total += 1
            bfs(node)

    return total


print(
    "Total no.of connected components (DFS):", get_nconnected_components_dfs(n, edges)
)
print(
    "Total no.of connected components (BFS):", get_nconnected_components_bfs(n, edges)
)
