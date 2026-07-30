class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat

        if m == r and n == c:
            return mat

        ans = [[0] * c for _ in range(r)]

        nr, nc = 0, 0
        for i in range(m):
            for j in range(n):
                ans[nr][nc] = mat[i][j]
                if nc + 1 < c:
                    nc += 1
                elif nc == c - 1:
                    nr += 1
                    nc = 0
        return ans


mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 9, 0],
    [4, 1, 4],
    [7, 0, 9],
]
sol = Solution().matrixReshape(mat, 3, 5)
for row in sol:
    print(*row)
