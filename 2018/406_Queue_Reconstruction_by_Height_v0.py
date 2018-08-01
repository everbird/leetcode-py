#!/usr/bin/eni python
# encoding: utf-8


import bisect
import random
from collections import defaultdict


class Solution(object):
    def reconstructQueue(self, people):
        heights = [x[0] for x in people]
        _heights = requeue(heights)
        return view(_heights)


def view(heights):
    r = []
    a = []
    for h in heights:
        n = len(a)
        i = bisect.bisect_left(a, h)
        bisect.insort_left(a, h)
        r.append([h, n-i])

    return r


def requeue(heights):
    c = n = len(heights)
    target = []
    while c > 0:
        x = heights.pop(random.randint(0, c-1))
        target.append(x)
        c -= 1

    return target


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]],
            [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
        ),
    ]
    f = s.reconstructQueue
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
