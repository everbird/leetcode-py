#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        li = [0] * n
        d = [li[:] for i in range(m)]

        for i in range(m):
            d[i][0] = 1

        for i in range(n):
            d[0][i] = 1

        for mi in range(1, m):
            for ni in range(1, n):
                d[mi][ni] = d[mi - 1][ni] + d[mi][ni - 1]

        return d[m - 1][n - 1]


if __name__ == '__main__':
    s = Solution()
    print s.uniquePaths(3, 7)
