# https://leetcode.com/problems/4sum


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        result: list[list[int]] = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1

                while left < right:
                    csm = nums[i] + nums[j] + nums[left] + nums[right]
                    if csm == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left + 1] == nums[left]:
                            left += 1
                        while left < right and nums[right - 1] == nums[right]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif csm < target:
                        left += 1
                    else:
                        right -= 1

        return result


arr = list(map(int, input("Enter arr: ").split()))
target = int(input("Enter target: "))
print(Solution().fourSum(arr, target))
