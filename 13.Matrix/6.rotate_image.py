# https://leetcode.com/problems/rotate-image


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse each row
        for i in range(n):
            l, r = 0, n - 1
            row = matrix[i]
            while l < r:
                row[l], row[r] = row[r], row[l]
                l += 1
                r -= 1


mat = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]
print(Solution().rotate(mat))
for row in mat:
    print(*row)

"""
[
    [1,   2,  3,  4,  5],
    [6,   7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]
"""
