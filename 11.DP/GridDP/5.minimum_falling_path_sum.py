# https://leetcode.com/problems/minimum-falling-path-sum
"""Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right.
Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1)."""
# The goal is to reach from any element of first row to any element of last row, but with minim path sum


class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]
        dp[0] = matrix[0]

        for i in range(1, n):
            for j in range(n):
                prev_left_bound = max(j - 1, 0)
                prev_optimum = min(dp[i - 1][prev_left_bound : j + 2])
                dp[i][j] = matrix[i][j] + prev_optimum
        return min(dp[-1])


matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
sol = Solution()
print(sol.minFallingPathSum(matrix))
