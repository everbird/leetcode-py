#!/usr/bin/env python3

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # profit[i][j]: during the first i days, with most j transactins, the max profit can be reached, no stock at hand
        # balance[i][j]: during the first i days, with most j transactions, the max balance can be reached, with a stock at hand.
        # profit[i][j] = max(profit[i-1][j], balance[i-1][j]+prices[i])
        # do nothing or sell the stock at hand
        #
        # balance[i][j] = max(balance[i-1][j], profit[i-1][j-1]-prices[i])
        # do nothing or buy a stock at day i

        n = len(prices)
        profit = [0] * (k+1)
        balance = [-float("inf")] * (k+1)
        for i in range(n):
            for j in range(1, k+1):
                # in the loop i in range(n), can save 2 dimention to 1 dimention since i-1 can be re-used in-place
                balance[j] = max(balance[j], profit[j-1] - prices[i])
                profit[j] = max(profit[j], balance[j] + prices[i])

        return profit[k]
