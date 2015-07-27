#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        lenh = len(matrix)
        for i in range(lenh):
            li = matrix[i]
            if li[0] <= target or li[-1] >= target:
                if self.binary_search(li, target):
                    return True

        return False

    def binary_search(self, array, target):
        b = 0
        e = len(array) - 1
        while b <= e:
            mid = (b+e) // 2
            n = array[mid]
            if n == target:
                return True
            elif n > target:
                e = mid - 1
            else:
                b = mid + 1

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
