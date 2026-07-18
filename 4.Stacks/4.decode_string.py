# https://leetcode.com/problems/decode-string?envType=problem-list-v2&envId=w7bvc4cm


class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""

        if s.isalpha():
            return s

        prefix = ""
        i = 0
        while s[i].isalpha():
            prefix += s[i]
            i += 1

        n = ""
        while s[i].isnumeric():
            n += s[i]
            i += 1

        n = int(n)
        depth = 1
        start, end = i, 0
        for i in range(start + 1, len(s)):
            if s[i] == "[":
                depth += 1
            elif s[i] == "]":
                depth -= 1

            if depth == 0:
                end = i
                break

        suffix = ""
        if end != len(s) - 1:
            suffix = self.decodeString(s[end + 1 :])

        return prefix + n * self.decodeString(s[start + 1 : end]) + suffix


S = input("Enter encoded string: ")
sol = Solution()
print(sol.decodeString(S))
