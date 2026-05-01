# (r, c) is node, grid[r][c] cost of entering cell.
# Return the minimum total cost to reach from (0, 0) to (m-1, n-1).
# You can move only in 4 directions.


import heapq


def min_cost(grid: list[list[int]]) -> int:
    if not grid:
        return -1
    m, n = len(grid), len(grid[0])
    costs = [[float("inf")] * n for i in range(m)]
    starting_cell_cost = grid[0][0]
    costs[0][0] = starting_cell_cost
    heap = [(starting_cell_cost, 0, 0)]  # (cost, row_index, col_index)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while heap:
        current_cost, r, c = heapq.heappop(heap)
        if r == m - 1 and c == n - 1:
            return current_cost

        if current_cost > costs[r][c]:
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                new_cost = current_cost + grid[nr][nc]
                if new_cost < costs[nr][nc]:
                    costs[nr][nc] = new_cost
                    heapq.heappush(heap, (new_cost, nr, nc))
    return -1


grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1],
]
print(min_cost(grid))
