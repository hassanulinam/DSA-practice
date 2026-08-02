# https://leetcode.com/problems/flood-fill


from collections import deque


class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        old_color = image[sr][sc]
        if old_color == color:
            return image
        q = deque([(sr, sc)])
        image[sr][sc] = color
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        M, N = len(image), len(image[0])

        while q:
            i, j = q.popleft()
            for kr, kc in dirs:
                nr, nc = kr + i, kc + j
                if 0 <= nr < M and 0 <= nc < N and image[nr][nc] == old_color:
                    image[nr][nc] = color
                    q.append((nr, nc))

        return image
