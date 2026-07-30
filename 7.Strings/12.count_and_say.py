# https://leetcode.com/problems/count-and-say


class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 1:
            return "1"

        def encode(s: str) -> str:
            enc = ""
            last = s[0]
            i = 1
            freq = 1
            while i < len(s):
                if s[i] == last:
                    freq += 1
                else:
                    enc += str(freq) + last
                    last = s[i]
                    freq = 1
                i += 1
            enc += str(freq) + last
            return enc

        res = "1"
        for i in range(n - 1):
            res = encode(res)
        return res
