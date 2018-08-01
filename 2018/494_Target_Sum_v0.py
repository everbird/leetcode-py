#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    cache = {}
    def findTargetSumWays(self, nums, S):
        self.cache = {}
        length = len(nums)

        def f(nums, n, S):
            if (n, S) in self.cache:
                return self.cache[(n, S)]
            if n == 0:
                return 1 if n == S else 0

            r = f(nums, n-1, S+nums[n-1]) + f(nums, n-1, S-nums[n-1])
            self.cache[(n, S)] = r
            return r

        return f(nums, length, S)


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
