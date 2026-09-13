def next_greater_elements(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)
    return result


def next_smaller_element(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[i] < nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    return result


nums = list(map(int, input("Enter arr: ").split()))
print(*next_greater_elements(nums))
print(*next_smaller_element(nums))
