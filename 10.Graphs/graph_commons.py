directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def is_out_bound_index_in_grid(
    r: int, c: int, total_rows: int, total_cols: int
) -> bool:
    return r < 0 or c < 0 or r >= total_rows or c >= total_cols
