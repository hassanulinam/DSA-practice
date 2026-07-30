class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if m < n:
            return -1

        for i in range(m - n + 1):
            j = 0
            while j < n and haystack[i + j] == needle[j]:
                j += 1
            if j == n:
                return i
        return -1


hay = input("Enter haystack: ")
need = input("Enter needle: ")
print(Solution().strStr(hay, need))
