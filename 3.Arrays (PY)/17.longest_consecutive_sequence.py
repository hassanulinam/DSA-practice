# https://leetcode.com/problems/longest-consecutive-sequence


def longestConsecutive(nums: list[int]) -> int:
    nums2 = set(nums)

    longest = 0

    for x in nums2:
        streak = 0
        if x - 1 not in nums2:
            while x + streak in nums2:
                streak += 1
            longest = max(longest, streak)
    return longest


inputs = [[100, 4, 200, 1, 3, 2], [0, 3, 7, 2, 5, 8, 4, 6, 0, 1], [1, 0, 1, 2]]
for x in inputs:
    print(longestConsecutive(x))
