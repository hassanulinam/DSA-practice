from collections import deque

"""
🔷 Problem: Shortest Path in Binary Matrix (8 directions)
You’re given an n x n grid:
0 → free cell
1 → blocked cell
You need to find the shortest path from (0,0) → (n-1,n-1)
Rules:
Move in 8 directions (including diagonals)
You can only walk on 0
Return length of shortest path
If not possible → return -1
"""


def shortest_path(grid: list[list[int]]) -> int:
    n = len(grid)
    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1

    q: deque[tuple[int, int, int]] = deque([(0, 0, 1)])
    grid[0][0] = 1

    directions = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]
    while q:
        r, c, dist = q.popleft()

        if r == n - 1 and c == n - 1:
            return dist
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nr < n and grid[nr][nc] == 0:
                q.append((nr, nc, dist + 1))
                grid[nr][nc] = 1
    return -1
