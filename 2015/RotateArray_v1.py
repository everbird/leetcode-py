#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        lenn = len(nums)
        _k = k % lenn
        _nums = nums[-_k:] + nums[:-_k]
        for i, n in enumerate(_nums):
            nums[i] = n


if __name__ == '__main__':
    s = Solution()
    a = [1,2,3,4,5,6,7]
    s.rotate(a, 3)
    print a

    a = [1,2]
    s.rotate(a, 3)
    print a
