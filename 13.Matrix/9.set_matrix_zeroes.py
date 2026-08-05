# https://leetcode.com/problems/set-matrix-zeroes


class Solution:
    def setZeroes(self, mat: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(mat), len(mat[0])
        # remember if first colum or first row had zeroes
        row0 = any(mat[0][c] == 0 for c in range(n))
        col0 = any(mat[r][0] == 0 for r in range(m))

        # mark zeroes in row[0] & col[0] to fill later.
        for i in range(1, m):
            for j in range(1, n):
                if mat[i][j] == 0:
                    mat[i][0] = 0
                    mat[0][j] = 0

        # Start filling zeroes
        for i in range(1, m):
            for j in range(1, n):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0

        if row0:
            for c in range(n):
                mat[0][c] = 0
        if col0:
            for r in range(m):
                mat[r][0] = 0
