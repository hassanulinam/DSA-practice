# https://leetcode.com/problems/longest-common-subsequence
"""Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0."""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cols, rows = len(text1), len(text2)
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                if text1[c] == text2[r]:
                    dp[r + 1][c + 1] = 1 + dp[r][c]
                else:
                    dp[r + 1][c + 1] = max(dp[r][c + 1], dp[r + 1][c])

        return dp[rows][cols]


t1 = input("Enter Txt-1: ")
t2 = input("Enter Txt-2: ")
sol = Solution()
print(sol.longestCommonSubsequence(t1, t2))
