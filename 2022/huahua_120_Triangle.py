#!/usr/bin/env python3

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        h = len(triangle)
        dp = [[0] * i for i in range(1, h+1)]
        dp[0][0] = triangle[0][0]
        for j in range(1, h):
            for i in range(j+1):
                if i == 0:
                    dp[j][i] = dp[j-1][i]
                elif i == j:
                    dp[j][i] = dp[j-1][i-1]
                else:
                    dp[j][i] = min(dp[j-1][i], dp[j-1][i-1])

                dp[j][i] += triangle[j][i]

        return min(dp[h-1])
