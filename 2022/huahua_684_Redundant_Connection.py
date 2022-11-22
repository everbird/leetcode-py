#!/usr/bin/env python3

class UnionFindSet:

    def __init__(self, n):
        self.parents = list(range(n+1))
        self.ranks = [0] * (n+1)

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
            self.ranks[px] += 1

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        u = UnionFindSet(len(edges))

        for x, y in edges:
            if not u.union(x, y):
                return [x, y]
