#!/usr/bin/env python3

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1 = p2 = 0

        n1 = len(firstList)-1
        n2 = len(secondList)-1

        rs = []
        while p1 <= n1 and p2 <= n2:
            s1, e1 = firstList[p1]
            s2, e2 = secondList[p2]
            if s1 > e2:
                p2 += 1
                continue

            if s2 > e1:
                p1 += 1
                continue

            rs.append([max(s1, s2), min(e1, e2)])

            if e1 < e2:
                p1 += 1
            else:
                p2 += 1

        return rs
