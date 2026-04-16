from collections import deque

from graph_commons import directions, is_out_bound_index_in_grid


def get_distances_from_ones(mat: list[list[int]]) -> list[list[int]]:
    rows, cols = len(mat), len(mat[0])
    dist: list[list[int]] = [[-1] * cols for r in range(rows)]
    q: deque[tuple[int, int]] = deque([])

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = dr + r, dc + c
            if is_out_bound_index_in_grid(nr, nc, rows, cols):
                continue
            if mat[nr][nc] == -1:
                continue
            if dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return dist


# mat = [
#     [1, 0, 0],
#     [0, -1, 0],
#     [0, 0, 0],
# ]
# mat = [
#     [0, 0, 0],
#     [0, -1, 0],
#     [1, 0, 0],
# ]
mat = [
    [1, -1, 0],
    [-1, -1, 0],
    [0, 0, 0],
]
print(get_distances_from_ones(mat))
# 1 -> active (that needs to spread),
# 0 -> empty cell,
# -1 -> wall (can't enter or pass through)
