from collections import deque

grid = [
    [0, 0, 0],
    [1, 1, 0],
    [0, 0, 0],
    [0, 1, 1],
    [0, 0, 0],
]
k = 1


def get_shortest_path_with_k_obstacles(grid: list[list[int]], k: int) -> int:
    if not grid:
        return -1
    m, n = len(grid), len(grid[0])
    visited = [[-1] * n for i in range(m)]
    # tuple[row_index, col_index, current_distance, remaining_k, visited_set]
    q: deque[tuple[int, int, int, int]] = deque([(0, 0, 0, k - grid[0][0])])

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        r, c, dist, remaining_k = q.popleft()
        if r == m - 1 and c == n - 1:
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                new_k = remaining_k - grid[nr][nc]

                if new_k < 0:
                    continue
                if visited[nr][nc] >= new_k:
                    continue

                visited[nr][nc] = new_k
                q.append((nr, nc, dist + 1, new_k))
    return -1


print(get_shortest_path_with_k_obstacles(grid, k))
