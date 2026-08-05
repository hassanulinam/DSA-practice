# https://leetcode.com/problems/word-search


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        w = len(word)
        seen = [[False] * n for _ in range(m)]

        def dfs(r: int, c: int, i: int):
            if i == w:
                return True
            if not (0 <= r < m and 0 <= c < n):
                return False
            if seen[r][c] or board[r][c] != word[i]:
                return False
            seen[r][c] = True
            ok = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            seen[r][c] = False
            return ok

        return any(dfs(r, c, 0) for r in range(m) for c in range(n))


board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"],
]
word = input("Enter word: ")
print(Solution().exist(board, word))
