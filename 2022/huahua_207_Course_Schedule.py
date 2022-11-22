#!/usr/bin/env python3

from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        for src, tgt in prerequisites:
            d[src].append(tgt)

        visited = [0] * numCourses

        def has_cycle(n):
            visited[n] = 1
            pres = d.get(n, [])
            for pre in pres:
                if visited[pre] == 1:
                    return True
                elif visited[pre] == 0:
                    if has_cycle(pre):
                        # otherwise just skip rather than return False
                        return True

            visited[n] = 2
            return False


        for i in range(numCourses):
            if visited[i] == 0 and has_cycle(i):
                return False

        return True
