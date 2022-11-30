#!/usr/bin/env python3

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        return max(
            rob_simple(nums, 0, n-2),
            rob_simple(nums, 1, n-1),
            )

def rob_simple(nums, s, e):
    t1 = t2 = 0
    for i in range(s, e+1):
        tmp = t1
        t1 = max(nums[i]+t2, t1)
        t2 = tmp
    return t1

# Space: O(1)
