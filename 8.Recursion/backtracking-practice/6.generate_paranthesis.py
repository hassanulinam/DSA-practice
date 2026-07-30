# https://leetcode.com/problems/generate-parentheses


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result: list[str] = []

        def backtrack(open: int, close: int, curr: str):
            if len(curr) == 2 * n:
                result.append(curr)

            if open < n:
                backtrack(open + 1, close, curr + "(")
            if close < open and close < n:
                backtrack(open, close + 1, curr + ")")

        backtrack(0, 0, "")
        return result


n = int(input("Enter n: "))
print(Solution().generateParenthesis(n))
