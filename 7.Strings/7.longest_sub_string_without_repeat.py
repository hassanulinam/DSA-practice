# https://leetcode.com/problems/longest-substring-without-repeating-characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen: dict[str, int] = {}
        left = 0
        ans = 0

        for right, char in enumerate(s):
            if char in last_seen:
                left = max(left, last_seen[char] + 1)

            last_seen[char] = right
            ans = max(ans, right - left + 1)
        return ans


print(Solution().lengthOfLongestSubstring("loddktdji"))
