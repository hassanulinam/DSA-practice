from math import ceil, floor


def is_palindrome(word: str) -> bool:
    left, right = 0, len(word) - 1

    while left <= right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome_from_center(word: str) -> bool:
    start, end = 0, len(word) - 1
    center = (end - start) / 2
    L, R = floor(center), ceil(center)

    while L >= 0 and R <= end:
        if word[L] != word[R]:
            return False
        L -= 1
        R += 1
    return True


word = input("Enter Word: ")
print(f"is palindrome: {is_palindrome(word)}")
print(f"is palindrome: {is_palindrome_from_center(word)}")
