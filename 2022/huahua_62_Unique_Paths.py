#!/usr/bin/env python3

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * m for _ in range(n)]
        for j in range(1, n):
            for i in range(1, m):
                dp[j][i] = dp[j-1][i] + dp[j][i-1]

        return dp[n-1][m-1]
