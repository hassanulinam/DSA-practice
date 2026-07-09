"""Find the minimum sum of values collected from top-left to bottom-right."""


class Solution:
    def minSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                top = dp[i - 1][j] if i > 0 else 9223372036854775807
                left = dp[i][j - 1] if j > 0 else 9223372036854775807
                dp[i][j] = grid[i][j] + min(top, left)
        return dp[m - 1][n - 1]


inpGrid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1],
]
sol = Solution()
print(sol.minSum(inpGrid))
