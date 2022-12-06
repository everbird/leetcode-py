#!/usr/bin/env python3

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 0
        n = len(prices)
        for i in range(n-1):
            r1 = simple_max_profit(prices, 0, i)
            r2 = simple_max_profit(prices, i, n-1)
            r = max(r, r1+r2)

        return r

def simple_max_profit(prices, start, end):
    minp = float("inf")
    r = 0
    for i in range(start, end+1):
        minp = min(minp, prices[i])
        r = max(r, prices[i]-minp)

    return r


# TLE
#

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left_profits = [0] * n
        right_profits = [0] * n
        minp = prices[0]
        maxp = prices[-1]
        for i in range(1, n):
            p = prices[i]
            minp = min(minp, p)
            left_profits[i] = max(left_profits[i-1], p-minp)
            _p = prices[n-1-i]
            maxp = max(maxp, _p)
            right_profits[n-1-i] = max(right_profits[n-i], maxp-_p)

        r = 0
        for i in range(n-1):
            r = max(r, left_profits[i]+right_profits[i])

        return r
