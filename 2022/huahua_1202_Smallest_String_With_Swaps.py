#!/usr/bin/env python3

from collections import defaultdict


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        lens = len(s)
        nexts = defaultdict(list)

        for x, y in pairs:
            nexts[y].append(x)
            nexts[x].append(y)

        visited = set()
        tmp = []
        idx = []
        def dfs(x):
            if x in visited:
                return
            idx.append(x)
            tmp.append(s[x])
            visited.add(x)
            for n in nexts.get(x, []):
                dfs(n)

        rs = list(s)
        for i in range(lens):
            if i not in visited:
                idx = []
                tmp = []
                dfs(i)
                idx.sort()
                tmp.sort()
                for k, char in zip(idx, tmp):
                    rs[k] = char

        return "".join(rs)
