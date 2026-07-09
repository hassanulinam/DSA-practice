# https://leetcode.com/problems/house-robber-ii
"""🏠 House Robber II
Same problem.
But now the houses form a circle."""


class Solution:
    def rob_linear(self, nums: list[int]) -> int:
        n = len(nums)
        a, b = nums[0], max(nums[:2])
        for i in range(2, n):
            curr = max(nums[i] + a, b)
            a, b = b, curr
        return b

    def rob(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        return max(self.rob_linear(nums[1:]), self.rob_linear(nums[:-1]))


houses = list(map(int, input("Enter amounts: ").split()))
sol = Solution()
print(sol.rob(houses))
