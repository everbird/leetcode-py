#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        counter = 1
        candidate = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            if counter == 0:
                candidate = x
                counter += 1
            elif x == candidate:
                counter += 1
            else:
                counter -= 1

        return candidate



if __name__ == '__main__':
    s = Solution()
    print s.majorityElement([3,1,2,3,2,3,3])
