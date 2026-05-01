import heapq


def build_weighted_graph(
    n: int, flights: list[tuple[int, int, int]]
) -> dict[int, list[tuple[int, int]]]:
    # u, v, w
    graph = {i: [] for i in range(n)}
    for u, v, w in flights:
        graph[u].append((v, w))

    return graph


def get_chepest_flight_price(
    n: int, graph: dict[int, list[tuple[int, int]]], k: int, src: int, dst: int
):
    heap = [(0, src, k + 1)]  # price, current_node, remaining_k
    prices = [float("inf")] * n
    prices[src] = 0
    while heap:
        current_price, current_node, remaining_k = heapq.heappop(heap)
        if remaining_k >= 0 and current_node == dst:
            return current_price
        if prices[current_node] > current_price or remaining_k <= 0:
            continue

        for nb_node, nb_price in graph[current_node]:
            new_price = current_price + nb_price
            if new_price < prices[nb_node]:
                prices[nb_node] = new_price
                heapq.heappush(heap, (new_price, nb_node, remaining_k - 1))

    return -1


n = 3
flights = [
    (0, 1, 100),
    (1, 2, 100),
]
src = 0
dst = 2
k = 0

graph = build_weighted_graph(n, flights)
print(get_chepest_flight_price(n, graph, k, src, dst))
