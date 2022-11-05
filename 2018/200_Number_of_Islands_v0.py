#!/usr/bin/eni python
# encoding: utf-8


from collections import defaultdict

moves = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

class Solution(object):

    def numIslands(self, grid):
        f = {}
        u = defaultdict(set)
        if not grid:
            return 0

        len_y = len(grid)
        len_x = len(grid[0])

        for j in xrange(len_y):
            for i in xrange(len_x):
                if grid[j][i] == '1':
                    f[(i, j)] = (i, j)
                    u[(i, j)].add((i, j))

        for j in xrange(len_y):
            for i in xrange(len_x):
                if grid[j][i] == '1':
                    for dx, dy in moves:
                        _i = i+dx
                        _j = j+dy
                        if (
                            0 <= _i < len_x
                            and 0 <= _j < len_y
                            and grid[_j][_i] == '1'
                            and f[(_i, _j)] != f[(i, j)]
                        ):
                            tx, ty = f[(_i, _j)]
                            for fx, fy in u[(tx, ty)]:
                                f[(fx, fy)] = f[(i, j)]

                            u[f[(i, j)]] |= u[(tx, ty)]
                            del u[(tx, ty)]

        return len(u)



if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [
                ['1','1','1','1','0'],
                ['1','1','0','1','0'],
                ['1','1','0','0','0'],
                ['0','0','0','0','0'],
            ],
            1
        ),
        (
            [
                ['1','1','0','0','0'],
                ['1','1','0','0','0'],
                ['0','0','1','0','0'],
                ['0','0','0','1','1'],
            ],
            3
        ),
    ]
    f = s.numIslands
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
