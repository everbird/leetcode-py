#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def findDuplicate(self, nums):
        n = len(nums)
        lo = 0
        hi = n - 1
        while lo < hi:
            r, index = partition(nums, lo, hi)
            if r == -1:
                return nums[index]
            elif r == 0:
                hi = index - 1
            elif r == 1:
                lo = index + 1


def partition(nums, lo, hi):
    pivot_v = nums[hi]
    a = b = lo
    while a < hi:

        if nums[a] < pivot_v:
            nums[a], nums[b] = nums[b], nums[a]
            b += 1
        elif nums[a] == pivot_v:
            return (-1, hi)  # found
        a += 1

    nums[hi], nums[b] = nums[b], nums[hi]
    if nums[b] >= b+1:
        return (1, b)  # right
    else:
        return (0, b)  # left




if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [1,3,4,2,2],
            2
        ),
        (
            [3,1,3,4,2],
            3
        ),
        (
            [7,9,7,4,2,8,7,7,1,5],
            7
        )
    ]
    f = s.findDuplicate
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
