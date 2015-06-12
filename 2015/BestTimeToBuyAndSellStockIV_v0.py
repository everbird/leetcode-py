#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} k
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, k, prices):
        lenp = len(prices)
        if k > (lenp/2):
            return self.quick_solution(prices)

        dp = [None] * (2*k+1)
        dp[0] = 0
        for i in range(lenp):
            for j in range(1, min(2 * k, i + 1) + 1):
                dp[j] = max(dp[j], dp[j-1] + prices[i]*[1, -1][j % 2])

        return dp[-1]

    def quick_solution(self, prices):
        r = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                r += prices[i+1] - prices[i]
        return r


if __name__ == '__main__':
    s = Solution()
    print s.maxProfit(3, [1,3,6,8,5,9,4])
