def largest_rect_area(nums: list[int]) -> int:
    max_area = nums[0] * nums[1]
    stack = []

    for i, curr_height in enumerate(nums):
        while stack and curr_height < nums[stack[-1]]:
            prev_idx = stack.pop()
            width = i - prev_idx
            curr_area = width * curr_height
            max_area = max(max_area, curr_area)
        stack.append(i)

    return max_area


arr = list(map(int, input("Enter heights:").split()))
print(largest_rect_area(arr))
