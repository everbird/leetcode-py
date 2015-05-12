#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        li = [0] * n
        r = [li[:] for i in range(n)]
        self.fill(r, n)
        return r

    def fill(self, r, n):
        left = -1
        top = 0
        right = n - 1
        bottom = n - 1
        x, y = 0, 0
        d = 0
        num = 1
        while num <= n*n:
            r[y][x] = num

            if left > right and top > bottom:
                break

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

            x, y = self.get_next(n, x, y, d)
            num += 1

    def get_next(self, n, x, y, d):
        if d % 4 == 0:
            return min(x+1, n-1), y
        elif d % 4 == 1:
            return x, min(y+1, n-1)
        elif d % 4 == 2:
            return max(x-1, 0), y
        elif d % 4 == 3:
            return x, max(y-1, 0)


if __name__ == '__main__':
    s = Solution()
    print s.generateMatrix(3)
