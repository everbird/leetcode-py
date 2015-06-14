#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0

        lenn = len(nums)
        b = e = 0
        r = nums[0]
        minl = None
        while e < lenn:
            if r >= s:
                x = e - b + 1
                if minl is None or minl > x:
                    minl = x
                if e == b:
                    e += 1
                    if e < lenn:
                        r += nums[e]
                r -= nums[b]
                b += 1
            else:
                e += 1
                if e < lenn:
                    r += nums[e]

        return minl or 0


if __name__ == '__main__':
    s = Solution()
    print s.minSubArrayLen(7, [2,3,1,2,4,3])
    print s.minSubArrayLen(70, [2,3,1,2,4,3])
    print s.minSubArrayLen(4, [2,3,1,2,4,3])
    print s.minSubArrayLen(15, [5,1,3 ,5,10,7,4,9,2,8])
    print s.minSubArrayLen(4, [1,4,4])
