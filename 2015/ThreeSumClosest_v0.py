#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nearest = 2**31
        nums.sort()
        for i, n in enumerate(nums):
            two_nearest = twoSumClosest(nums[i + 1:], target - n)
            t = two_nearest + n
            if abs(nearest - target) > abs(t - target):
                nearest = t

        return nearest


def twoSumClosest(nums, target):
    b = 0
    e = len(nums) - 1
    nearest = 2**31
    while b < e:
        t = nums[b] + nums[e]
        if abs(nearest - target) > abs(t - target):
            nearest = t

        if target > t:
            b += 1
        elif target < t:
            e -= 1
        else:
            return t

    return nearest


if __name__ == '__main__':
    a = [-1, 2, 1, -4]
    s = Solution()
    r = s.threeSumClosest(a, 1)
    print r
