def longestSubarray(nums, k):
    prefix_sum = 0
    seen = {0: -1}
    ans = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]

        complement = prefix_sum - k
        if complement in seen:
            ans = max(ans, i - seen[complement])

        if prefix_sum not in seen:
            seen[prefix_sum] = i

    return ans


print("case-1:")
print(longestSubarray([-34, 10, 5, 2, 7, 1, 9], 15))
print("case-2:")
print(longestSubarray([-3, 2, 1], 6))
print("Case-3:")
print(longestSubarray([1, -1, 5, -2, 3], 3))
