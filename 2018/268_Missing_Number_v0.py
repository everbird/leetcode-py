#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def missingNumber(self, nums):
        n = len(nums) + 1
        return (n-1) * n // 2 - sum(nums)


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [3,0,1],
            2
        ),
        (
            [9,6,4,2,3,5,7,0,1],
            8
        ),
    ]
    f = s.missingNumber
    for input_args, expected in tests:
        s.cache = {}

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
