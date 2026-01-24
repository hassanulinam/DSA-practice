def word_hash(word: str) -> tuple[int, ...]:
    freq = [0] * 26
    for c in word:
        freq[ord(c) - ord("a")] += 1
    return tuple(freq)


def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = dict[tuple[int, ...], list[str]]()

    for word in strs:
        whash = word_hash(word)
        # whash = "".join(sorted(word))
        if whash in groups:
            groups[whash].append(word)
        else:
            groups[whash] = [word]

    return list(groups.values())


k = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(k)
