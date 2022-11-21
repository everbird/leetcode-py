#!/usr/bin/env python3

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        llen = len(isConnected)
        visited = set()

        r = 0
        def dfs(m):
            visited.add(m)
            for n in range(llen):
                if n in visited:
                    continue 

                if isConnected[m][n] == 1:
                    dfs(n)

        for i in range(llen):
            if i not in visited:
                r += 1
                dfs(i)

        return r
