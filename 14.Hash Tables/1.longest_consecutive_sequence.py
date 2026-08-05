class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        space = set(nums)
        ans = 1
        for n in nums:
            if n - 1 not in space:
                curr, ln = n, 1
                while curr + 1 in space:
                    curr += 1
                    ln += 1
                ans = max(ans, ln)
        return ans


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(Solution().longestConsecutive(nums))
