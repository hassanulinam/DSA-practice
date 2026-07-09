# https://leetcode.com/problems/unique-paths-ii
"""You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner."""


class Solution:
    def uniquePathsWithObstacles(self, obsGrid: list[list[int]]) -> int:
        m, n = len(obsGrid), len(obsGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if obsGrid[0][0] == 0 else 0
        for i in range(m):
            for j in range(n):
                if (obsGrid[i][j] == 1) or (i == 0 and j == 0):
                    continue
                top = dp[i - 1][j] if i > 0 else 0
                left = dp[i][j - 1] if j > 0 else 0
                dp[i][j] = top + left
        return dp[m - 1][n - 1]


grid = [
    [0, 1],
    [0, 0],
]
sol = Solution()
print(sol.uniquePathsWithObstacles(grid))
