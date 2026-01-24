def isAnagram(s: str, t: str) -> bool:
    letters = dict()
    if len(s) != len(t):
        return False

    for c in s:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1

    for c in t:
        if c in letters:
            letters[c] -= 1
        else:
            return False

    for remaining_count in letters.values():
        if remaining_count != 0:
            return False
    return True


print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "acr"))
