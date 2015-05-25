#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        max_p = -1
        min_p = 2**31
        max_profit = 0
        for i in range(len(prices)):
            p = prices[i]
            if min_p > p:
                min_p = p
                max_p = -1

            if p > max_p:
                max_p = p
                diff = p - min_p
                if max_profit < diff:
                    max_profit = diff

        return max_profit


if __name__ == '__main__':
    s = Solution()
    print s.maxProfit([5,3,1,3,6,8,4,7,9,0,4,8])
    print s.maxProfit([4,1,2])
