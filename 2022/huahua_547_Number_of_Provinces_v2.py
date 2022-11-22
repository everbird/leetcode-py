#!/usr/bin/env python3

class UnionFindSet:

    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * (n)

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
        elif self.ranks[px] < self.ranks[py]:
            self.parents[px] = py
        else:
            self.parents[px] = py
            self.ranks[py] += 1

        return True


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        u = UnionFindSet(n)
        for j in range(n):
            for i in range(j+1, n):
                if isConnected[j][i] == 1:
                    u.union(j, i)

        r = set()
        for i in range(n):
            r.add(u.find(i))

        return len(r)
