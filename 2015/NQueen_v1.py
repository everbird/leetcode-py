#!/usr/bin/env python
# encoding: utf-8

import copy


class Solution:
    # @return a list of lists of string
    r = []

    def solveNQueens(self, n):
        r = []
        li = ['.'] * n
        for i in range(n):
            r.append(li[:])

        self.solve(r, 0, n)
        return self.r

    def solve(self, r, row, n):
        if row == n:
            if r not in self.r:
                self.r.append(copy.deepcopy(r))
                return

        for j in range(n):
            if self.is_valid(r, n, row, j):
                r[j][row] = 'Q'
                #printr(r)
                self.solve(r, row+1, n)
                r[j][row] = '.'

    def is_valid(self, r, n, x, y):
        for i in range(n):
            if r[i][x] == 'Q':
                return False

        for i in range(n):
            if r[y][i] == 'Q':
                return False

        for i in range(n):
            if ((x + i < n and y + i < n and r[y + i][x + i] == 'Q')
                    or (x + i < n and y - i >= 0 and r[y - i][x + i] == 'Q')
                    or (x - i >= 0 and y + i < n and r[y + i][x - i] == 'Q')
                    or (x - i >= 0 and y - i >= 0 and r[y - i][x - i] == 'Q')):
                return False

        return True


def printr(r):
    for i in r:
        print i

    print '-' * 6


if __name__ == '__main__':
    s = Solution()
    print s.solveNQueens(7)
