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
        elif self.ranks[py] > self.ranks[px]:
            self.parents[px] = py
        else:
            self.parents[px] = py
            self.ranks[py] += 1

        return True


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        lenn = len(equations)
        u = UnionFindSet(lenn*2)

        m = {}
        cnt = 0
        def _get_index(x):
            nonlocal cnt, m
            if x in m:
                return m[x]

            m[x] = cnt
            cnt += 1
            return m[x]

        for s in equations:
            if "==" in s:
                x, y = s.split("==")
                if x == y:
                    continue

                u.union(_get_index(x), _get_index(y))

        for s in equations:
            if "!=" in s:
                x, y = s.split("!=")
                if u.find(_get_index(x)) == u.find(_get_index(y)):
                    return False

        return True
