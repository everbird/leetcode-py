#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def minCostClimbingStairs(self, cost):
        if not cost:
            return 0

        len_n = len(cost)
        if len_n == 1:
            return cost[0]

        dp = [0] * (len_n + 1)
        for i in range(2, len_n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

        return dp[len_n]


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [10, 15, 20],
            15
        ),
        (
            [1, 100, 1, 1, 1, 100, 1, 1, 100, 1],
            6
        ),
    ]
    for input_args, expected in tests:
        r = s.minCostClimbingStairs(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
