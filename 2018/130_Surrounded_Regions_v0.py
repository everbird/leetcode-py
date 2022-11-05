#!/usr/bin/eni python
# encoding: utf-8

from collections import defaultdict

neighbors = [
    (1, 0),
    (0, 1),
    (-1,  0),
    (0, -1),
]


class Solution(object):

    def solve(self, board):
        roots = {}
        groups = defaultdict(set)
        if not board:
            return

        len_y = len(board)
        len_x = len(board[0])

        for j in xrange(len_y):
            for i in xrange(len_x):
                if board[j][i] == 'O':
                    roots[(i, j)] = (i, j)
                    groups[(i, j)].add((i, j))

        for j in xrange(len_y):
            for i in xrange(len_x):
                if board[j][i] == 'O':
                    for dx, dy in neighbors:
                        _j = j+dy
                        _i = i+dx
                        if (
                            0 <= _i < len_x
                            and 0 <= _j < len_y
                            and board[_j][_i]=='O'
                            and roots[(_i, _j)] !=  roots[(i, j)]
                        ):
                            _ti, _tj = roots[(_i, _j)]
                            for xi, xj in groups[roots[(_i, _j)]]:
                                roots[(xi, xj)] = roots[(i, j)]

                            groups[roots[(i, j)]] |= groups[(_ti, _tj)]
                            del groups[(_ti, _tj)]

        for (hx, hy), nodes in groups.iteritems():
            if any(nx==0 or ny==0 or nx==(len_x-1) or ny==(len_y-1) for (nx, ny) in nodes):
                continue

            for node in nodes:
                x, y = node
                board[y][x] = 'X'


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [
                ['X', 'X', 'X', 'X'],
                ['X', 'O', 'O', 'X'],
                ['X', 'X', 'O', 'X'],
                ['X', 'O', 'X', 'X'],
            ],
            [
                ['X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X'],
                ['X', 'O', 'X', 'X'],
            ],
        ),
        (
            [],
            []
        ),
        (
            [
                ["X","X","X","X","O","O","X","X","O"],
                ["O","O","O","O","X","X","O","O","X"],
                ["X","O","X","O","O","X","X","O","X"],
                ["O","O","X","X","X","O","O","O","O"],
                ["X","O","O","X","X","X","X","X","O"],
                ["O","O","X","O","X","O","X","O","X"],
                ["O","O","O","X","X","O","X","O","X"],
                ["O","O","O","X","O","O","O","X","O"],
                ["O","X","O","O","O","X","O","X","O"]
            ],
            [
                ["X","X","X","X","O","O","X","X","O"],
                ["O","O","O","O","X","X","O","O","X"],
                ["X","O","X","O","O","X","X","O","X"],
                ["O","O","X","X","X","O","O","O","O"],
                ["X","O","O","X","X","X","X","X","O"],
                ["O","O","X","X","X","O","X","X","X"],
                ["O","O","O","X","X","O","X","X","X"],
                ["O","O","O","X","O","O","O","X","O"],
                ["O","X","O","O","O","X","O","X","O"]
            ]
            # [
            #     ["X","X","X","X","O","O","X","X","O"],
            #     ["O","O","O","O","X","X","O","O","X"],
            #     ["X","O","X","O","O","X","X","O","X"],
            #     ["O","O","X","X","X","X","X","O","O"],
            #     ["X","O","O","X","X","X","X","X","O"],
            #     ["O","O","X","X","X","O","X","X","X"],
            #     ["O","O","O","X","X","O","X","X","X"],
            #     ["O","O","O","X","O","O","O","X","O"],
            #     ["O","X","O","O","O","X","O","X","O"]
            # ]
        ),
    ]
    f = s.solve
    for input_args, expected in tests:
        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)

        r = input_args
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
