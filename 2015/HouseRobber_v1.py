#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
            return 0

        lenn = len(nums)
        if lenn == 1:
            return nums[0]

        dp = [0] * (lenn+1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, lenn+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])

        return dp[lenn]


if __name__ == '__main__':
    s = Solution()
    print s.rob([1,5,6,4,3,6,8])
