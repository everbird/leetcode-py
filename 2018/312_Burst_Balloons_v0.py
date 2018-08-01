#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def maxCoins(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]

        max_v = 0
        for i in range(n):
            left = nums[i-1] if i > 0 else 1
            right = nums[i+1] if i < n-1 else 1
            v = left*nums[i]*right + self.maxCoins(nums[:i] + nums[i+1:])
            max_v = max(max_v, v)
        return max_v


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [3,1,5,8],
            167
        ),
    ]
    f = s.maxCoins
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
