#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        lenn = len(nums)
        max_v = 0
        for i in range(lenn-1):
            n = nums[i]
            if n == 0 and max_v <= i:
                return False

            max_v = max(max_v, n+i)
        return True


if __name__ == '__main__':
    s = Solution()
    print s.canJump([2,3,1,1,4])
    print s.canJump([3,2,1,0,4])
    print s.canJump([0])
    print s.canJump([3,2,1,0])
