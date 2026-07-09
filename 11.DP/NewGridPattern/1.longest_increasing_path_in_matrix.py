# https://leetcode.com/problems/longest-increasing-path-in-a-matrix
"""Given an m x n integers matrix, return the length of the longest increasing path in matrix.
From each cell, you can either move in four directions: left, right, up, or down.
You may not move diagonally or move outside the boundary


matrix = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1],
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
"""


class Solution:
    def is_in_bound(self, nr: int, nc: int, rows: int, cols: int) -> bool:
        return nr >= 0 and nc >= 0 and nr < rows and nc < cols

    def get_adjancency_matrix(self, mx: list[list[int]]) -> dict[int, list[int]]:
        graph: dict[int, set[int]] = {}
        m, n = len(mx), len(mx[0])

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for i in range(m):
            for j in range(n):
                if mx[i][j] not in graph.keys():
                    graph[mx[i][j]] = set()
                for dr, dc in directions:
                    nr, nc = i + dr, j + dc
                    if self.is_in_bound(nr, nc, m, n):
                        graph[mx[i][j]].add(mx[nr][nc])

        update_graph: dict[int, list[int]] = {}
        for v in graph.keys():
            update_graph[v] = list(graph[v])
        return update_graph

    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        graph = self.get_adjancency_matrix(matrix)
        # maxKey = max(graph.keys())
        memo: dict[int, int] = {}

        def dfs(start: int) -> int:
            if start in memo:
                return memo[start]

            distances = [0]
            for node in graph[start]:
                if node < start:
                    if node in memo:
                        distances.append(memo[node])
                    else:
                        memo[node] = dfs(node)
                        distances.append(memo[node])
            return max(distances) + 1

        ans = 0
        for each_key in graph.keys():
            ans = max(ans, dfs(each_key))

        return ans


matrix = [
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1],
]
sol = Solution()
print(sol.longestIncreasingPath(matrix))
