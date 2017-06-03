#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        index1 = index2 = 0
        count = (len1 + len2) // 2 + 1
        pre = current = 0

        while count > 0:
            pre = current
            v1 = nums1[index1] if index1 < len1 else None
            v2 = nums2[index2] if index2 < len2 else None

            if v1 is None:
                index2 +=1
                current = v2 if v2 is not None else v1
            elif v2 is None:
                index1 += 1
                current = v1 if v1 is not None else v2
            elif v1 >= v2:
                index2 +=1
                current = v2 if v2 is not None else v1
            else:
                index1 += 1
                current = v1 if v1 is not None else v2

            count -= 1

        if (len1 + len2) % 2 == 0:
            return (pre + current) / 2.0
        else:
            return current


if __name__ == '__main__':
    #a = [1, 3, 5, 7]
    #b = [2, 4, 6, 8, 9, 10]
    #a = []
    #b = [2, 3]
    #a = [1]
    #b = [1]
    #a = [2]
    #b = []
    #a = [3, 4]
    #b = []
    a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    b = [0, 6]
    s = Solution()
    r = s.findMedianSortedArrays(a, b)
    print r
