#!/usr/bin/env python3

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[0][i] = matrix[0][i]

        for j in range(1, n):
            for i in range(n):
                v1 = dp[j-1][i-1] if i > 0 else float("inf")
                v2 = dp[j-1][i]
                v3 = dp[j-1][i+1] if i < (n-1) else float("inf")
                dp[j][i] = min(v1, v2, v3) + matrix[j][i]

        return min(dp[n-1])
