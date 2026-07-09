# https://leetcode.com/problems/house-robber
"""🏠 House Robber
You are a robber planning to rob houses along a street.
Each house contains some amount of money.
The only constraint:
You cannot rob two adjacent houses.
Return the maximum amount of money you can rob."""


class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * (n)
        dp[0] = nums[0]
        if n > 1:
            dp[1] = max(nums[:2])
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[n - 1]

    def rob_optimal(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        a, b = nums[0], max(nums[:2])
        for i in range(2, n):
            curr = max(nums[i] + a, b)
            a, b = b, curr
        return b


houses = list(map(int, input("Enter amounts: ").split()))
sol = Solution()
print(sol.rob(houses))
print(sol.rob_optimal(houses))
