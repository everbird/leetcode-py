#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        lenh = len(matrix)
        lenw = len(matrix[0])
        if lenh <= 1:
            return

        for j in range(lenh // 2):
            for i in range((lenh + 1) // 2):
                if lenh % 2 == 1:
                    if i == 0 and j == ((lenh + 1) // 2 - 1):
                        continue

                t = matrix[j][i]
                matrix[j][i] = matrix[lenh - i - 1][j]
                matrix[lenh - i - 1][j] = matrix[lenh - j - 1][lenw - i - 1]
                matrix[lenh - j - 1][lenw - i - 1] = matrix[i][lenh - j - 1]
                matrix[i][lenh - j - 1] = t


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
