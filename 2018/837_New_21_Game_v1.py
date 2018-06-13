#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if K == 0 or (N - K + 1) >= W:
            return 1.0

        dp = [1.0] + [0] * N
        dp_sum = dp[0]
        for i in range(1, N+1):
            dp[i] = dp_sum / W
            if i < K:
                dp_sum += dp[i]
            if i >= W:
                dp_sum -= dp[i - W]

        return sum(dp[K:])


def main():
    s = Solution()
    tests = [
        ((2, 1, 10), 0.2),
        ((10, 1, 10), 1.0),
        ((6, 1, 10), 0.6),
        ((21, 17, 10), 0.73278),
    ]
    for input_args, expected in tests:
        r = s.new21Game(*input_args)
        print 'Input:{}\tOutput:{}\tExpected:{}'.format(input_args, r, expected)

if __name__ == '__main__':
    main()
