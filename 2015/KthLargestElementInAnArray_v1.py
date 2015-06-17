#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        return self.find(nums, 0, len(nums)-1, k)

    def find(self, nums, lo, hi, k):
        index = self.partition(nums, lo, hi)
        if index == (k-1):
            return nums[index]

        if index > (k-1):
            return self.find(nums, lo, index-1, k)
        else:
            return self.find(nums, index+1, hi, k)

    def partition(self, nums, lo, hi):
        pivot_v = nums[hi]
        store = lo
        for i in range(lo, hi):
            if nums[i] > pivot_v:
                nums[i], nums[store] = nums[store], nums[i]
                store += 1

        nums[hi], nums[store] = nums[store], nums[hi]
        return store


if __name__ == '__main__':
    s = Solution()
    print s.findKthLargest([3,2,1,5,6,4], 2)
    #a = [3,2,1,5,6,4]
    #print s.partition(a, 0, 5)
    #print a
