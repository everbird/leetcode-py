#!/usr/bin/env python3

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profile = 0
        pre = None
        n = len(prices)
        for i in range(n):
            if pre is None:
                pre = prices[i]
                continue

            if prices[i] - pre > 0:
                max_profile += prices[i]-pre

            pre = prices[i]

        return max_profile
