# https://leetcode.com/problems/rotting-oranges
from collections import deque

grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1],
]


def mins_for_rotting(grid: list[list[int]]) -> int:
    if not grid:
        return -1
    minutes = 0
    fresh = 0
    q: deque[tuple[int, int]] = deque([])
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1
            elif grid[r][c] == 2:
                q.append((r, c))

    if fresh == 0:
        return 0

    def is_out_bound(r: int, c: int) -> bool:
        return r < 0 or c < 0 or r >= rows or c >= cols

    while q:
        is_spread = False
        size = len(q)
        for _ in range(size):
            r, c = q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                a, b = r + dr, c + dc
                if is_out_bound(a, b):
                    continue
                if grid[a][b] == 1:
                    grid[a][b] = 2
                    q.append((a, b))
                    is_spread = True
                    fresh -= 1
        if is_spread:
            minutes += 1

    return minutes if fresh == 0 else -1


print("Minutes:", mins_for_rotting(grid))
