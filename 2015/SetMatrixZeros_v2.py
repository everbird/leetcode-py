#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        lenh = len(matrix)
        lenw = len(matrix[0])
        for j in range(lenh):
            for i in range(lenw):
                if matrix[j][i] == 0:
                    matrix[j][i] = None

        for j in range(lenh):
            for i in range(lenw):
                if matrix[j][i] is None:
                    self.set_empty(matrix, i, j)

        for j in range(lenh):
            for i in range(lenw):
                if matrix[j][i] is None:
                    matrix[j][i] = 0

    def set_empty(self, matrix, x, y):
        lenh = len(matrix)
        lenw = len(matrix[0])
        for j in range(lenh):
            if matrix[j][x] is not None:
                matrix[j][x] = 0

        for i in range(lenw):
            if matrix[y][i] is not None:
                matrix[y][i] = 0


if __name__ == '__main__':
    s = Solution()
    a = [
        [1, 0],
        [1, 1],
    ]
    a = [
        [0,0,0,5],
        [4,3,1,4],
        [0,1,1,4],
        [1,2,1,3],
        [0,0,1,1]
    ]
    s.setZeroes(a)
    print a
