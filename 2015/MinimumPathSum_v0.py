#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        if m == 1 and n == 1:
            return grid[0][0]

        li = [0] * n
        d = [li[:] for i in range(m)]
        d[0][0] = grid[0][0]
        for i in range(1, n):
            d[0][i] = d[0][i - 1] + grid[0][i]

        for i in range(1, m):
            d[i][0] = d[i - 1][0] + grid[i][0]

        for mi in range(1, m):
            for ni in range(1, n):
                d[mi][ni] = min(d[mi - 1][ni], d[mi][ni - 1]) + grid[mi][ni]

        return d[m - 1][n - 1]



if __name__ == '__main__':
    s = Solution()
    print s.minPathSum([
        [1,2,3],
        [-9,6,4],
        [0,7,5],
    ])
