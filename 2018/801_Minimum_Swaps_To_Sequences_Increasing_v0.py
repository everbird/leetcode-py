#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def minSwap(self, A, B):
        len_n = len(A)
        dp = [(0, 1)]
        for i in range(1, len_n):
            a, b = float('inf'), float('inf')
            if A[i-1] < A[i] and B[i-1] < B[i]:
                a = dp[i-1][0]
                b = dp[i-1][1] + 1

            if A[i-1] < B[i] and B[i-1] < A[i]:
                a = min(dp[i-1][1], a)
                b = min(dp[i-1][0] + 1, b)

            dp += [(a, b)]

        return min(dp[len_n-1])


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                [1,3,5,4],
                [1,2,3,7]
            ),
            1
        ),
        (
            (
                [0,4,4,5,9],
                [0,1,6,8,10]
            ),
            1
        ),
    ]
    for input_args, expected in tests:
        r = s.minSwap(*input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
