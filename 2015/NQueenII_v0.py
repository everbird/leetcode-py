#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} n
    # @return {integer}
    count = 0

    def totalNQueens(self, n):
        li = ['.'] * n
        r = [li[:] for i in range(n)]
        self.place_queen(r, 0, n)
        return self.count

    def place_queen(self, r, row, n):
        if n == row:
            self.count += 1
            return

        for i in range(n):
            if self.is_valid(r, n, row, i):
                r[i][row] = 'Q'
                #printr(r)
                self.place_queen(r, row+1, n)
                r[i][row] = '.'

    def is_valid(self, r, n, x, y):
        for i in range(n):
            if r[y][i] == 'Q':
                return False

        for i in range(n):
            if r[i][x] == 'Q':
                return False

        for i in range(n):
            if ((x + i < n and y + i < n and r[y + i][x + i] == 'Q')
                    or (x + i < n and y - i >= 0 and r[y - i][x + i] == 'Q')
                    or (x - i >= 0 and y + i < n and r[y + i][x - i] == 'Q')
                    or (x - i >= 0 and y - i >= 0 and r[y - i][x - i] == 'Q')):
                return False

        return True

def printr(r):
    for li in r:
        print li

    print '-' * 6


if __name__ == '__main__':
    s = Solution()
    for i in range(4, 10):
        print s.totalNQueens(i)
