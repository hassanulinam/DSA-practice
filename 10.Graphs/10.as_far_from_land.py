from collections import deque

from graph_commons import directions

grid = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


def farthest_from_land(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return -1
    dist = 0
    q: deque[tuple[int, int]] = deque([])
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                q.append((r, c))

    if not q or len(q) == rows * cols:
        return -1

    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == 0:
                    q.append((nr, nc))
                    grid[nr][nc] = grid[r][c] + 1
                    dist = grid[nr][nc] - 1
    return dist


print(farthest_from_land(grid))
