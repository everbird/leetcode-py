#!/usr/bin/env python
# encoding: utf-8

from collections import Counter


# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __repr__(self):
        return '<{},{}>'.format(self.x, self.y)


class Solution:
    # @param {Point[]} points
    # @return {integer}
    def maxPoints(self, points):
        if not points:
            return 0

        lenp = len(points)
        max_c = 0
        for i in range(lenp):
            p1 = points[i]
            r = []
            same = 0
            for j in range(i+1, lenp):
                p2 = points[j]
                if p1.x == p2.x and p1.y == p2.y:
                    same += 1
                    continue

                k = (p1.y - p2.y) * 1.0 / (p1.x - p2.x) if p1.x != p2.x else None
                r.append(k)
            c = Counter(r)
            r = c.most_common()
            cnt = r[0][1] if r else 0
            cnt += same
            if max_c < cnt:
                max_c = cnt

        return max_c+1


if __name__ == '__main__':
    s = Solution()
    points = [
        Point(1,1), Point(4,4), Point(2,2), Point(2,3), Point(5,5)
    ]
    print s.maxPoints(points)

    points = [
        Point(0,0), Point(1,1), Point(0,0)
    ]
    print s.maxPoints(points)

    points = [
        Point(0,0), Point(0,0)
    ]
    print s.maxPoints(points)

    points = [
        Point(84,250), Point(0,0), Point(1,0), Point(0,-70), Point(0,-70), Point(1,-1), Point(21,10), Point(42,90), Point(-42,-230)
    ]
    print s.maxPoints(points)
