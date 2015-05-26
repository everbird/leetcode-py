#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if not prices:
            return 0

        lenp = len(prices)
        maxl = [0] * lenp
        maxr = [0] * lenp
        maxl[0] = 0
        min_v = prices[0]
        max_rv = prices[-1]
        for i in range(lenp):
            maxl[i] = max(maxl[i-1], prices[i] - min_v)
            if min_v > prices[i]:
                min_v = prices[i]
            ri = lenp - i - 1
            maxr[ri] = max(maxr[lenp - 1], max_rv - prices[ri])
            if max_rv < prices[ri]:
                max_rv = prices[ri]

        m = 0
        for l, r in zip(maxl, maxr):
            if m < l+r:
                m = l+r

        return m


if __name__ == '__main__':
    s = Solution()
    print s.maxProfit([4,1,2,5,7,9,3,5])
    print s.maxProfit([1])
    print s.maxProfit([1,2])
    print s.maxProfit([1,4,2])
    print s.maxProfit([3,2,6,5,0,3])
    print s.maxProfit([1,2,4,2,5,7,2,4,9,0])
