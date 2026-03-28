def longest_prefix(arr: list[str]) -> str:
    pivot = arr[0]
    for i in range(1, len(arr)):
        if len(arr[i]) < len(pivot):
            pivot = arr[i]

    plen = len(pivot)
    for i in range(plen):
        is_common = True
        for word in arr:
            if word[i] != pivot[i]:
                is_common = False
                break
        if not (is_common):
            return pivot[:i]

    return pivot


words = input("Enter words arr: ").split()
print(longest_prefix(words))
