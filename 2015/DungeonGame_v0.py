#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[][]} dungeon
    # @return {integer}
    def calculateMinimumHP(self, dungeon):
        _d = []
        for d in dungeon[::-1]:
            _d.append(d[::-1])

        lenh = len(_d)
        lenw = len(_d[0])
        line = [0] * lenw
        dp = [line[:] for i in range(lenh)]
        dp[0][0] = max(-_d[0][0]+1, 1)
        for j in range(1, lenh):
            dp[j][0] = max(dp[j-1][0] - _d[j][0], 1)

        for i in range(1, lenw):
            dp[0][i] = max(dp[0][i-1] - _d[0][i], 1)

        for j in range(1, lenh):
            for i in range(1, lenw):
                dp[j][i] = min(max(1, dp[j-1][i] - _d[j][i]),
                              max(1, dp[j][i-1] - _d[j][i]))

        return max(dp[-1][-1], 1)


if __name__ == '__main__':
    s = Solution()
    d = [
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5],
    ]
    print s.calculateMinimumHP(d)

    d = [
        [-3, 5],
    ]
    print s.calculateMinimumHP(d)
