#!/usr/bin/eni python
# encoding: utf-8

import heapq


class Solution(object):
    def findKthNumber(self, n, k):
        heap = []
        for i in range(1, n+1):
            heapq.heappush(heap, (str(i), i))

        for i in range(k-1):
            heapq.heappop(heap)

        return heapq.heappop(heap)[1]


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                13,
                2
            ),
            10
        ),
    ]
    f = s.findKthNumber
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
