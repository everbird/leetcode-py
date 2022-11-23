#!/usr/bin/env python3

class UnionFindSet:

    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n

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
        elif self.ranks[py] > self.ranks[px]:
            self.parents[px] = py
        else:
            self.parents[px] = py
            self.ranks[py] += 1

        return True


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        lens = len(strs)
        u = UnionFindSet(lens)
        
        for j in range(lens):
            for i in range(j+1, lens):
                if is_similar(strs[i], strs[j]):
                    u.union(i, j)

        r = set()
        for i in range(lens):
            _i = u.find(i)
            if _i not in r:
                r.add(_i)

        return len(r)


def is_similar(x, y):
    if len(x) != len(y):
        return False

    if x == y:
        return True

    cnt = 0
    n = len(x)
    for i in range(n):
        if x[i] != y[i]:
            cnt += 1

    if cnt == 2:
        return True

    return False
