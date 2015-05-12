#!/usr/bin/env python
# encoding: utf-8

import copy


class Solution:
    # @return a list of lists of string
    r = []
    count = 0

    def solveNQueens(self, n):
        r = []
        li = ['.'] * n
        for i in range(n):
            r.append(li[:])

        self.solve(r, n)
        return self.r

    def solve(self, r, n):
        for i in range(n):
            for j in range(n):
                if self.is_valid(r, n, i, j):
                    r[j][i] = 'Q'
                    self.count += 1

                    if self.count == n:
                        if (all(['Q' in r[k] for k in range(n)])
                                and r not in self.r):
                            self.r.append(copy.deepcopy(r))
                    else:
                        self.solve(r, n)

                    r[j][i] = '.'
                    self.count -= 1

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
                    or (x - i >= 0 and y - i < n and r[y - i][x - i] == 'Q')):
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    print s.solveNQueens(4)

    a = [
        ['.', '.', 'Q', '.'],
        ['Q', '.', '.', '.'],
        ['.', '.', '.', 'Q'],
        ['.', 'Q', '.', '.']
    ]

    a = [
        ['.', '.', 'Q', '.'],
        ['Q', '.', '.', '.'],
        ['.', '.', '.', 'Q'],
        ['.', 'Q', '.', '.']
    ]

    a = [
        ['.', '.', 'Q', '.'],
        ['Q', '.', '.', '.'],
        ['.', '.', '.', 'Q'],
        ['.', 'Q', '.', '.']
    ]
