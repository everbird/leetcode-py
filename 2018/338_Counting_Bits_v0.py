#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def countBits(self, num):
        dp = [0] * (num+1)
        if num == 0:
            return dp

        dp[1] = 1
        for i in range(2, num+1):
            _i = find(i)
            dp[i] += dp[_i] + 1

        return dp


def find(n):
    v = 1
    while v <= n:
        v = v << 1

    return n - (v>>1)




if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            5,
            [0,1,1,2,1,2]
        ),
        (
            0,
            [0]
        ),
    ]
    f = s.countBits
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
