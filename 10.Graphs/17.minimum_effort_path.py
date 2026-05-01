import heapq


def min_effort_path(grid: list[list[int]]) -> int:
    if not grid:
        return -1
    m, n = len(grid), len(grid[0])
    efforts = [[float("inf")] * n for i in range(m)]
    starting_cell_effort = 0
    efforts[0][0] = starting_cell_effort
    heap = [(starting_cell_effort, 0, 0)]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while heap:
        current_effort, r, c = heapq.heappop(heap)
        if r == m - 1 and c == n - 1:
            return current_effort
        if current_effort > efforts[r][c]:
            continue
        current_cost = grid[r][c]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                new_cost = abs(grid[nr][nc] - current_cost)
                new_effort = max(current_effort, new_cost)
                if new_effort < efforts[nr][nc]:
                    efforts[nr][nc] = new_effort
                    heapq.heappush(heap, (new_effort, nr, nc))
    return -1


heights = [
    [1, 2, 2],
    [3, 8, 2],
    [5, 3, 5],
]
print(min_effort_path(heights))


"""
# 🧩 Next Problem: Minimum Effort Path

## 🔹 Description

You are given a grid:

```python
heights = [
    [1, 2, 2],
    [3, 8, 2],
    [5, 3, 5]
]
```

---

## 🔹 Movement rule

From `(r, c)` → `(nr, nc)`

Cost is:

```python
abs(heights[r][c] - heights[nr][nc])
```

---

## 🔹 Path cost definition (IMPORTANT)

Unlike before:

❌ Not sum of costs

✅ Path cost = **maximum edge cost along the path**

---

## 🔹 Goal

Minimize that maximum value.

---

## 🔹 Example

Best path gives:

```text
2
```

---

# 🧠 Why this is a big deal

This breaks your current assumption:

```python
new_cost = current_cost + something  ❌
```

Now:

```python
new_cost = max(current_cost, edge_cost)  ✅
```

---
"""
