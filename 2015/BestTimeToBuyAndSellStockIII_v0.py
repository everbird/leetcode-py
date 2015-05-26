#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if not prices:
            return 0

        max_p = 0
        for i in range(len(prices)):
            l = self._maxProfit(prices[:i])
            r = self._maxProfit(prices[i:])
            v = l + r
            if max_p < v:
                max_p = v

        return max_p

    def _maxProfit(self, prices):
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
    print s.maxProfit([4,1,2,5,7,9,3,5])
    print s.maxProfit([1])
    print s.maxProfit([1,2])
    print s.maxProfit([1,4,2])
    print s.maxProfit([3,2,6,5,0,3])
    print s.maxProfit([1,2,4,2,5,7,2,4,9,0])
