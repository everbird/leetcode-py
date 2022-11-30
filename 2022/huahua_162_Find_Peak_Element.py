#!/usr/bin/env python3

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        s = 0
        e = n - 1
        while s <= e:
            m = (s+e) // 2

            if m == e and nums[m] > nums[m-1]:
                return m

            if m == s and nums[m] > nums[m+1]:
                return m

            if nums[m-1] < nums[m] and nums[m+1] < nums[m]:
                return m

            if nums[m] < nums[m+1]:
                s = m + 1
            else:
                e = m - 1

        return
