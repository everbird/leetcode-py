#!/usr/bin/env python3

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        ng = len(g)
        ns = len(s)
        j = 0
        r = 0
        for i in range(ng):
            while j < ns and s[j] < g[i]:
                j += 1

            if j < ns:
                r += 1
                j += 1

        return r
