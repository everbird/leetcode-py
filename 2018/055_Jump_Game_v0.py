#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):

    def canJump(self, nums):
        max_i = 0
        len_n = len(nums)
        for i in xrange(len_n):
            if max_i < i:
                return False

            max_i = max(max_i, i+nums[i])

            if max_i >= (len_n-1):
                return True

        return True



if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [2,3,1,1,4],
            True
        ),
        (
            [3,2,1,0,4],
            False
        ),
    ]
    f = s.canJump
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
