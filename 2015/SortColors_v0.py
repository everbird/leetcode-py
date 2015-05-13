#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        lenn = len(nums)
        for t in range(1, 3):
            hi = 0
            while hi < lenn and nums[hi] != t:
                hi += 1

            if hi == len:
                continue

            ti = hi
            while ti < lenn:
                while ti < lenn and nums[ti] == t:
                    ti += 1

                if ti == lenn:
                    break

                nums[hi], nums[ti] = nums[ti], nums[hi]
                hi += 1
                ti += 1


if __name__ == '__main__':
    s = Solution()
    a = [0,1,2,1,0,2,1,2,1]
    s.sortColors(a)
    print a

    a = [1,0,1]
    s.sortColors(a)
    print a

    a = []
    s.sortColors(a)
    print a
