#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        lenw = len(matrix[0])
        lenh = len(matrix)
        x = 0
        y = lenh - 1
        while x < lenw and y >= 0:
            if matrix[y][x] == target:
                return True
            if matrix[y][x] < target:
                x += 1
            else:
                y -= 1

        return False


if __name__ == '__main__':
    s = Solution()
    m = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    print s.searchMatrix(m, 5)
    print s.searchMatrix(m, 20)
    print '-'*6

    m = [
        [1, 3, 5],
    ]
    print s.searchMatrix(m, 3)
    print '-'*6

    m = [
        [1, 4],
        [2, 5]
    ]
    print s.searchMatrix(m, 2)

    print '-'*6
    print s.searchMatrix([
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ], 19)
