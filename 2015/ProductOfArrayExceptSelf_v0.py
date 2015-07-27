#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        lenn = len(nums)
        left = [1] * lenn
        right = [1] * lenn
        n = 1
        m = 1
        for i in range(lenn-1):
            n *= nums[i]
            left[i+1] = n
            ri = lenn - i - 1
            m *= nums[ri]
            right[lenn - i - 2] = m

        return [left[x]*right[x] for x in range(lenn)]


if __name__ == '__main__':
    s = Solution()
    print s.productExceptSelf([1,2,3,4])
