# https://leetcode.com/problems/search-in-rotated-sorted-array


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)

        def find_pivot():
            low, high = 0, n - 1
            while low < high:
                mid = (low + high) >> 1
                if nums[mid] > nums[high]:
                    low = mid + 1
                else:
                    high = mid
            return low

        def bs(low: int, high: int) -> int:
            while low <= high:
                mid = (low + high) >> 1
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        pivot = find_pivot()
        first_part = bs(0, pivot - 1)
        if first_part != -1:
            return first_part
        second_part = bs(pivot, n - 1)
        return second_part


arr = list(map(int, input("Enter arr: ").split()))
k = int(input("Enter target: "))
print(Solution().search(arr, k))
