# LeetCode 216 - Combination Sum III
# https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        """
        Find all possible combinations of k numbers that sum up to n.
        Only numbers from 1 to 9 can be used, and each number can be used at most once.

        Approach:
        - Use backtracking with limited range [1, 9]
        - Two choices at each step:
          1. Include current number and move to next
          2. Skip current number and move to next
        - Stop if we've selected k numbers or remaining sum is 0

        Key constraint: exactly k numbers from 1-9

        Time: O(C(9,k) * k) - bounded by combinations of 9 elements taken k at a time
        Space: O(k) for recursion stack
        """
        result: list[list[int]] = []

        def backtrack(start: int, remaining: int, count: int, path: list[int]) -> None:
            # Pruning: if remaining sum is less than or equal to 0, invalid
            if remaining <= 0:
                return

            # Base case: found valid combination with exactly k numbers
            if count == k and remaining == 0:
                result.append(path[:])
                return

            # Optimization: stop if we need more numbers than available
            if count + (9 - start + 1) < k:
                return

            # Try each number from start to 9
            for i in range(start, 10):
                # Pruning: if adding i exceeds remaining, no point continuing
                if remaining - i <= 0:
                    break

                path.append(i)
                backtrack(i + 1, remaining - i, count + 1, path)
                path.pop()  # Backtrack

        backtrack(1, n, 0, [])
        return result


# Test
if __name__ == "__main__":
    print(Solution().combinationSum3(3, 7))  # Should return [[1, 2, 4]]
    print(Solution().combinationSum3(4, 1))  # Should return [[1, 2, 3, 4]]
