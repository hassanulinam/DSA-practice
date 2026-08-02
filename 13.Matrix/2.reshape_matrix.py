class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        if (m * n != r * c) or (m == r and n == c):
            return mat

        ans = [[0] * c for _ in range(r)]
        for k in range(m * n):
            ans[k // c][k % c] = mat[k // n][k % n]
        return ans


mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 9, 0],
    [4, 1, 4],
    [7, 0, 9],
    [1, 2, 3],
]
sol = Solution().matrixReshape(mat, 2, 9)
for row in sol:
    print(*row)
