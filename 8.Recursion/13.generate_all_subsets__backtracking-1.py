def generate_subsets(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []

    def backtrack(start: int, path: list[int]) -> None:
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


k = list(map(int, input("Enter Arr: ").split()))
print(generate_subsets(k))


# result = [
#     [],
#     [12],
#     [12, 23],
#     [12, 23, 34],
#     [12, 23, 34, 45],
#     [12, 23, 34, 45, 56],
#     [12, 23, 34, 56],
#     [12, 23, 45],
#     [12, 23, 45, 56],
#     [12, 23, 56],
#     [12, 34],
#     [12, 34, 45],
#     [12, 34, 45, 56],
#     [12, 34, 56],
#     [12, 45],
#     [12, 45, 56],
#     [12, 56],
#     [23],
#     [23, 34],
#     [23, 34, 45],
#     [23, 34, 45, 56],
#     [23, 34, 56],
#     [23, 45],
#     [23, 45, 56],
#     [23, 56],
#     [34],
#     [34, 45],
#     [34, 45, 56],
#     [34, 56],
#     [45],
#     [45, 56],
#     [56],
# ]
