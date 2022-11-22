#!/usr/bin/env python3

from collections import defaultdict, deque


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(dict)
        n = len(equations)
        for i in range(n):
            tgt, src = equations[i]
            v = values[i]
            d[src][tgt] = v
            d[tgt][src] = 1.0 / v

        rs = []
        for tgt, src in queries:
            if src not in d or tgt not in d:
                rs.append(-1.0)
                continue
            elif src == tgt and src in d:
                rs.append(1.0)
                continue

            q = deque([(src, 1.0)])
            visited = set()
            found = False
            while q and not found:
                n, r = q.popleft()
                visited.add(n)
                for x, xv in d[n].items():
                    if x in visited:
                        continue

                    if x == tgt:
                        rs.append(r*xv)
                        found = True
                        break
                    q.append((x, r*xv))
            if not found:
                rs.append(-1.0)

        return rs
