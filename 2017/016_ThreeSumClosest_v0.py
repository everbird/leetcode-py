#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()
        r = None
        for i, n in enumerate(nums):
            _twosum = self.twoSumClosest(nums[i+1:], target - n)
            if _twosum is None:
                continue

            _sum = _twosum + n
            if r is None or abs(target - _sum) < abs(target - r):
                r = _sum

        return r

    def twoSumClosest(self, nums, target):
        s = 0
        e = len(nums) - 1
        r = None
        while s < e:
            _sum = nums[s] + nums[e]
            if r is None or abs(target - _sum) < abs(target - r) :
                r = _sum

            if target > _sum:
                s += 1
            else:
                e -= 1

        return r


if __name__ == '__main__':
    #a = [-1, 2, 1, -4]
    a = [0, 2, 1, -3]
    s = Solution()
    r = s.threeSumClosest(a, 1)
    print r
