# https://leetcode.com/problems/longest-increasing-path-in-a-matrix
"""Given an m x n integers matrix, return the length of the longest increasing path in matrix.
From each cell, you can either move in four directions: left, right, up, or down.
You may not move diagonally or move outside the boundary


matrix = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1],
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
"""


class Solution:
    def is_in_bound(self, nr: int, nc: int, m: int, n: int) -> bool:
        return nr >= 0 and nc >= 0 and nr < m and nc < n

    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(i: int, j: int) -> int:
            if not dp[i][j]:
                vals = [0]
                for dr, dc in directions:
                    nr, nc = dr + i, dc + j
                    if self.is_in_bound(nr, nc, m, n) and matrix[i][j] > matrix[nr][nc]:
                        vals.append(dfs(nr, nc))
                dp[i][j] = 1 + max(vals)
            return dp[i][j]

        return max(dfs(x, y) for x in range(m) for y in range(n))


matrix = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1],
]
sol = Solution()
print(sol.longestIncreasingPath(matrix))
