#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        nums = sorted(nums)
        b = 0
        e = len(nums) - 1
        mid = (b+e) / 2
        return nums[mid]


if __name__ == '__main__':
    s = Solution()
    print s.majorityElement([3,1,2,3,2,3,3])
