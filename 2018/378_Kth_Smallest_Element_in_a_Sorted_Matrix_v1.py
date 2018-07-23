#!/usr/bin/eni python
# encoding: utf-8


import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapq.heapify(heap)
        for i in range(k-1):
            val, row_index, col_index = heapq.heappop(heap)
            if col_index+1 < n:
                heapq.heappush(heap, (matrix[row_index][col_index+1], row_index, col_index+1))

        return heapq.heappop(heap)[0]


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
