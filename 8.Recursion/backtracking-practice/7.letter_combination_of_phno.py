# https://leetcode.com/problems/letter-combinations-of-a-phone-number


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        n = len(digits)
        ans = []

        def backtrack(progress: str, k: int):
            if len(progress) == n:
                ans.append(progress)
                return

            for c in mapping[digits[k]]:
                backtrack(progress + c, k + 1)

        backtrack("", 0)
        return ans


digs = input("Enter digits from (2-9): ")
sol = Solution().letterCombinations(digs)
print(*sol)
