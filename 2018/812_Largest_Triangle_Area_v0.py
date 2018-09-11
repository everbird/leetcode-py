#!/usr/bin/eni python
# encoding: utf-8

class Solution(object):
    def largestTriangleArea(self, points):
        size = len(points)
        permutation = []
        for i in xrange(size):
            for j in xrange(i+1, size):
                for k in xrange(j+1, size):
                    permutation.append(
                        (points[i], points[j], points[k])
                    )

        r = 0
        for p in permutation:
            area = get_area(p)
            r = max(r, area)

        return r


def get_area(points):
    p0, p1, p2 = points
    return abs(
        p0[0]*p1[1] + p1[0]*p2[1] + p2[0]*p0[1]
        - p0[0]*p2[1] - p1[0]*p0[1] - p2[0]*p1[1]
    ) / 2.0


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [[0,0],[0,1],[1,0],[0,2],[2,0]],
            2
        ),
    ]
    f = s.largestTriangleArea
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
