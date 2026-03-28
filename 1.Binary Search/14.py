# https://leetcode.com/problems/search-in-rotated-sorted-array
#
def findPivot(arr: list[int]):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (right + left) // 2

        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    return left  # return minimum element's index


def getIndexOfBinarySearch(arr: list[int], target: int, left: int, right: int) -> int:
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            return mid

    return -1


def search(nums: list[int], target: int) -> int:
    pivot = findPivot(nums)
    print("Pivot:", pivot)
    left_find = getIndexOfBinarySearch(nums, target, 0, pivot - 1)
    if left_find == -1:
        # print("rigt find")
        return getIndexOfBinarySearch(nums, target, pivot, len(nums) - 1)
    # print("left find")
    return left_find


inputs = [
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([4, 5, -8, -7, 0, 1, 2], 3),
    ([1, 2, 3, 4, 5, 6, 7], 5),
    ([4, 5, 6, 7, 0, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 4),
    ([4, 5, 6, 7, 8, 1, 2], 2),
]

for nums, target in inputs:
    print(nums, " :: ", target, "\t -->", search(nums, target))
