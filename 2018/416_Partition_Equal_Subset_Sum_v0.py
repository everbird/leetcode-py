#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def canPartition(self, nums):
        s = sum(nums)
        if s % 2:
            return False

        target = s // 2
        return find_sum(nums, target)


def find_sum(nums, target):
    if not nums:
        return target == 0
    return find_sum(nums[:-1], target) or find_sum(nums[:-1], target - nums[-1])


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
