#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        if len(nums) < 3:
            return []

        d = {}
        r = set([])
        for i, m in enumerate(nums):
            for j, n in enumerate(nums[i+1:]):
                d[nums[i] + nums[i+j+1]] = [(nums[i], nums[i+j+1]), (nums[i+j+1], nums[i])] if nums[i] != nums[i+j+1] else [(nums[i], nums[i+j+1])]
                for k, x in enumerate(nums[:i+j+2]):
                    ts = d.get(-x)
                    if ts:
                        for t in ts:
                            if t[0] <= t[1] and t[1] <= x:
                                r.add(t + (x, ))

        return list(r)


if __name__ == '__main__':
    a = [1,2,3,7,5,9,-1,-8,-3, 10]
    #a = [0,0,0]
    #a = [0,0,0,0]
    s = Solution()
    r = s.threeSum(a)
    print r
