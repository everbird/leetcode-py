#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [None] * n
        r = 0
        dp[0] = 1
        for j in range(n):
            v = 1
            for i in range(j):
                if nums[i] < nums[j]:
                    v = max(v, dp[i]+1)
            dp[j] = v
            r = max(r, v)

        return r


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [10,9,2,5,3,7,101,18],
            4
        ),
        (
            [10,9,2,5,3,4],
            3
        ),
    ]
    f = s.lengthOfLIS
    for input_args, expected in tests:
        s.cache = {}

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
