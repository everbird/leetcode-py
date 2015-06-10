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
            while b+1 <= e and nums[b] == nums[b+1]:
                b += 1

            while e-1 >= b and nums[e] == nums[e-1]:
                e -= 1

            if b == e:
                return nums[b]

            mid = (b + e) / 2
            if nums[mid] >= nums[b] and mid != b:
                b = mid
            else:
                e = mid

        return nums[mid+1] if nums[mid] > nums[mid+1] else nums[0]


if __name__ == '__main__':
    s = Solution()
    print s.findMin([4, 5, 6, 6, 7, 0, 1, 2])
    print s.findMin([4, 5, 6, 7, 8, 8, 0, 1, 2])
    print s.findMin([8, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8])
    print s.findMin([1, 0])
    print s.findMin([1])
    print s.findMin([1,2,3,4,5,6,7])
    print s.findMin([10, 1, 10, 10, 10])
    print s.findMin([10, 10, 10, 1, 10])
    print s.findMin([1, 1])
