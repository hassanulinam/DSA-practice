def majorityElement(nums: list[int]) -> int:
    n = len(nums)

    # Moore's voting algo (war strategy, population with majority wins on battle)
    current_num = nums[0]
    current_strength = 1

    for i in range(1, n):
        if nums[i] == current_num:
            current_strength += 1
        else:
            current_strength -= 1
            if current_strength <= 0:  # select new number
                current_num = nums[i]
                current_strength = 1

    freq = 0
    for i in range(n):
        if current_num == nums[i]:
            freq += 1

    if freq > n // 2:
        return current_num
    return -1


arr = [1, 3, 1, 1, 4, 1, 1, 5, 1, 1, 6, 2, 2]
print(majorityElement(arr))
