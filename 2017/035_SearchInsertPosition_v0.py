#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        if not nums or target < nums[0]:
            return 0
        return binary_search(nums, target)


def binary_search(nums, target):
    b = 0
    e = len(nums) - 1
    flag = 0
    m = None
    mid = 0
    while b <= e:
        mid = (b + e) // 2
        m = nums[mid]
        if m == target:
            return mid
        elif m > target:
            e = mid - 1
        else:
            b = mid + 1

    return mid if m > target else mid + 1



if __name__ == '__main__':
    s = Solution()
    print s.searchInsert([1,3,5,6], 5)
    print s.searchInsert([1,3,5,6], 2)
    print s.searchInsert([1,3,5,6], 7)
    print s.searchInsert([1,3,5,6], 0)
