#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if not matrix:
            return []

        lenh = len(matrix)
        lenw = len(matrix[0])
        top = 0
        left = -1
        right = lenw - 1
        bottom = lenh - 1
        x, y = 0, 0
        d = 0
        r = [matrix[y][x]]
        while top >= bottom or right >= left:

            if d % 4 == 0 and x == right and y == top:
                left += 1
                d += 1
            elif d % 4 == 1 and x == right and y == bottom:
                top += 1
                d += 1
            elif d % 4 == 2 and x == left and y == bottom:
                right -= 1
                d += 1
            elif d % 4 == 3 and x == left and y == top:
                bottom -= 1
                d += 1

            if top == bottom and right == left:
                break

            _x = x
            _y = y
            x, y = self.get_next(matrix, x, y, d)
            if not left <= x <= right or not top <= y <= bottom:
                break

            if _x != x or _y != y:
                r.append(matrix[y][x])

        return r

    def get_next(self, matrix, x, y, d):
        lenh = len(matrix)
        lenw = len(matrix[0])

        if d % 4 == 0:
            return min(x+1, lenw - 1), y
        elif d % 4 == 1:
            return x, min(y+1, lenh - 1)
        elif d % 4 == 2:
            return max(x - 1, 0), y
        else:
            return x, max(y - 1, 0)


if __name__ == '__main__':
    s = Solution()
    print s.spiralOrder(
        [
            [ 1, 2, 3 ],
            [ 4, 5, 6 ],
            [ 7, 8, 9 ]
        ]
    )

    print s.spiralOrder(
        [
            [ 2, 3 ],
        ]
    )

    print s.spiralOrder(
        [
            [3],
            [2]
        ]
    )
