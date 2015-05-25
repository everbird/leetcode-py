#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if not prices:
            return 0

        pre = None
        s = 0
        min_p = prices[0]
        for i in range(len(prices)):
            p = prices[i]

            if pre is not None:
                if p > pre:
                    pass
                else:
                    if min_p is not None:
                        s += (pre - min_p)

                    min_p = p

            pre = p

        s += (prices[-1] - min_p)

        return s


if __name__ == '__main__':
    s = Solution()
    print s.maxProfit([4,1,2,5,8,9,4,6])
    print s.maxProfit([4])
    print s.maxProfit([])
    print s.maxProfit([3,3,5,0,0,3,1,4])
