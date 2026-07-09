# https://leetcode.com/problems/triangle
"""Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below.
More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

2
3 4
6 5 7
4 1 8 3
"""


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = [[0] * (i + 1) for i in range(len(triangle))]
        m = len(triangle)
        dp[0][0] = triangle[0][0]
        for i in range(1, m):
            for j in range(len(dp[i])):
                prev_bound = max(j - 1, 0)
                prev_optimum = min(dp[i - 1][prev_bound : j + 1])
                dp[i][j] = triangle[i][j] + prev_optimum
        return min(dp[-1])


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
sol = Solution()
print(sol.minimumTotal(triangle))
