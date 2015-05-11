#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n = len(matrix)
        if n <= 1:
            return

        for j in range(n // 2):
            for i in range((n + 1) // 2):
                if n % 2 == 1:
                    if i == 0 and j == ((n - 1) // 2):
                        continue

                t = matrix[j][i]
                matrix[j][i] = matrix[n - i - 1][j]
                matrix[n - i - 1][j] = matrix[n - j - 1][n - i - 1]
                matrix[n - j - 1][n - i - 1] = matrix[i][n - j - 1]
                matrix[i][n - j - 1] = t


if __name__ == '__main__':
    s = Solution()
    a = [
            [1,0,1],
            [0,0,1],
            [1,0,1],
        ]
    s.rotate(a)
    print a

    a = [
        [1]
        ]
    s.rotate(a)
    print a

    a = [
        [1,2],
        [3,4],
        ]
    s.rotate(a)
    print a

    a = [
        [1,2,8],
        [3,4,9],
        [5,6,0],
        ]
    s.rotate(a)
    print a

    a = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
        ]
    s.rotate(a)
    print a

    a = [
        [1,2,3,4,5],
        [5,6,7,8,9],
        [9,10,11,12,13],
        [13,14,15,16,17],
        [13,14,15,16,17],
        ]
    s.rotate(a)
    print a

    a = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]
    ]
    s.rotate(a)
    print a
