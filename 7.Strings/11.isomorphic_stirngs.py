# https://leetcode.com/problems/isomorphic-strings


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)
        if n1 != n2:
            return False

        map: dict[str, str] = {}
        track: set[str] = set()
        for i in range(n1):
            if s[i] in map:
                if map[s[i]] != t[i]:
                    return False
            elif t[i] not in track:
                map[s[i]] = t[i]
                track.add(t[i])
            else:
                return False

        return True


s = input("Enter S: ")
t = input("Enter T: ")
print(Solution().isIsomorphic(s, t))
