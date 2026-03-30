# https://leetcode.com/problems/combination-sum-ii?envType=problem-list-v2&envId=backtracking
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result: list[list[int]] = []
        candidates = sorted(candidates)

        def backtrack(remaining: int, start: int, path: list[int]) -> None:
            if remaining == 0:
                result.append(path[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(remaining - candidates[i], i + 1, path)
                path.pop()

        backtrack(target, 0, [])

        return result


arr = list(map(int, input("Enter arr: ").split()))
target = int(input("Enter target: "))
print(Solution().combinationSum2(arr, target))
