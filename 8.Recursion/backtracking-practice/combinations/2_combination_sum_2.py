# LeetCode 40 - Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Find all unique combinations in candidates where the candidate numbers sum to target.
        Each number in candidates may only be used ONCE in a combination.
        The same repeated number may be chosen from candidates once per occurrence.

        Approach:
        - Sort the array to group duplicates together
        - Use backtracking with two choices:
          1. Include current candidate and move to next index
          2. Skip current candidate and move to next index
        - Duplicate handling: skip same value at same recursion level
        - Pruning: if candidate > remaining target, stop

        Key difference from Combination Sum: can't reuse same element twice

        Time: O(m * 2^n) where m is average result length, n is input size
        Space: O(target) for recursion stack
        """
        result: list[list[int]] = []

        # Sort to group duplicates
        candidates.sort()

        def backtrack(start: int, remaining: int, path: list[int]) -> None:
            # Found valid combination
            if remaining == 0:
                result.append(path[:])
                return

            # Try each candidate from current index onwards
            for i in range(start, len(candidates)):
                # Skip duplicates at same recursion level
                # If we already processed this number at this level, skip it
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Pruning
                if candidates[i] > remaining:
                    break

                # Include current and move to next index (can't reuse same element)
                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], path)
                path.pop()  # Backtrack

        backtrack(0, target, [])
        return result


# Test
if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(Solution().combinationSum2(candidates, target))
