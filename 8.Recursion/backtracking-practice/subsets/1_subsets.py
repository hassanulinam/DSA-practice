# LeetCode 78 - Subsets
# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        Find all possible subsets (the power set) of the given array.

        Approach:
        - For each element, we have two choices:
          1. Include it in the current subset
          2. Exclude it from the current subset
        - Process all elements recursively

        Time: O(2^n * n) where n is input size
        Space: O(n) for recursion stack

        Alternative: can use bit manipulation to generate 2^n subsets
        """
        result: list[list[int]] = []

        def backtrack(start: int, path: list[int]) -> None:
            # Add current subset to result
            result.append(path[:])

            # Try adding each remaining element
            for i in range(start, len(nums)):
                path.append(nums[i])           # Include
                backtrack(i + 1, path)         # Recurse
                path.pop()                     # Backtrack - Exclude

        backtrack(0, [])
        return result


# Test
if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
