#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def findTargetSumWays(self, nums, S):
        n = len(nums)
        dp = [[0] * (2*1000+1) for i in range(n)]
        def reindex(index):
            return index + 1000
        dp[0][reindex(nums[0])] = 1
        dp[0][reindex(-nums[0])] += 1
        for i in range(1, n):
            for j in range(-1000, 1000+1):
                if -1000 <= j+nums[i] <= 1000 and dp[i-1][reindex(j+nums[i])] != 0:
                    dp[i][reindex(j)] += dp[i-1][reindex(j+nums[i])]

                if -1000 <= j-nums[i] <= 1000 and dp[i-1][reindex(j-nums[i])]:
                    dp[i][reindex(j)] += dp[i-1][reindex(j-nums[i])]

        return dp[n-1][reindex(S)] if S <= 1000 else 0



if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                [1, 1, 1, 1, 1],
                3
            ),
            5
        ),
    ]
    f = s.findTargetSumWays
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
