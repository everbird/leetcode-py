#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def findTargetSumWays(self, nums, S):
        n = len(nums)
        dp = [[0] * (2*1000+1) for i in range(n)]
        def reindex(index):
            print index, '<<<'
            return index + 1000
        dp[0][reindex(nums[0])] = 1
        dp[0][reindex(-nums[0])] += 1
        for i in range(1, n):
            for j in range(-1000, 1000+1):
            #     dp[i][reindex(j)] = dp[i-1][reindex(j+nums[i])] + dp[i-1][reindex(j-nums[i])]
                x = dp[i-1][reindex(j)]
                if x != 0:
                    dp[i][reindex(j+nums[i])] += x
                    dp[i][reindex(j-nums[i])] += x

        return dp[n-1][reindex(S)]



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
