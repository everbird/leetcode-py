#!/usr/bin/env python3

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        r = None
        d = float("inf")
        for i, k in enumerate(nums):
            if i+1 >= n-1:
                break

            t = target - k
            _sum = k + two_sum_closest(nums, i+1, n-1, t)
            if abs(target - _sum) < d:
                r = _sum
                d = abs(target - _sum)

        return r


def two_sum_closest(nums, s, e, target):
    r = None
    d = float("inf")
    while s < e:
        _sum = nums[s] + nums[e]
        if _sum == target:
            return _sum
        elif _sum > target:
            e -= 1
        else:
            s += 1

        if abs(_sum - target) < d:
            d = abs(_sum - target)
            r = _sum

    return r
