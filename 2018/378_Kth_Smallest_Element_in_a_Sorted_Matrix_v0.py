#!/usr/bin/eni python
# encoding: utf-8


from collections import defaultdict


class Solution(object):
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        lo = matrix[0][0]
        hi = matrix[n-1][n-1] + 1
        while lo < hi:
            mid = (lo + hi) // 2
            cnt = 0
            for row in matrix:
                cnt += binary_search(row, mid)
            if cnt >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo


def binary_search(array, target):
    lo = 0
    hi = len(array)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if array[mid] <= target:
            lo = mid + 1
        else:
            hi = mid

    return lo






if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                [
                    [ 1,  5,  9],
                    [10, 11, 13],
                    [12, 13, 15]
                ],
                8
            ),
            13
        ),
    ]
    f = s.kthSmallest
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
