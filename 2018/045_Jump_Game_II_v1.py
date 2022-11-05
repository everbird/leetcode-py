#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):

    def jump(self, nums):
        len_n = len(nums)
        count = 0
        last = 0
        max_i = 0
        for i in xrange(len_n-1):
            max_i = max(max_i, i+nums[i])
            if i == last:
                count += 1
                last = max_i

        return count


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [2,3,1,1,4],
            2
        ),
    ]
    f = s.jump
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
