#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def profitableSchemes(self, G, P, group, profit):
        dp = [[0] * (G+1) for x in range(P+1)]
        dp[0][0] = 1
        for p, g in zip(profit, group):
            for i in range(P, -1, -1):
                for j in range(G-g,-1,-1):
                    dp[min(P, i+p)][j+g] += dp[i][j]

        return sum(dp[P]) % (10**9+7)



if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                5,
                3,
                [2,2],
                [2,3]
            ),
            2
        ),
        (
            (
                10,
                5,
                [2,3,5],
                [6,7,8]
            ),
            7
        ),
        (
            (
                1,
                1,
                [2,2,2,2,2],
                [1,2,1,1,0]
            ),
            0
        ),
        (
            (
                10,
                1,
                [7,1,9,1,9],
                [1,2,2,1,0]
            ),
            12
        ),
        # (
        #     (
        #         10,
        #         1,
        #         [6,3,6,1,10,1,11,6,8,8,11,10,9,10,4,7,9,6,7,9,10,8,4,6,7,7,9,4,4,4,8,6,7,10,5,2,1,6,11,3,8,9,3,2,8,4,7,10,9,5,3,6,10,4,5,4,10,3,8,6,11,10,6,9,8,11,3,7,2,7,7,9,7,10,1,3,3,9,6,3,11,3,5,10,9,4,10,6,4,10,9,2,1,1,9,10,5,10,7,6],
        #         [2,0,0,1,2,0,0,1,2,1,1,2,2,2,1,0,2,2,1,1,0,0,2,2,0,2,2,2,0,1,2,1,1,0,0,2,2,2,2,0,0,0,0,2,0,0,1,0,2,1,0,2,0,0,1,2,2,1,1,2,1,1,2,0,2,0,0,1,1,1,0,1,1,2,2,1,0,0,1,0,2,2,1,2,2,0,0,2,0,2,2,1,0,2,0,1,0,1,0,2],
        #     ),
        #     -1
        # ),
    ]
    f = s.profitableSchemes
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
