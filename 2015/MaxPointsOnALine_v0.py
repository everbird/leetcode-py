#!/usr/bin/env python
# encoding: utf-8


# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    # @param {Point[]} points
    # @return {integer}
    def maxPoints(self, points):
        lenp = len(points)
        max_c = 0
        for i in range(lenp):
            p1 = points[i]
            for j in range(i+1, lenp):
                p2 = points[j]
                count = 2
                for k in range(j+1, lenp):
                    p3 = points[k]
                    if self.verify(p1, p2, p3):
                        count += 1
                        if max_c < count:
                            max_c = count

        return max_c


    def verify(self, p1, p2, p3):
        if p1.x == p2.x:
            return p3.x == p1.x

        k = (p1.y - p2.y) / (p1.x - p2.x)
        b = p1.y - p1.x * k
        return (p3.x * k + b) == p3.y

if __name__ == '__main__':
    s = Solution()
    points = [
        Point(1,1), Point(4,4), Point(2,2), Point(2,3), Point(5,5)
    ]
    print s.maxPoints(points)
