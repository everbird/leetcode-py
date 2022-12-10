#!/usr/bin/env python3

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 1:
            return 0
        if n == 1:
            return nums[0]

        return max(simple_rob_so1(nums[:-1]), simple_rob_so1(nums[1:]))


def simple_rob(nums):
    n = len(nums)
    if n < 1:
        return 0
    elif n == 1:
        return nums[0]

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    return dp[n-1]


def simple_rob_so1(nums):
    n = len(nums)
    if n < 1:
        return 0
    elif n == 1:
        return nums[0]

    a = nums[0]
    b = max(nums[0], nums[1])
    for i in range(2, n):
        tmp = b
        b = max(b, a+nums[i])
        a = tmp
    return b

# S:O(1)
