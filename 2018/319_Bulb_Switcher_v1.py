#!/usr/bin/eni python
# encoding: utf-8

import math

class Solution(object):

    def bulbSwitch(self, n):
        return int(math.sqrt(n))


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            3,
            1
        ),
        (
            999999,
            999
        )
    ]
    f = s.bulbSwitch
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
