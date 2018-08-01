#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def gameOfLife(self, board):
        if not board:
            return
        len_y = len(board)
        len_x = len(board[0])
        marks = [[0 for i in range(len_x)] for j in range(len_y)]
        for j in range(len_y):
            for i in range(len_x):
                val = check(board, i, j, len_x, len_y)
                marks[j][i] = val

        for j in range(len_y):
            for i in range(len_x):
                v = marks[j][i]
                if v in (0, 1, 3):
                    board[j][i] = 0
                elif v in (2, 4):
                    board[j][i] = 1


def check(board, x, y, len_x, len_y):
    dy = [-1, 0, 1]
    dx = [-1, 0, 1]
    cnt = 0
    for _y in dy:
        for _x in dx:
            if (_x == 0 and _y == 0) or ((x+_x) >= len_x) or ((y+_y) >= len_y) or ((y+_y) < 0) or ((x+_x) < 0):
                continue

            if board[y+_y][x+_x] == 1:
                cnt += 1

    if board[y][x] == 1:
        if cnt < 2:
            return 1
        elif 2 <= cnt <= 3:
            return 2
        else:
            return 3
    else:
        return 4 if cnt == 3 else 0


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [
                [0,1,0],
                [0,0,1],
                [1,1,1],
                [0,0,0]
            ],
            [
                [0,0,0],
                [1,0,1],
                [0,1,1],
                [0,1,0]
            ]
        ),
    ]
    f = s.gameOfLife
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        r = input_args
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
