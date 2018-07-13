#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def largestSumOfAverages(self, A, K):
        N = len(A)
        cache = [0] * N
        s = 0
        for i, v in enumerate(A):
            s += v
            cache[i] = s

        def avg(i, j):
            # [...]
            return (cache[j] - cache[i-1] if i != 0 else cache[j]) / float(j - i + 1)

        dp = [avg(i, N-1) for i in range(N)]
        for k in range(K-1):
            for i in range(N):
                for j in range(i+1, N):
                    dp[i] = max(dp[i], avg(i, j-1)+dp[j])

        return dp[0]


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                [9,1,2,3,9],
                3
            ),
            20
        ),
    ]
    for input_args, expected in tests:
        r = s.largestSumOfAverages(*input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
