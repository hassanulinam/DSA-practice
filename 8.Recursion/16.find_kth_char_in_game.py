class Solution2:
    def kthCharacter(self, k: int) -> str:
        def get_next_path(path: str) -> str:
            a = ord("a")
            res = ""
            for i in range(len(path)):
                new = a + ((ord(path[i]) - a + 1) % 26)
                res += chr(new)
            return res

        res = "a"
        while len(res) < k:
            res += get_next_path(res)
        return res[k - 1]


print(Solution2().kthCharacter(3))
