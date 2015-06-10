#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        if not nums:
            return

        b = 0
        e = len(nums) - 1
        if b == e:
            return nums[0]

        while b < e:
            mid = (b + e) / 2
            if nums[mid] > nums[b]:
                b = mid
            else:
                e = mid

        return nums[mid+1] if nums[mid+1] < nums[mid] else nums[0]


if __name__ == '__main__':
    s = Solution()
    print s.findMin([4, 5, 6, 7, 0, 1, 2])
    print s.findMin([4, 5, 6, 7, 8, 0, 1, 2])
    print s.findMin([1, 0])
    print s.findMin([1])
    print s.findMin([1,2,3,4,5,6,7])
