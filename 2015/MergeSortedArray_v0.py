#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        if not nums2:
            return

        k = len(nums1) - 1
        a = m - 1
        b = n - 1
        while a >= 0 or b >= 0:
            if (a >= 0 and b >= 0 and nums1[a] > nums2[b]) or (a >= 0 and b < 0):
                nums1[k] = nums1[a]
                a -= 1
            elif (a >= 0 and b >= 0 and nums1[a] <= nums2[b]) or (a < 0 and b >= 0):
                nums1[k] = nums2[b]
                b -= 1

            k -= 1


if __name__ == '__main__':
    s = Solution()
    a = [1,3,6,7,9,0,0,0,0,0,0]
    s.merge(a, 5, [2,3,4,8,10,11], 6)
    print a

    a = [2,0]
    s.merge(a, 1, [1], 1)
    print a
