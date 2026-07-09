import heapq


def generate_adjacency_list_from_weighted_edges(
    n: int, edges: list[tuple[int, int, int]]
) -> dict[int, list[tuple[int, int]]]:
    graph = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w))

    return graph


def shortest_path_to_dest(
    src: int, dest: int, edges: list[tuple[int, int, int]], n: int
) -> int | float:
    graph = generate_adjacency_list_from_weighted_edges(n, edges)
    dist = [float("inf")] * n
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        currest_dist, node = heapq.heappop(heap)
        if node == dest:
            return currest_dist
        if currest_dist > dist[node]:
            continue
        for nb, weight in graph[node]:
            new_dist = currest_dist + weight
            if new_dist < dist[nb]:
                dist[nb] = new_dist
                heapq.heappush(heap, (new_dist, nb))

    return dist[dest]


# (u, v, w) → edge from u → v with weight w
edges = [
    (0, 1, 4),
    (0, 2, 1),
    (2, 1, 2),
    (1, 3, 1),
    (2, 3, 5),
    (3, 4, 4),
    (2, 4, 1),
]
# print(shortes_path(0, edges, 4, 1))
print(shortest_path_to_dest(0, 4, edges, 5))
