# https://leetcode.com/problems/string-to-integer-atoi


class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        ans, i, n, sign = 0, 0, len(s), 1
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1
        while i < n and s[i] == " ":
            i += 1

        if i < n and s[i] == "-":
            sign = -1
            i += 1
        elif i < n and s[i] == "+":
            i += 1

        while i < n and s[i].isdigit():
            ans = ans * 10 + int(s[i])
            if sign * ans <= INT_MIN:
                return INT_MIN
            if sign * ans >= INT_MAX:
                return INT_MAX
            i += 1

        return sign * ans


print(Solution().myAtoi(""))
