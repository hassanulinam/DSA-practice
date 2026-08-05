# https://leetcode.com/problems/spiral-matrix


class Solution:
    def spiralOrder(self, mat: list[list[int]]) -> list[int]:
        ans = []
        m, n = len(mat), len(mat[0])

        t, b = 0, m - 1
        l, r = 0, n - 1

        while t <= b and l <= r:
            # top left to top right pass
            ans += mat[t][l : r + 1]
            t += 1

            # top right corner to bottom right
            for i in range(t, b + 1):
                ans.append(mat[i][r])
            r -= 1

            # bottom right to bottom left
            if t <= b:
                ans += mat[b][l : r + 1][::-1]
                b -= 1

            # bottom left to top left
            if l <= r:
                for i in range(b, t - 1, -1):
                    ans.append(mat[i][l])
                l += 1
        return ans


mat = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]
print(Solution().spiralOrder(mat))

"""
[
    [1,   2,  3,  4,  5],
    [6,   7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]
"""
