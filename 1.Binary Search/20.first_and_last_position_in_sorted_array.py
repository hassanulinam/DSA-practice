# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def lower_bound(x: int) -> int:
            low, high = 0, len(nums)
            while low < high:
                mid = (low + high) >> 1
                if nums[mid] < x:
                    low = mid + 1
                else:
                    high = mid
            return low

        left = lower_bound(target)
        right = lower_bound(target + 1) - 1
        return [left, right] if left <= right else [-1, -1]


arr = list(map(int, input("Enter arr: ").split()))
k = int(input("Enter target: "))
print(Solution().searchRange(arr, k))
