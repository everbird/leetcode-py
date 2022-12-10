#!/usr/bin/env python3

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * (m+1) for _ in range(n+1)]

        r = 0
        for j in range(1, n+1):
            for i in range(1, m+1):
                if matrix[j-1][i-1] == 1:
                    dp[j][i] = min(dp[j-1][i], dp[j-1][i-1], dp[j][i-1]) + 1
                    r += dp[j][i]

        return r
