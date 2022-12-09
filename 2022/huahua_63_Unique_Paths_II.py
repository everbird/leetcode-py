#!/usr/bin/env python3

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[1] * m for _ in range(n)]
        for j in range(1, n):
            if obstacleGrid[j][0] == 0:
                dp[j][0] = dp[j-1][0]
            else:
                dp[j][0] = 0

        for i in range(1, m):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = dp[0][i-1]
            else:
                dp[0][i] = 0

        for j in range(1, n):
            for i in range(1, m):
                if obstacleGrid[j][i] == 1:
                    dp[j][i] = 0
                else:
                    dp[j][i] = dp[j-1][i] + dp[j][i-1]
        return dp[n-1][m-1]
