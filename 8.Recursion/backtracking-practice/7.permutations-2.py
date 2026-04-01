# https://leetcode.com/problems/permutations-ii?envType=problem-list-v2&envId=backtracking
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        nums = sorted(nums)
        n = len(nums)
        used = [False] * n

        def backtrack(path: list[int]) -> None:
            if len(path) == n:
                result.append(path[:])
                return

            for i in range(n):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    # try to understand the intuition behind this condition,
                    # which prevents duplicate permutations
                    continue

                used[i] = True
                path.append(nums[i])

                backtrack(path)

                path.pop()
                used[i] = False

        backtrack([])
        return result


arr = list(map(int, input("Enter arr: ").split()))
permutations = Solution().permuteUnique(arr)
print("Permuations length: ", len(permutations))
print(permutations)
