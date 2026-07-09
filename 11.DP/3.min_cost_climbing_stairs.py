# https://leetcode.com/problems/min-cost-climbing-stairs
"""You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor."""


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return min(dp[n - 1], dp[n - 2])

    def minCostOptimal(self, cost: list[int]) -> int:
        a, b = cost[0], cost[1]
        for i in range(2, len(cost)):
            curr = cost[i] + min(a, b)
            a, b = b, curr
        return min(a, b)


cost = list(map(int, input("Enter costs: ").split()))
sol = Solution()
print(sol.minCostClimbingStairs(cost))
print(sol.minCostOptimal(cost))
