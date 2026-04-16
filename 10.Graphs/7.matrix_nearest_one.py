from collections import deque

from graph_commons import directions, is_out_bound_index_in_grid


def nearest_ones(mat: list[list[int]]) -> list[list[int]]:
    dist: list[list[int]] = []
    rows, cols = len(mat), len(mat[0])
    q: deque[tuple[int, int]] = deque([])
    for i in range(rows):
        row = []
        for j in range(cols):
            if mat[i][j] == 1:
                q.append((i, j))
                row.append(0)
            else:
                row.append(-1)
        dist.append(row)

    while q:
        r, c = q.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if is_out_bound_index_in_grid(nr, nc, rows, cols):
                continue
            if dist[nr][nc] == -1:
                q.append((nr, nc))
                dist[nr][nc] = dist[r][c] + 1

    return dist


mat: list[list[int]] = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1],
]

print("Nearest ones:", nearest_ones(mat))
