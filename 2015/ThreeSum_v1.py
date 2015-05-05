#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        r = []
        nums.sort()
        for i, n in enumerate(nums):
            ts = twoSum(nums[i + 1:], -nums[i])
            for t in ts:
                tt = [nums[i]] + t
                if tt not in r:
                    r.append(tt)

        return r


def twoSum(nums, target):
    r = []
    d = {}
    for n in nums:
        if d.get(target - n):
            r.append([min(n, target - n), max(n, target - n)])
        else:
            d[n] = True

    return r


if __name__ == '__main__':
    #a = [1,2,3,7,5,9,-1,-8,-3, 10]
    #a = [0,0,0]
    a = [0,0,0,0]
    s = Solution()
    r = s.threeSum(a)
    print r
