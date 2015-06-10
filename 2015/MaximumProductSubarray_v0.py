#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        imax = imin = 1
        r = nums[0]
        for i in range(len(nums)):
            n = nums[i]
            if n > 0:
                imax = max(n, imax*n)
                imin = min(n, imin*n)
            else:
                t = imax
                imax = max(n, imin*n)
                imin = min(n, t*n)

            r = max(r, imax)

        return r


if __name__ == '__main__':
    s = Solution()
    print s.maxProduct([2,3,-2,4])
    print s.maxProduct([-1, 2,3, 2,4,5])
    print s.maxProduct([-2])
    print s.maxProduct([-1,-1])
    print s.maxProduct([-4,-3, -2])
