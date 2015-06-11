#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        b = 0
        e = len(nums) - 1

        while b <= e:
            mid = (b+e) / 2

            if b == e:
                return b

            if b+1 == e:
                return b if nums[b] > nums[e] else e

            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1] < nums[mid] < nums[mid+1]:
                b = mid + 1
            elif nums[mid-1] > nums[mid] > nums[mid+1]:
                e = mid - 1
            else:
                e = mid

        return mid


if __name__ == '__main__':
    s = Solution()
    print s.findPeakElement([1, 2, 3, 1])
    print s.findPeakElement([1, 2, 1, 2,3,4,3])
    print s.findPeakElement([9,8,7,6,5,4,3,2,3,4,2,1])
    print s.findPeakElement([1])
    print s.findPeakElement([1, 2])
