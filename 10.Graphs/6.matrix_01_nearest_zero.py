from collections import deque

from graph_commons import directions, is_out_bound_index_in_grid


def nearest_zeroes(mat: list[list[int]]) -> list[list[int]]:
    rows, cols = len(mat), len(mat[0])
    q: deque[tuple[int, int]] = deque([])
    dist: list[list[int]] = []
    for r in range(rows):
        row = []
        for c in range(cols):
            if mat[r][c] == 0:
                q.append((r, c))
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
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

    return dist


mat: list[list[int]] = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1],
]

# [
#   [0,0,0],
#   [0,1,0],
#   [1,2,1]
# ]
#
print("Output:\n", nearest_zeroes(mat))
