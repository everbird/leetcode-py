#!/usr/bin/env python3

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        # dp[i] = max(dp[i-1], prices[i]-L[i])
        dp[0] = 0
        lowest = prices[0]
        for i in range(n):
            p = prices[i]
            lowest = min(lowest, p)
            dp[i] = max(dp[i-1], p-lowest)

        return dp[n-1]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profile = 0
        for p in prices:
            min_price = min(min_price, p)
            max_profile = max(max_profile, p-min_price)

        return max_profile
