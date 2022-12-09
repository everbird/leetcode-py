#!/usr/bin/env python3

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        dp = [[float("inf")] * (m+1) for _ in range(n+1)]
        dp[n][m-1] = dp[n-1][m] = 1
        for j in range(n-1, -1, -1):
            for i in range(m-1, -1, -1):
                dp[j][i] = max(1, min(dp[j][i+1], dp[j+1][i]) - dungeon[j][i])
        return dp[0][0]

# bottom-up
