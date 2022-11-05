#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):

    def fourSum(self, nums, target):
        nums.sort()
        return kSum(4, nums, target)


def kSum(k, nums, target):
    rs = []
    if k == 2:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            _sum = nums[lo] + nums[hi]
            if _sum == target:
                rs.append([nums[lo], nums[hi]])
                while lo < hi and nums[lo] == nums[lo+1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi-1]:
                    hi -= 1
                lo += 1
                hi -= 1
            elif _sum > target:
                hi -= 1
            else:
                lo += 1

    else:
        pre = None
        for i, n in enumerate(nums[:-(k-1)]):
            if pre == n:
                continue

            r = kSum(k-1, nums[i+1:], target - n)
            for _r in r:
                rs.append([n] + _r)
            pre = n
    return rs


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                [1, 0, -1, 0, -2, 2],
                0
            ),
            [
                [-1,  0, 0, 1],
                [-2, -1, 1, 2],
                [-2,  0, 0, 2]
            ]
        ),
    ]
    f = s.fourSum
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
