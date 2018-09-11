#!/usr/bin/eni python
# encoding: utf-8

class Solution(object):
    def surfaceArea(self, grid):
        area = 0
        N = len(grid)
        for j in xrange(N):
            for i in xrange(N):
                if grid[j][i] > 0:
                    area += grid[j][i] * 4 + 2

        for j in xrange(N):
            for i in xrange(N-1):
                area -= min(grid[j][i], grid[j][i+1]) * 2

        for j in xrange(N-1):
            for i in xrange(N):
                area -= min(grid[j][i], grid[j+1][i]) * 2

        return area


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [[2]],
            10
        ),
        (
            [[1,2],[3,4]],
            34
        ),
        (
            [[1,0],[0,2]],
            16
        ),
        (
            [[1,1,1],[1,0,1],[1,1,1]],
            32
        ),
        (
            [[2,2,2],[2,1,2],[2,2,2]],
            46
        ),
    ]
    f = s.surfaceArea
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
