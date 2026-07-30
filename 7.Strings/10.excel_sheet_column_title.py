# https://leetcode.com/problems/excel-sheet-column-title


class Solution:
    def convertToTitle(self, cln: int) -> str:
        ans = ""
        while cln > 0:
            cln -= 1
            ans = chr(ord("A") + cln % 26) + ans
            cln //= 26
        return ans


n = int(input("Enter column number: "))
print(Solution().convertToTitle(n))
