#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):

    # TLE
    def jump(self, nums):
        len_n = len(nums)
        current = len_n - 1
        count = 0
        while current > 0:
            min_i = current
            for i in xrange(current-1, -1, -1):
                if nums[i] >= (current - i):
                    min_i = min(min_i, i)

            current = min_i

            count += 1

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
