#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        len_n = len(nums)
        for i in xrange(len_n):
            while nums[i] != i+1 and len_n >= nums[i] >= 1 and nums[nums[i]-1] != nums[i]:
                swap(nums, i, nums[i]-1)

        pre = None
        for i, n in enumerate(nums):
            if n != (i+1):
                return i+1
        return len_n+1


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


if __name__ == '__main__':
    s = Solution()
    print s.firstMissingPositive([1,2,0])
    print s.firstMissingPositive([3,4,-1,1])
    print s.firstMissingPositive([1,1])
