# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
def findMin(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


inputs = [
    [5, 6, 7, 8, -1, 0, 1, 2, 3],
    [9, 10, 1, 2, 3, 4, 5, 6, 7, 8],
    [12, 23, 45, 67, 10, 11],
    [3, 4, 5, 1, 2],
    [4, 5, 6, 7, 0, 1, 2],
    [11, 13, 15, 17],
]
for x in inputs:
    print(findMin(x))
