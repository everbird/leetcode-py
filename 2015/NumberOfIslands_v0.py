#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        if not grid:
            return 0

        lenh = len(grid)
        lenw = len(grid[0])

        cnt = 0

        def fill(j, i):
            grid[j][i] = 'F'

            if j-1 >= 0 and grid[j-1][i] == '1':
                fill(j-1, i)

            if j+1 < lenh and grid[j+1][i] == '1':
                fill(j+1, i)

            if i-1 >= 0 and grid[j][i-1] == '1':
                fill(j, i-1)

            if i+1 < lenw and grid[j][i+1] == '1':
                fill(j, i+1)

        for j in range(lenh):
            for i in range(lenw):
                c = grid[j][i]
                if c == '0':
                    continue

                if c == '1':
                    cnt += 1
                    fill(j, i)

        return cnt




if __name__ == '__main__':
    s = Solution()
    g = [
        list('11110'),
        list('11010'),
        list('11000'),
        list('00000'),
    ]
    print s.numIslands(g)

    g = [
        list('11000'),
        list('11000'),
        list('00100'),
        list('00011'),
    ]
    print s.numIslands(g)

    g = [
        list('1'),
    ]
    print s.numIslands(g)
