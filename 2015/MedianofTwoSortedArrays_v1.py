#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return find_kth(nums1, nums2, n // 2 + 1)
        else:
            a = find_kth(nums1, nums2, n // 2)
            b = find_kth(nums1, nums2, n // 2 + 1)
            return (a + b) * 0.5


def find_kth(a, b, k):
    lena = len(a)
    lenb = len(b)
    if lena > lenb:
        return find_kth(b, a, k)

    if lena == 0:
        return b[k - 1]

    if k == 1:
        return min(a[0], b[0])

    pa = min(k // 2, lena)
    pb = k - pa

    if a[pa - 1] > b[pb - 1]:
        return find_kth(a, b[pb:], k - pb)
    else:
        return find_kth(a[pa:], b, k - pa)


if __name__ == '__main__':
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8, 9, 10]
    s = Solution()
    r = s.findMedianSortedArrays(a, b)
    print r
