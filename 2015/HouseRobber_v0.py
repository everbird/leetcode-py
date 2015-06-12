#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
            return 0

        lenn = len(nums)
        if lenn == 1:
            return nums[0]

        a = nums[0]
        r1 = self.rob(nums[2:])
        r2 = self.rob(nums[1:])
        return max(a+r1, r2)


if __name__ == '__main__':
    s = Solution()
    print s.rob([1,5,6,4,3,6,8])
