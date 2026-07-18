# https://leetcode.com/problems/edit-distance
"""Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:
Insert a character
Delete a character
Replace a character

if S1[i] == S2[j]:
    dp[i][j] = 0
else:


"""


class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        rows, cols = len(s1), len(s2)
        dp = [[-1] * (cols) for _ in range(rows)]

        def recurse(i: int, j: int) -> int:
            if i == rows:
                return cols - j
            if j == cols:
                return rows - i

            if dp[i][j] != -1:
                return dp[i][j]

            if s1[i] == s2[j]:
                dp[i][j] = recurse(i + 1, j + 1)
            else:
                deletion = recurse(i + 1, j)
                insertion = recurse(i, j + 1)
                replacement = recurse(i + 1, j + 1)
                dp[i][j] = 1 + min(deletion, insertion, replacement)

            return dp[i][j]

        return recurse(0, 0)


t1 = input("Enter Txt-1: ")
t2 = input("Enter Txt-2: ")
sol = Solution()
print(sol.minDistance(t1, t2))
