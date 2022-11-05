#!/usr/bin/eni python
# encoding: utf-8

import bisect
from collections import Counter


class Solution(object):

    def numFriendRequests(self, ages):
        ages.sort()
        c = Counter(ages)
        cnt = 0
        for i, age_a in enumerate(ages):
            if age_a <= 14:
                continue
            _age_b = 0.5 * age_a + 7
            ia = bisect.bisect_right(ages, age_a)
            ib = bisect.bisect_right(ages, _age_b)
            cnt += ia - ib - 1

        return cnt



if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [16, 16],
            2
        ),
        (
            [16, 17, 18],
            2
        ),
        (
            [20,30,100,110,120],
            3
        ),
        (
            [8,85,24,85,69],
            4
        ),
    ]
    f = s.numFriendRequests
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
