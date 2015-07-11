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
        r = []
        x, y = -1, 0
        direction = 0
        while lenh > 0 and lenw > 0:
            moves = lenh if direction % 2 else lenw
            for i in range(moves):
                if direction == 0:
                    x += 1
                elif direction == 1:
                    y += 1
                elif direction == 2:
                    x -= 1
                else:
                    y -= 1

                r.append(matrix[y][x])

            if direction % 2:
                lenw -= 1
            else:
                lenh -= 1

            direction = (direction + 1) % 4

        return r


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
