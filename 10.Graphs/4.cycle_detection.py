from collections import deque

n = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
graph = {i: [] for i in range(n)}

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

# graph = {0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]}  # True


def get_is_cyclic_graph(graph: dict[int, list[int]]) -> bool:
    visited = set()

    def dfs(node: int, parent: int) -> bool:
        visited.add(node)

        for nb in graph[node]:
            if nb not in visited:
                if dfs(nb, node):
                    return True
            elif nb != parent:
                return True
        return False

    for each_node in range(n):
        if each_node not in visited:
            if dfs(each_node, -1):
                return True

    return False


def get_is_cyclic_graph_bfs(graph: dict[int, list[int]]) -> bool:
    visited = set()

    def bfs(node: int) -> bool:
        visited.add(node)
        q = deque([node])
        while q:
            parent = q.popleft()

            for nb in graph[parent]:
                if nb not in visited:
                    visited.add(nb)
                    q.append(nb)
                elif nb != parent:
                    return True
        return False

    for each_node in graph:
        if each_node not in visited:
            if bfs(each_node):
                return True
    return False


print("Is having cycle?:", get_is_cyclic_graph(graph))
print("Is having cycle?(BFS):", get_is_cyclic_graph_bfs(graph))
