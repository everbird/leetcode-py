#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):

    def maxSubArray(self, nums):
        len_n = len(nums)
        dp = [0] * len_n
        dp[0] = nums[0]
        for i in xrange(1, len_n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [-2,1,-3,4,-1,2,1,-5,4],
            6
        ),
    ]
    f = s.maxSubArray
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
