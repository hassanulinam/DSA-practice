"""
0 --(4)-- 1
|        / \
(1)    (2) (1)
|      /     \
2 ----(5)---- 3
"""

import heapq


def dijkstra(
    graph: dict[int, list[tuple[int, int]]], n: int, src: int
) -> list[int | float]:
    dist = [float("inf")] * n
    dist[src] = 0
    heap = [(0, src)]  # (distance, node)
    while heap:
        current_dist, node = heapq.heappop(heap)

        if current_dist > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return dist


n = 4
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [],
}
src = 0
print(dijkstra(graph, n, src))
