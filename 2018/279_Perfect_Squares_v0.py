#!/usr/bin/eni python
# encoding: utf-8


import math


class Solution(object):
    cache = {}
    def numSquares(self, n):
        self.cache = {}
        return self.dp(n)

    def dp(self, n):
        if n == 0:
            return 0

        if n in self.cache:
            return self.cache[n]

        m = int(math.sqrt(n))
        r = float('inf')
        for x in range(m, 0, -1):
            if n >= x*x:
                cnt = self.dp(n - x*x)
                r = min(r, cnt+1)
        self.cache[n] = r
        return r


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            12,
            3
        ),
        (
            13,
            2
        ),
        (
            43,
            3
        ),
        (
            3288,
            -1
        )
    ]
    f = s.numSquares
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
