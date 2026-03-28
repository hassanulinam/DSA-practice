def longest_substring_length(word: str) -> int:
    mlen = 0
    start, end = 0, len(word) - 1

    def is_palindrome(L: int, R: int) -> int:
        while L >= start and R <= end:
            if word[L] != word[R]:
                break
            L -= 1
            R += 1
        return R - L - 1

    for i in range(end + 1):
        odd = is_palindrome(i, i)
        even = is_palindrome(i, i + 1)
        mlen = max(odd, even, mlen)
    return mlen


def get_longest_palindrome_substring(word: str) -> str:
    ans = ""
    start, end = 0, len(word) - 1

    def get_palindrome_from_center(L: int, R: int) -> str:
        while L >= start and R <= end:
            if word[L] != word[R]:
                break
            L -= 1
            R += 1
        return word[L + 1 : R]

    for i in range(end + 1):
        odd = get_palindrome_from_center(i, i)
        even = get_palindrome_from_center(i, i + 1)
        if len(odd) > len(ans):
            ans = odd
        if len(even) > len(ans):
            ans = even
    return ans


word = input("Enter word: ")
print(f"Longest palindrom substring length: {longest_substring_length(word)}")
print(f"Palindrom substring: {get_longest_palindrome_substring(word)}")
