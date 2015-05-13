#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        r = []
        lenh = len(matrix)
        lenw = len(matrix[0])
        for j in range(lenh):
            for i in range(lenw):
                if matrix[j][i] == 0:
                    r.append((j, i))

        for y, x in r:
            for i in range(lenw):
                matrix[y][i] = 0

            for j in range(lenh):
                matrix[j][x] = 0


if __name__ == '__main__':
    s = Solution()
    a = [
        [1, 0],
        [1, 1],
    ]
    s.setZeroes(a)
    print a
