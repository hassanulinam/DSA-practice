from collections import deque

from graph_commons import directions, is_out_bound_index_in_grid

# 1 -> active (that needs to spread),
# 0 -> empty cell,
# -1 -> wall (can't enter or pass through)


def get_distances_from_ones(mat: list[list[int]]) -> list[list[int]]:
    rows, cols = len(mat), len(mat[0])
    dist: list[list[int]] = [[-2] * cols for r in range(rows)]
    q: deque[tuple[int, int]] = deque([])

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1:
                q.append((i, j))
                dist[i][j] = 0
            elif mat[i][j] == -1:
                # earlier indication of walls. `-2` nodes are the only unvisited ones now
                dist[i][j] = -1

    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = dr + r, dc + c
            if is_out_bound_index_in_grid(nr, nc, rows, cols):
                continue
            # update the unvisited nodes
            if dist[nr][nc] == -2:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    # update unreachable nodes
    for r in range(rows):
        for c in range(cols):
            if dist[r][c] == -2:
                dist[r][c] = -1
    return dist


mat1 = [
    [1, 0, 0],
    [0, -1, 0],
    [0, 0, 0],
]
mat2 = [
    [0, 0, 0],
    [0, -1, 0],
    [1, 0, 0],
]
mat3 = [
    [1, -1, 0],
    [-1, -1, 0],
    [0, 0, 0],
]
print(get_distances_from_ones(mat1))
print(get_distances_from_ones(mat2))
print(get_distances_from_ones(mat3))
