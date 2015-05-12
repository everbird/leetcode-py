#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]

        s = 0
        max_v = -2**31
        for i, n in enumerate(nums):
            if s + n <= 0:
                s = 0
                if max_v < n:
                    max_v = n

            else:
                s += n
                if max_v < s:
                    max_v = s

        return max_v


if __name__ == '__main__':
    s = Solution()
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print s.maxSubArray(a)

    a = [-2, -1]
    print s.maxSubArray(a)
