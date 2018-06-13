#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def numMagicSquaresInside(self, grid):
        if not grid:
            return 0

        len_y = len(grid)
        len_x = len(grid[0])
        if len_y < 3 or len_x < 3:
            return 0

        cnt = 0
        for i in range(len_y - 2):
            for j in range(len_x - 2):
                if is_magic_square(j, i, grid):
                    cnt += 1
        return cnt


def is_magic_square(x, y, grid):
    for i in range(3):
        # Rows
        if sum(grid[y+i][x:x+3]) != 15:
            return False

        # Columns
        column_sum = 0
        for j in range(3):
            if not 1 <= grid[y+j][x+i] <= 9:
                return False
            column_sum += grid[y+j][x+i]

        if column_sum != 15:
            return False

    # Diagonals
    a = b = 0
    for i in range(3):
        a += grid[y+i][x+i]
        b += grid[y+2-i][x+i]

    if a != 15 or b != 15:
        return False

    return True


def main():
    s = Solution()
    tests = [
        (
            [
                [4,3,8,4],
                [9,5,1,9],
                [2,7,6,2]
            ],
            1
        ),
    ]
    for input_args, expected in tests:
        r = s.numMagicSquaresInside(input_args)
        print 'Input:{}\tOutput:{}\tExpected:{}'.format(input_args, r, expected)

    m1 = [
        [4,3,8],
        [9,5,1],
        [2,7,6]
    ]
    print is_magic_square(0, 0, m1)
    m2 = [
        [1,8,6],
        [10,5,0],
        [4,2,9]
    ]
    print is_magic_square(0, 0, m2)

if __name__ == '__main__':
    main()
