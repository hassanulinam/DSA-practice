# https://leetcode.com/problems/spiral-matrix-ii


class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        t, b = 0, n - 1
        l, r = 0, n - 1
        current_number = 0
        mat = [[0] * n for _ in range(n)]

        def next():
            nonlocal current_number
            current_number += 1
            return current_number

        while t <= b and l <= r:
            # top left -> top right
            for i in range(l, r + 1):
                mat[t][i] = next()
            t += 1
            # top right -> bottom right
            for i in range(t, b + 1):
                mat[i][r] = next()
            r -= 1

            if t <= b:  # bottom right -> bottom left
                for i in range(r, l - 1, -1):
                    mat[b][i] = next()
                b -= 1

            if l <= r:  # bottom left -> top left
                for i in range(b, t - 1, -1):
                    mat[i][l] = next()
                l += 1

        return mat


n = int(input("Enter N: "))
sol = Solution().generateMatrix(n)
for row in sol:
    print(*row)
