#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    cache = {}
    def maxCoins(self, nums):
        self.cache = {}
        return self._max_coins(nums)

    def _max_coins(self, nums):
        if tuple(nums) in self.cache:
            return self.cache[tuple(nums)]

        n = len(nums)
        if n == 1:
            return nums[0]

        max_v = 0
        for i in range(n):
            left = nums[i-1] if i > 0 else 1
            right = nums[i+1] if i < n-1 else 1
            v = left*nums[i]*right + self._max_coins(nums[:i] + nums[i+1:])
            max_v = max(max_v, v)

        self.cache[tuple(nums)] = max_v
        return max_v


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [3,1,5,8],
            167
        ),
        (
            [35,16,83,87,84,59,48,41,20,54],
            1849648
        ),
        (
            [8,2,6,8,9,8,1,4,1,5,3,0,7,7,0,4,2,2],
            -1
        )
    ]
    f = s.maxCoins
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
