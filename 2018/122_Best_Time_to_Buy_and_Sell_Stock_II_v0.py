#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):

    def maxProfit(self, prices):
        flag_inc = False
        pre = None
        len_p = len(prices)
        lo = 0
        ans = 0
        for i in xrange(len_p):
            if pre is not None:
                p = prices[i]
                if prices[pre] > p:
                    if flag_inc:
                        ans += prices[pre] - prices[lo]
                    lo = i
                flag_inc = prices[pre] <= p

            pre = i

        if flag_inc:
            ans += prices[pre] - prices[lo]

        return ans


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [7,1,5,3,6,4],
            7
        ),
        (
            [1,2,3,4,5],
            4
        ),
        (
            [7,6,4,3,1],
            0
        ),
        (
            [5,2,3,2,6,6,2,9,1,0,7,4,5,0],
            20
        ),
    ]
    f = s.maxProfit
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
