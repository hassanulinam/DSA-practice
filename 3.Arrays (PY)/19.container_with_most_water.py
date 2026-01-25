# https://leetcode.com/problems/container-with-most-water


def maxArea(height: list[int]) -> int:
    n = len(height)
    max_capacity = 0
    left, right = 0, n - 1

    while left < right:
        area = (right - left) * min(height[left], height[right])
        max_capacity = max(max_capacity, area)

        if height[right] > height[left]:
            left += 1
        else:
            right -= 1

    return max_capacity


inputs = [[1, 8, 6, 2, 5, 4, 8, 3, 7], [1, 1]]
for x in inputs:
    print(maxArea(x))
