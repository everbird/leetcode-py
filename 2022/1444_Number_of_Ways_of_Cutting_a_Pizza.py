#!/usr/bin/env python3

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        n = len(pizza)
        m = len(pizza[0])
        MOD = 10**9 + 7
        dp = [[[None] * k for _ in range(m)] for _ in range(n)]
        _sum = [[0] * (m+1) for _ in range(n+1)]
        for j in range(n-1, -1, -1):
            for i in range(m-1, -1, -1):
                _sum[j][i] = _sum[j+1][i] + _sum[j][i+1] - _sum[j+1][i+1] + int(pizza[j][i] == "A")

        def dfs(x, y, kk):
            if _sum[y][x] == 0:
                return 0

            if kk == 0:
                return 1

            if dp[y][x][kk] is not None:
                return dp[y][x][kk]

            r = 0
            for j in range(y, n):
                if _sum[y][x] - _sum[j][x] > 0:
                    r = (r + dfs(x, j, kk-1)) % MOD

            for i in range(x, m):
                if _sum[y][x] - _sum[y][i] > 0:

                    r = (r + dfs(i, y, kk-1)) % MOD

            dp[y][x][kk] = r
            return r

        result = dfs(0, 0, k-1)
        return result
