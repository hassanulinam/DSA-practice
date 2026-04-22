from collections import deque

from graph_commons import directions, is_out_bound_index_in_grid

INF = 2147483647

grid = [
    [INF, -1, 0, INF],
    [INF, INF, INF, -1],
    [INF, -1, INF, -1],
    [0, -1, INF, INF],
]


def update_distances() -> None:
    q: deque[tuple[int, int]] = deque([])
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                q.append((r, c))

    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if is_out_bound_index_in_grid(nr, nc, rows, cols):
                continue

            if grid[nr][nc] == INF:
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))


update_distances()
print(grid)
