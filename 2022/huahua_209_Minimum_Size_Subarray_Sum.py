#!/usr/bin/env python3

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        n = len(nums)
        s = 0
        e = -1
        _sum = 0
        r = float("inf")
        while s < n and e < n:
            if _sum < target:
                e += 1
                if e >= n:
                    break
                _sum += nums[e]
            else:
                r = min(r, e-s+1)
                _sum -= nums[s]
                s += 1

        return r
