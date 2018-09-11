#!/usr/bin/eni python
# encoding: utf-8

class Solution(object):
    def projectionArea(self, grid):
        N = len(grid)
        area = 0
        for j in xrange(N):
            max_v = 0
            for i in xrange(N):
                # x-y
                if grid[j][i]:
                    area += 1

                # x-z
                max_v = max(max_v, grid[i][j])
            area += max_v
            # y-z
            area += max(grid[j])

        return area


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [[2]],
            5
        ),
        (
            [[1,2],[3,4]],
            17
        ),
        (
            [[1,0],[0,2]],
            8
        ),
        (
            [[1,1,1],[1,0,1],[1,1,1]],
            14
        ),
        (
            [[2,2,2],[2,1,2],[2,2,2]],
            21
        ),
    ]
    f = s.projectionArea
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
