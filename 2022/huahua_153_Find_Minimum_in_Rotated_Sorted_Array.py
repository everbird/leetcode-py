#!/usr/bin/env python3

class Solution:
    def findMin(self, nums: List[int]) -> int:
        s = 0
        e = len(nums)-1

        if nums[s] < nums[e]:
            return nums[0]

        m = 0
        while s < e:
            m = (s+e) // 2
            if nums[m] >= nums[0]:
                s = m + 1
            else:
                e = m

        return nums[e]
