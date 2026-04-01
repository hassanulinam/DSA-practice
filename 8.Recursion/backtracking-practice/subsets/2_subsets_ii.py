# LeetCode 90 - Subsets II
# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        """
        Find all possible subsets given an array that may contain duplicates.
        The solution set must not contain duplicate subsets.

        Approach:
        - Similar to Subsets, but with duplicate handling
        - Sort the array to group duplicates
        - Skip duplicates at same recursion level (like Combination Sum II)
        - Key insight: only skip if current == prev AND prev is not used at this level

        Time: O(m * 2^n) where m is average result length
        Space: O(n) for recursion stack

        Key difference from Subsets: duplicate handling with sorted array
        """
        result: list[list[int]] = []

        # Sort to group duplicates
        nums.sort()

        def backtrack(start: int, path: list[int]) -> None:
            # Add current subset
            result.append(path[:])

            for i in range(start, len(nums)):
                # Skip duplicates at same recursion level
                # If this number was already used at this level, skip
                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result


# Test
if __name__ == "__main__":
    nums = [1, 2, 2]
    print(Solution().subsetsWithDup(nums))
