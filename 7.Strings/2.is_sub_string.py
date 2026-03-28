def isSubString(word: str, start: int, end: int, subStr: str) -> bool:
    subStrStartIndex = start
    while start <= end:
        if subStr[subStrStartIndex - start] != word[start]:
            return False
        start += 1
    return True


word = input("Enter word: ")
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))
subStr = input("Enter sub string: ")
print(f"is Substring: {isSubString(word, start, end, subStr)}")
