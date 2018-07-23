#!/usr/bin/eni python
# encoding: utf-8
from collections import Counter
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        c = Counter(nums)
        heap = [(-cnt, key) for key, cnt in c.iteritems()]
        heapq.heapify(heap)
        r = []
        for i in range(k):
            _, key = heapq.heappop(heap)
            r.append(key)

        return r


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                [1,1,1,2,2,3],
                2
            ),
            [1, 2]
        ),
        (
            (
                [5,3,1,1,1,3,73,1],
                1
            ),
            [1]
        ),
        (
            (
                [4,1,-1,2,-1,2,3],
                2
            ),
            [-1, 2]
        )
    ]
    f = s.topKFrequent
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
