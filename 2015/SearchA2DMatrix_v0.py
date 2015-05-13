#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        lenh = len(matrix)
        lenw = len(matrix[0])

        if lenh == 1:
            return target in matrix[0]

        if lenw == 1:
            return [target] in matrix

        b = 0
        e = lenh - 1
        while b <= e:
            mid = (b + e) // 2
            if target == matrix[mid][0]:
                return True

            elif target > matrix[mid][0]:
                if (mid+1) < lenh and target < matrix[mid+1][0]:
                    break

                b = mid + 1
            else:
                e = mid - 1

        n = mid
        t = matrix[n]
        b = 0
        e = lenw - 1
        while b <= e:
            mid = (b + e) // 2
            if target == t[mid]:
                return True
            elif target > t[mid]:
                b = mid + 1
            else:
                e = mid - 1

        return False


if __name__ == '__main__':
    s = Solution()
    print s.searchMatrix([
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 12)

    print s.searchMatrix([
        [1,1],
        [2,2]
    ], 3)

    print s.searchMatrix([
        [1,3,5,7],
        [10,11,16,20],
        [23,30,34,50]
    ], 10)
