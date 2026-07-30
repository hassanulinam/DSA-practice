# https://leetcode.com/problems/regular-expression-matching


class Solution:
    def isMatch(self, word: str, pattern: str) -> bool:
        sp = 0
        rp = 0

        # last_char = word[0]
        # while sp < len(word) and rp < len(pattern):
        #     if pattern[rp] == ".":
        #         last_char = word[sp]
        #         sp += 1
        #         rp += 1
        #     elif pattern[rp] == "*":
        #         if pattern[rp - 1] == ".":
        #             sp = len(word) - 1

        #         while sp < len(word) and word[sp] == last_char:
        #             sp += 1
        #         rp += 1
        #         if sp < len(word):
        #             last_char = word[sp]
        #         else:
        #             last_char = word[-1]
        #     elif pattern[rp] == word[sp]:
        #         rp += 1
        #         sp += 1
        #     else:
        #         return False

        # is_s_pending = len(word[sp:]) > 0
        # is_pattern_pending = len(pattern[rp:]) > 0
        # return not (is_s_pending or is_pattern_pending)


word = input("Enter word: ")
pattern = input("Enter pattern: ")
print(Solution().isMatch(word, pattern))
