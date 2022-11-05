#!/usr/bin/eni python
# encoding: utf-8

import bisect
from collections import Counter


class Solution(object):

    def numFriendRequests(self, ages):
        N = 120
        c = Counter(ages)
        cnt = 0
        for age_a in range(1, N+1):
            if age_a <= 14 or c[age_a] == 0:
                continue

            for age_b in range(15, N+1):
                if age_b <= (0.5 * age_a + 7) or c[age_b] == 0 or age_b > age_a:
                    continue

                if age_b == age_a:
                    cnt += c[age_a] * (c[age_a] - 1)
                else:
                    cnt += c[age_a] * c[age_b]

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
