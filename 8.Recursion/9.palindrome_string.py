def is_palindrome(word: str) -> bool:
    if len(word) == 0:
        return True
    if len(word) == 1:
        return True

    return word[0] == word[-1] and is_palindrome(word[1:-1])


word = input("Enter word: ")
print(is_palindrome(word))
