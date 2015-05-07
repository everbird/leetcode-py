#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        return binary_search(nums, target)


def binary_search(nums, k):
    b = 0
    e = len(nums) - 1
    while b <= e:
        mid = (b + e) // 2
        m = nums[mid]
        if k == m:
            return mid
        elif k > m:
            b = mid + 1
        else:
            e = mid - 1

    return mid if m > k else mid + 1


if __name__ == '__main__':
    s = Solution()
    print s.searchInsert([1,3,5,6], 5)
    print s.searchInsert([1,3,5,6], 2)
    print s.searchInsert([1,3,5,6], 7)
    print s.searchInsert([1,3,5,6], 0)
