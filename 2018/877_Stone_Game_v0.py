#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def stoneGame(self, p):
        n = len(p)
        dp = [[0] * n for i in range(n)]
        for i in range(n): dp[i][i] = p[i]
        for d in range(1, n):
            for i in range(n - d):
                dp[i][i + d] = max(p[i] - dp[i + 1][i + d], p[i + d] - dp[i][i + d - 1])
        print '>>>', dp
        return dp[0][-1] > 0


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [5,3,4,5],
            True
        ),
    ]
    f = s.stoneGame
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
