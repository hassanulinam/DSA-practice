# https://leetcode.com/problems/longest-valid-parentheses


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [(0, 0)] * n  # paranthesis_count, stack_pending
        ans = 0
        if s[0] == "(":
            dp[0] = (0, 1)
        for i in range(1, n):
            prev_paranth_count, prev_stack_pending = dp[i - 1]
            if s[i] == "(":
                dp[i] = (prev_paranth_count, prev_stack_pending + 1)
            else:
                dp[i] = prev_paranth_count + 2, prev_stack_pending - 1
                is_stack_empty = dp[i][1] == 0
                if is_stack_empty:
                    ans = max(ans, dp[i][0])

        return ans


paranthesis = input("Enter paranthesis: ")
print(Solution().longestValidParentheses(paranthesis))
