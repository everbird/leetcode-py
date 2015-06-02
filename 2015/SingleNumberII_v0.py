#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        ones = 0
        twos = 0
        for i in range(len(nums)):
            ones = (ones ^ nums[i]) & ~twos
            twos = (twos ^ nums[i]) & ~ones

        return ones

if __name__ == '__main__':
    s = Solution()
    print s.singleNumber([1,1,3,1,4,5,5,5,4,4])
