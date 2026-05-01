import heapq


def generate_adjacency_list_from_weighted_edges(
    n: int, edges: list[tuple[int, int, int]]
) -> dict[int, list[tuple[int, int]]]:
    graph = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w))

    return graph


def shortes_path(
    src: int,
    edges: list[tuple[int, int, int]],
    n: int,
    destination: int,
) -> int:
    graph = generate_adjacency_list_from_weighted_edges(n, edges)
    dist = [float("inf")] * n
    dist[src] = 0
    heap = [(0, src)]  # (distance, node)
    while heap:
        current_dist, node = heapq.heappop(heap)

        if node == destination:
            return current_dist

        if current_dist > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return -1


# (u, v, w) → edge from u → v with weight w
edges = [
    (0, 1, 4),
    (0, 2, 1),
    (2, 1, 2),
    (1, 3, 1),
    (2, 3, 5),
]
print(shortes_path(0, edges, 4, 1))
