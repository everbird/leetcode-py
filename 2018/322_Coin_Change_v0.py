#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    cache = {}

    def coinChange(self, coins, amount):
        if not coins:
            return -1
        self.cache = {}
        return self.dp(coins, amount)


    def dp(self, coins, amount):
        if amount in self.cache:
            return self.cache[amount]

        if amount == 0:
            return 0
        elif amount < 0:
            return -1
        min_cnt = float('inf')
        for c in coins:
            cnt = self.dp(coins, amount - c)
            if cnt != -1:
                min_cnt = min(min_cnt, cnt+1)

        r = min_cnt if min_cnt != float('inf') else -1
        self.cache[amount] = r
        return r


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                [1, 2, 5],
                11
            ),
            3
        ),
        (
            (
                [2],
                3
            ),
            -1
        ),
        (
            (
                [1,2,5],
                100
            ),
            20
        ),
        (
            (
                [186,419,83,408],
                6249
            ),
            20
        ),
        (
            (
                [159,342,471,125,269,151,310,485,471,356],
                6229
            ),
            14
        ),
        (
            (
                [370,417,408,156,143,434,168,83,177,280,117],
                9953
            ),
            24
        )

    ]
    f = s.coinChange
    for input_args, expected in tests:
        s.cache = {}

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
