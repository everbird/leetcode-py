#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} n
    # @return {integer}
    count = 0

    def totalNQueens(self, n):
        r = [-1] * n
        self.place_queen(r, 0, n)
        return self.count

    def place_queen(self, r, row, n):
        if n == row:
            self.count += 1
            return

        for i in range(n):
            if self.is_valid(r, n, row, i):
                r[row] = i
                self.place_queen(r, row+1, n)
                r[row] = -1

    def is_valid(self, r, n, x, y):
        for i in range(n):
            if r[i] == y or (r[i] != -1 and abs(x - i) == abs(r[i] - y)):
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    for i in range(4,10):
        print s.totalNQueens(i)
