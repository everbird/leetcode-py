#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        n = len(nums)
        s = 0
        nums.sort()
        for i in xrange(n):
            s += nums[i]
            if s == target:
                return True
            elif s > target:
                return False

        return False


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [1, 5, 11, 5],
            True
        ),
        (
            [1, 2, 3, 5],
            False
        )
    ]
    f = s.canPartition
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
