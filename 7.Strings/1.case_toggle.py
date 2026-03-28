def toggleCase(word) -> str:
    result = []
    for i in range(len(word)):
        if word[i].isupper():
            result.append(word[i].lower())
        else:
            result.append(word[i].upper())

    return "".join(result)


word = input()
print(toggleCase(word))
