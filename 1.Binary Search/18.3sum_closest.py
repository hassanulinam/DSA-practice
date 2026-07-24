# https://leetcode.com/problems/3sum-closest


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        ans = sum(nums[:3])
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                csm = nums[i] + nums[left] + nums[right]
                if csm == target:
                    return csm
                elif csm < target:
                    left += 1
                else:
                    right -= 1

                if abs(target - csm) < abs(target - ans):
                    ans = csm
        return ans


arr = list(map(int, input("Enter arr: ").split()))
target = int(input("Enter target: "))
print(Solution().threeSumClosest(arr, target))
