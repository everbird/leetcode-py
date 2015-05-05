#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        nums.sort()
        r = []
        for i, n in enumerate(nums):
            ts = threeSum(nums[i + 1:], target - n)
            for t in ts:
                tt = (n, ) + t
                if tt not in r:
                    r.append(tt)
        return r


def threeSum(nums, target):
    r = []
    for i, n in enumerate(nums):
        ts = twoSum(nums[i + 1:], target - n)
        for t in ts:
            tt = (n, ) + t
            if tt not in r:
                r.append(tt)
    return r


def twoSum(nums, target):
    d = {}
    r = []
    for n in nums:
        t = d.get(target - n)
        if t:
            r.append((target - n, n))
        else:
            d[n] = True

    return r


if __name__ == '__main__':
    a = [1, 0, -1, 0, -2, 2]
    s = Solution()
    r = s.fourSum(a, 0)
    print r
