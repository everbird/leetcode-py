#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def nthUglyNumber(self, n):
        if n <= 0:
            return
        dp = [0] * n
        dp[0] = 1
        m2 = m3 = m5 = 0  # Step is always 1, but this is used to peek the target values in the future
        for i in range(1, n):
            min_v = min(dp[m2]*2, dp[m3]*3, dp[m5]*5)
            dp[i] = min_v
            if min_v == dp[m2]*2:
                m2 += 1
            if min_v == dp[m3]*3:
                m3 += 1
            if min_v == dp[m5]*5:
                m5 += 1

        return dp[n-1]


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            10,
            12
        ),
    ]
    f = s.nthUglyNumber
    for input_args, expected in tests:
        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
