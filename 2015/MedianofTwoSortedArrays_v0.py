#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1) + len(nums2)
        i1 = i2 = 0
        p = r = 0
        for i in range(n // 2 + 1):
            p = r
            a = nums1[i1] if len(nums1) >= i1 + 1 else None
            b = nums2[i2] if len(nums2) >= i2 + 1 else None
            if b is None or (a and b and a <= b):
                r = nums1[i1]
                i1 += 1
            elif a is None or (a and b and a > b):
                r = nums2[i2]
                i2 += 1

        if n % 2 == 1:
            return r
        else:
            return (r + p) * 0.5


if __name__ == '__main__':
    #a = [1, 3, 5, 7]
    #b = [2, 4, 6, 8, 9, 10]
    #a = []
    #b = [2, 3]
    #a = [1]
    #b = [1]
    a = [2]
    b = []
    s = Solution()
    r = s.findMedianSortedArrays(a, b)
    print r
