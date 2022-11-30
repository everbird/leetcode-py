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
    if s > e:
        return 0

    n = e - s + 1
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = nums[s]
    for i in range(2, n+1):
        dp[i] = max(dp[i-1], dp[i-2]+nums[s+i-1])

    return dp[n]
