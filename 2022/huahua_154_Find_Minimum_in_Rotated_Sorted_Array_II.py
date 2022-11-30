#!/usr/bin/env python3

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[0] < nums[n-1]:
            return nums[0]

        s = 0
        e = n-1
        while s <= e:
            while s < e and nums[s] == nums[s+1]:
                s += 1
            while s < e and nums[e] == nums[e-1]:
                e -= 1

            if s == e:
                return nums[s]

            m = (s+e) // 2
            if nums[m] > nums[m+1]:
                return nums[m+1]

            if nums[m] < nums[m-1]:
                return nums[m]

            if nums[m] >= nums[s]:
                s = m + 1
            else:
                e = m - 1

        return
