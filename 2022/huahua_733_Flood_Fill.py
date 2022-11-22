#!/usr/bin/env python3

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        d = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
        ]

        n = len(image)
        m = len(image[0])
        visited = set()
        v = image[sr][sc]
        def dfs(y, x):
            if (y, x) in visited:
                return

            image[y][x] = color
            visited.add((y, x))

            for dy, dx in d:
                _y = dy + y
                _x = dx + x
                if 0 <= _y < n and 0 <= _x < m and image[_y][_x] == v:
                    dfs(_y, _x)

        dfs(sr, sc)
        return image
