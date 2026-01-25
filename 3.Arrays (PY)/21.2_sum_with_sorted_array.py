# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
def twoSum(numbers: list[int], target: int) -> list[int]:
    n = len(numbers)
    left, right = 0, n - 1
    while left < right:
        need = target - numbers[right]

        if need < numbers[left]:
            right -= 1
        elif need > numbers[left]:
            left += 1
        else:
            return [left + 1, right + 1]

    return [-1]


inputs = [([2, 7, 11, 15], 9), ([2, 3, 4], 6), ([-1, 0], -1)]

for nums, target in inputs:
    print(twoSum(nums, target))
