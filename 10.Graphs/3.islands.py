from collections import deque

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]


def get_islands_count_dfs(grid: list[list[str]]) -> int:
    total = 0
    if len(grid) == 0:
        return total
    m, n = len(grid), len(grid[0])

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= m or c < 0 or c >= n:
            return
        if grid[r][c] == "0":
            return

        grid[r][c] = "0"

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(m):
        for c in range(n):
            if grid[r][c] == "1":
                total += 1
                dfs(r, c)

    return total


def get_islands_count_bfs(grid: list[list[str]]) -> int:
    total = 0
    if len(grid) == 0:
        return total

    m, n = len(grid), len(grid[0])

    def bfs(r: int, c: int) -> None:
        q = deque([(r, c)])
        grid[r][c] = "0"
        while q:
            i, j = q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                a, b = i + dr, j + dc
                if a < 0 or b < 0 or a >= m or b >= n:
                    continue
                if (grid[a][b]) == "1":
                    grid[a][b] = "0"
                    q.append((a, b))

    for r in range(m):
        for c in range(n):
            if grid[r][c] == "1":
                total += 1
                bfs(r, c)

    return total


# print("Islands count:", get_islands_count_dfs(grid))
print("Islands count (BFS):", get_islands_count_bfs(grid))
