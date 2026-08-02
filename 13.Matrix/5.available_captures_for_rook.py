# https://leetcode.com/problems/available-captures-for-rook


class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        ans = 0
        rr = cc = -1
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    rr, cc = i, j
                    break
            if rr != -1:
                break
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for nr, nc in dirs:
            r, c = rr + nr, cc + nc
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == "B":
                    break
                if board[r][c] == "p":
                    ans += 1
                    break
                r += nr
                c += nc
        return ans


board = [
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", "p", "p", "p", "p", "p", ".", "."],
    [".", "p", "p", "B", "p", "p", ".", "."],
    [".", "p", "B", "R", "B", "p", ".", "."],
    [".", "p", "p", "B", "p", "p", ".", "."],
    [".", "p", "p", "p", "p", "p", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
]
print(Solution().numRookCaptures(board))
