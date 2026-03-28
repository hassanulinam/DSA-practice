def dominantIndices(nums: list[int]) -> int:
    N = len(nums)
    avgs: list[float] = [0] * N
    curr_sum = 0
    k = 0
    for i in range(N - 1, -1, -1):
        curr_sum += nums[i]
        k += 1
        avgs[i] = curr_sum / k

    dcount = 0
    for i in range(N - 1):
        if nums[i] > avgs[i + 1]:
            dcount += 1
    return dcount


arr = [4, 1, 2]
print(dominantIndices(arr))
