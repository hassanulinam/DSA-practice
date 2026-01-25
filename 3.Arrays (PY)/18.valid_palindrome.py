# https://leetcode.com/problems/valid-palindrome
def isPalindrome(s: str) -> bool:
    n = len(s)
    s = s.lower()
    left, right = 0, n - 1
    while left < right:
        while left < n and (not s[left].isalnum()):
            left += 1

        while right >= 0 and (not s[right].isalnum()):
            right -= 1

        if not (left < n and right >= 0):
            break

        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


inputs = ["A man, a plan, a canal: Panama", "race a car", " "]
for x in inputs:
    print(x, "-->", isPalindrome(x))
