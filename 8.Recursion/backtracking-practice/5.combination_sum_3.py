# https://leetcode.com/problems/combination-sum-iii?envType=problem-list-v2&envId=backtracking
class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result: list[list[int]] = []
        nums = list(range(1, 10))

        def backtrack(remaining: int, path: list[int], start: int) -> None:
            if len(path) == k:
                if remaining == 0:
                    result.append(path[:])
                return  # once we hit the length k, there's no need to dig deeper

            for i in range(start, len(nums)):
                # if the current number is greater than remaining, there's not point of loop
                if nums[i] > remaining:
                    break
                path.append(nums[i])
                backtrack(remaining - nums[i], path, i + 1)
                path.pop()

        backtrack(n, [], 0)
        return result


k = int(input("Enter K: "))
n = int(input("Enter N: "))
print(Solution().combinationSum3(k, n))
