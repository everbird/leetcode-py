#!/usr/bin/env python3

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        sold = [0] * (n+1)
        held = [-float("inf")] * (n+1)
        for i in range(n):
            p = prices[i]
            sold[i+1] = max(sold[i], held[i] + p - fee)
            held[i+1] = max(held[i], sold[i]-p)

        return sold[-1]

# State transition


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        sold = 0
        held = -prices[0]
        for i in range(1, n):
            sold = max(sold, held + prices[i] - fee)
            held = max(held, sold-prices[i])

        return sold
