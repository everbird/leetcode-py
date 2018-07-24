#!/usr/bin/eni python
# encoding: utf-8

import math

class Solution(object):
    def isPowerOfThree(self, n):
        s = set([
            1,
            3,
            9,
            27,
            81,
            243,
            729,
            2187,
            6561,
            19683,
            59049,
            177147,
            531441,
            1594323,
            4782969,
            14348907,
            43046721,
            129140163,
            387420489,
            1162261467,
        ])
        return n in s


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            27,
            True
        ),
        (
            0,
            False
        ),
        (
            9,
            True
        ),
        (
            45,
            False
        )
    ]
    f = s.isPowerOfThree
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
