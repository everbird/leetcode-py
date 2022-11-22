#!/usr/bin/env python3

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # 1. find lands
        # 2. flood to mark water with distance BFS
        n = len(grid)
        d = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
        ]
        q = []
        for j in range(n):
            for i in range(n):
                if grid[j][i] == 1:
                    q.append((j, i, 0))

        maxd = -1
        while q:
            y, x, dis = q.pop(0)
            for dy, dx in d:
                _y = y + dy
                _x = x + dx
                if 0 <= _x < n and 0 <= _y < n and grid[_y][_x] == 0:
                    maxd = max(maxd, dis+1)
                    grid[_y][_x] = dis+1
                    q.append((_y, _x, dis+1))

        return maxd
