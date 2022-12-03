#!/usr/bin/env python3

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rs = []
        n = len(nums)
        pre = None
        for i, t in enumerate(nums):
            if t == pre:
                continue

            _rs = two_sum(nums, i+1, n-1, -t)
            if _rs:
                for r in _rs :
                    rs.append([t, nums[r[0]], nums[r[1]]])

            pre = t

        return rs


def two_sum(nums, s, e, target):
    rs = []
    while s < e:
        _sum = nums[s] + nums[e]
        shrink = [False, False]
        if target == _sum:
            rs.append([s, e])
            s += 1
            e -= 1
            shrink = [True, True]

        elif target > _sum:
            s += 1
            shrink[0] = True
        else:
            e -= 1
            shrink[1] = True

        if shrink[0]:
            while s < e and nums[s] == nums[s-1]:
                s += 1

        if shrink[1]:
            while s < e and nums[e] == nums[e+1]:
                e -= 1

    return rs
