#!/usr/bin/env python3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        gh = len(grid)
        gw = len(grid[0])
        visited = set()

        d = [
            (1, 0),
            (0, -1),
            (-1, 0),
            (0, 1),
        ]

        r = 0
        def dfs(x, y):
            if (x, y) in visited:
                return

            visited.add((x, y))

            for dx, dy in d:
                _x = x + dx
                _y = y + dy
                if 0 <= _x <= gw-1 and 0 <= _y <= gh-1 and grid[y][x] == "1":
                    dfs(_x, _y)

        for j in range(gh):
            for i in range(gw):
                if grid[j][i] == "1" and (i, j) not in visited:

                    r += 1
                    dfs(i, j)

        return r
