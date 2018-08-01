#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        a = 0
        while a < n:
            while a < n and nums[a] != 0:
                a += 1
            b = a + 1
            while b < n and nums[b] == 0:
                b += 1

            if a <  b < n and nums[a] == 0 and nums[b] != 0:
                nums[a], nums[b] = nums[b], nums[a]

            a += 1


    def moveZeroesX(self, nums):
        n = len(nums)
        lo = 0
        hi = n - 1
        while lo < hi:
            if nums[lo] != 0:
                lo += 1
                continue
            elif nums[hi] == 0:
                hi -= 1
                continue
            else:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [0,1,0,3,12],
            [1,3,12,0,0]
        ),
    ]
    f = s.moveZeroes
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        r = input_args
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
