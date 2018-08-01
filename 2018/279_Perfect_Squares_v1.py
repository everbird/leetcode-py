#!/usr/bin/eni python
# encoding: utf-8


import math


class Solution(object):
    def numSquares(self, n):
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            m = int(math.sqrt(i))
            for x in range(1, m+1):
                if i >= x*x:
                    dp[i] = min(dp[i], dp[i-x*x]+1)

        return dp[n]


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
            3
        )
    ]
    f = s.numSquares
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
