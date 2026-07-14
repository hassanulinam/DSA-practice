# https://leetcode.com/problems/longest-common-subsequence
"""Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0."""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[-1] * n for _ in range(m)]

        def lcs(i: int, j: int) -> int:
            if i >= m or j >= n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if text1[i] == text2[j]:
                dp[i][j] = 1 + lcs(i + 1, j + 1)
            else:
                dp[i][j] = max(lcs(i + 1, j), lcs(i, j + 1))
            return dp[i][j]

        return lcs(0, 0)


t1 = input("Enter Txt-1: ")
t2 = input("Enter Txt-2: ")
sol = Solution()
print(sol.longestCommonSubsequence(t1, t2))
