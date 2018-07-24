#!/usr/bin/eni python
# encoding: utf-8

import math

class Solution(object):
    def isPowerOfThree(self, n):
        x = 3**19
        return n > 0 and (x % n) == 0



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
