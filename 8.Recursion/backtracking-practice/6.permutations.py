# https://leetcode.com/problems/permutations?envType=problem-list-v2&envId=backtracking


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        n = len(nums)

        used = [False] * n

        def backtrack(path: list[int]) -> None:
            if len(path) == n:
                result.append(path[:])
                return

            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])

                backtrack(path)

                path.pop()
                used[i] = False

        backtrack([])

        return result


arr = list(map(int, input("Enter arr: ").split()))
permutations = Solution().permute(arr)
print("Permuations length: ", len(permutations))
print(permutations)
