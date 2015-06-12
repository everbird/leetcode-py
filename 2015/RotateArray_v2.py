#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        lenn = len(nums)
        k = k % lenn
        self.in_place_reverse(nums, 0, lenn-k-1)
        self.in_place_reverse(nums, lenn-k, lenn-1)
        self.in_place_reverse(nums, 0, lenn-1)


    def in_place_reverse(self, nums, b, e):
        while b <= e:
            nums[b], nums[e] = nums[e], nums[b]
            b += 1
            e -= 1


if __name__ == '__main__':
    s = Solution()
    a = [1,2,3,4,5,6,7]
    s.rotate(a, 3)
    print a

    a = [1,2]
    s.rotate(a, 3)
    print a

    a = [1,2,3,4,5,6]
    s.rotate(a, 2)
    print a

    a = [1,2]
    s.rotate(a, 0)
    print a

    a = [1,2]
    s.rotate(a, 2)
    print a
