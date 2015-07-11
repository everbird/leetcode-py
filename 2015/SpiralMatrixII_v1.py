#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        if not n:
            return []

        li = [0] * n
        m = [li[:] for i in range(n)]
        height = n
        width = n
        x, y = -1, 0
        direction = 0
        v = 1
        while width and height:
            moves = height if direction % 2 else width
            for i in range(moves):
                if direction == 0:
                    x += 1
                elif direction == 1:
                    y += 1
                elif direction == 2:
                    x -= 1
                else:
                    y -= 1
                m[y][x] = v
                v += 1

            if direction % 2:
                width -= 1
            else:
                height -= 1

            direction = (direction + 1) % 4

        return m


if __name__ == '__main__':
    s = Solution()
    print s.generateMatrix(3)
