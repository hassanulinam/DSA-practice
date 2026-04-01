# LeetCode 39 - Combination Sum
# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Find all unique combinations in candidates where the candidate numbers sum to target.
        The same repeated number may be chosen from candidates an unlimited number of times.

        Approach:
        - Use backtracking with two choices at each step:
          1. Include current candidate and stay at same index (can reuse)
          2. Skip current candidate and move to next index
        - Pruning: if candidate > remaining target, stop (since array is sorted)

        Time: O(R) where R is total combinations
        Space: O(target) for recursion stack
        """
        result: list[list[int]] = []

        def backtrack(start: int, remaining: int, path: list[int]) -> None:
            # Base case: found valid combination
            if remaining == 0:
                result.append(path[:])
                return

            # Try each candidate from current index onwards
            for i in range(start, len(candidates)):
                # Pruning: if candidate exceeds remaining target, no point continuing
                if candidates[i] > remaining:
                    break

                # Include current candidate and recurse (same index = can reuse)
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i], path)  # Note: i not i+1
                path.pop()  # Backtrack

        backtrack(0, target, [])
        return result


# Test
if __name__ == "__main__":
    candidates = [2, 3, 5]
    target = 8
    print(Solution().combinationSum(candidates, target))
