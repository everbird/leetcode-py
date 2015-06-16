#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        for i in range(k):
            t = self.heap_sort(nums)
            v = t[0]
            nums = nums[1:]

        return v

    def heap_sort(self, nums):
        lenn = len(nums)
        height = 0
        while 2**height < (lenn // 2):
            height += 1

        while height >= 0:
            for i in range(2**height, 2**(height+1)):
                if i+1 < lenn:
                    pi = (i - 1) // 2
                    li = i
                    ri = i+1
                    if nums[li] > nums[pi]:
                        nums[li], nums[pi] = nums[pi], nums[li]

                    if nums[ri] > nums[pi]:
                        nums[ri], nums[pi] = nums[pi], nums[ri]

            height -= 1

        return nums




if __name__ == '__main__':
    s = Solution()
    print s.findKthLargest([3,2,1,5,6,4], 2)
    #print s.heap_sort([3,2,1,5,6,4])
