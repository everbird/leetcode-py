#!/usr/bin/eni python
# encoding: utf-8

from collections import defaultdict

class Solution(object):

    def bulbSwitch(self, n):
        d = defaultdict(int)
        for i in xrange(1, n+1):
            for j in xrange(i-1, n, i):
                d[j] += 1

        return sum(1 if x % 2 == 1 else 0 for x in d.values())


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            3,
            1
        ),
        (
            999999,
            -1
        )
    ]
    f = s.bulbSwitch
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
