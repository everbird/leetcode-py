#!/usr/bin/eni python
# encoding: utf-8

moves = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]

class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        r = []

        size = len(moves)
        move_index = 0
        steps = 0
        x, y = c0, r0
        n = 1
        while len(r) != R*C:
            if move_index % 2 == 0:
                steps += 1

            dx, dy = moves[move_index]
            for i in xrange(steps):
                if 0 <= x < C and 0 <= y < R:
                    r.append([y, x])
                    n += 1

                x += dx
                y += dy

            move_index = (move_index + 1) % size

        return r


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                1,
                4,
                0,
                0
            ),
            [[0, 0], [0, 1], [0, 2], [0, 3]]
        ),
        (
            (
                5,
                6,
                1,
                4
            ),
            [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
        ),
    ]
    f = s.spiralMatrixIII
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
