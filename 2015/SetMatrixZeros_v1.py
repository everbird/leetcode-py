#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        lenh = len(matrix)
        lenw = len(matrix[0])
        y = -1
        for j in range(lenh):
            if 0 in matrix[j]:
                y = j
                break

        x = -1
        for i in range(lenw):
            for j in range(lenh):
                if 0 == matrix[j][i]:
                    x = i
                    matrix[y][x] = 0

        if x == -1 or y == -1:
            return

        for j in range(lenh):
            if 0 in matrix[j]:
                matrix[j][x] = 0

        for j in range(lenh):
            for i in range(lenw):
                if j == y or i == x:
                    continue

                if matrix[j][x] == 0 or matrix[y][i] == 0:
                    matrix[j][i] = 0

        for j in range(lenh):
            matrix[j][x] = 0

        for i in range(lenw):
            matrix[y][i] = 0


if __name__ == '__main__':
    s = Solution()
    a = [
        [1, 0],
        [1, 1],
    ]
    s.setZeroes(a)
    print a
