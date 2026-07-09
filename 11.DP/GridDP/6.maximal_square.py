# https://leetcode.com/problems/maximal-square
"""Given an m x n binary matrix filled with 0's and 1's,find the largest square containing only 1's and return its area."""


class Solution:
    def maximalSquare(self, mx: list[list[str]]) -> int:
        if not mx or len(mx) < 1:
            return 0
        m, n = len(mx), len(mx[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        result = 0
        for i in range(m):
            for j in range(n):
                if mx[i][j] == "1":
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1
                    result = max(result, dp[i + 1][j + 1])
        return result**2


matrix = [
    ["1", "0", "1", "0", "0", "1", "1", "1", "0"],
    ["1", "1", "1", "0", "0", "0", "0", "0", "1"],
    ["0", "0", "1", "1", "0", "0", "0", "1", "1"],
    ["0", "1", "1", "0", "0", "1", "0", "0", "1"],
    ["1", "1", "0", "1", "1", "0", "0", "1", "0"],
    ["0", "1", "1", "1", "1", "1", "1", "0", "1"],
    ["1", "0", "1", "1", "1", "0", "0", "1", "0"],
    ["1", "1", "1", "0", "1", "0", "0", "0", "1"],
    ["0", "1", "1", "1", "1", "0", "0", "1", "0"],
    ["1", "0", "0", "1", "1", "1", "0", "0", "0"],
]
sol = Solution()
print(sol.maximalSquare(matrix))
