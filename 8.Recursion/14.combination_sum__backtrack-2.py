def generate_combination_sums(nums: list[int], target: int) -> list[list[int]]:
    result: list[list[int]] = []

    def backtrack(start: int, remaining: int, path: list[int]):
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i, remaining - nums[i], path)
            path.pop()

    backtrack(0, target, [])

    return result


arr = list(map(int, input("Enter arr: ").split()))
target = int(input("Enter Target: "))
print(generate_combination_sums(arr, target))
