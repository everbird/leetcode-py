#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        max_profit = 0
        min_p = None
        max_p = 0
        for i in range(len(prices)):
            p = prices[i]
            if min_p is None or min_p > p:
                min_p = p
                max_p = 0

            if max_p < p:
                max_p = p
                max_profit = max(max_profit, max_p - min_p)

        return max_profit


if __name__ == '__main__':
    s = Solution()
    print s.maxProfit([5,3,1,3,6,8,4,7,9,0,4,8])
    print s.maxProfit([4,1,2])
