"""https://leetcode.com/problems/n-th-tribonacci-number
The Tribonacci sequence Tn is defined as follows:
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 1:
            return 0
        if n < 3:
            return 1
        if n < 4:
            return 2

        dp = {0: 0, 1: 1, 2: 1, 3: 2}
        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]


n = int(input("Enter n: "))
sol = Solution()
print(sol.tribonacci(n))
