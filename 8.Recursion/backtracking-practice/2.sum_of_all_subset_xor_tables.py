# https://leetcode.com/problems/sum-of-all-subset-xor-totals?envType=problem-list-v2&envId=backtracking
class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        total = 0

        def backtrack(start: int, current_xor: int) -> None:
            nonlocal total
            total += current_xor

            for i in range(start, len(nums)):
                backtrack(i + 1, current_xor ^ nums[i])

        backtrack(0, 0)
        return total


arr = list(map(int, input("Enter arr: ").split()))
print(Solution().subsetXORSum(arr))
