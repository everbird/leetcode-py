#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        nums1 = map(int, version1.split('.'))
        nums2 = map(int, version2.split('.'))

        while nums1 and nums2:
            if nums1[0] > nums2[0]:
                return 1
            elif nums1[0] < nums2[0]:
                return -1
            else:
                nums1 = nums1[1:]
                nums2 = nums2[1:]

        while nums1 and nums1[0]==0:
            nums1 = nums1[1:]

        while nums2 and nums2[0]==0:
            nums2 = nums2[1:]

        if not nums1 and not nums2:
            return 0
        elif nums1:
            return 1
        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    #print s.compareVersion('0.1', '1.1')
    #print s.compareVersion('1.2', '1.1')
    #print s.compareVersion('13.37', '13.37')
    print s.compareVersion('1', '1.1')
    print s.compareVersion('1.0', '1')
