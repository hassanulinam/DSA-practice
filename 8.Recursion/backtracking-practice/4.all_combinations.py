# https://leetcode.com/problems/combinations?envType=problem-list-v2&envId=backtracking
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result: list[list[int]] = []

        def backtrack(path: list[int], curr: int):
            if len(path) == k:
                result.append(path[:])
                return

            for i in range(curr, n + 1):
                path.append(i)
                backtrack(path, i + 1)
                path.pop()

        backtrack([], 1)
        return result


arr = list(map(int, input("Enter range: ").split()))
print(Solution().combine(arr[0], arr[1]))
