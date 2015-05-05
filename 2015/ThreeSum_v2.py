#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        r = []
        nums.sort()
        lenn = len(nums)
        for i, n in enumerate(nums[:-2]):
            lo = i + 1
            hi = lenn - 1
            target = -n
            while lo < hi:
                if nums[lo] + nums[hi] == target:
                    t = [n, nums[lo], nums[hi]]
                    if t not in r:
                        r.append(t)
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
                elif nums[lo] + nums[hi] > target:
                    hi -= 1
                else:
                    lo += 1

        return r


if __name__ == '__main__':
    a = [1,2,3,7,5,9,-1,-8,-3, 10]
    #a = [0,0,0]
    #a = [0,0,0,0]
    s = Solution()
    r = s.threeSum(a)
    print r
