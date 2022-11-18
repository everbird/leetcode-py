#!/usr/bin/env python3

class Solution:
    def findMin(self, nums: List[int]) -> int:
        s = 0
        e = len(nums)-1

        if e == 0 or nums[s] < nums[e]:
            return nums[0]

        while s<e:
            while s+1 <= e and nums[s] == nums[s+1]:
                s += 1

            while e-1 >= s and nums[e] == nums[e-1]:
                e -= 1

            if s == e:
                return nums[s]

            m = (s - e) // 2 + e
            if nums[m] >= nums[s] and s != m:
                s = m
            else:
                e = m

        return nums[m+1]
