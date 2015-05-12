#!/usr/bin/env python
# encoding: utf-8


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def printl(items):
    for i in items:
        print i.start, i.end, '|',

    print '<<<'


class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort(key=lambda x: x.start)
        r = []
        cur = None
        for t in intervals:
            b, e = t.start, t.end

            if not cur:
                cur = Interval(b, e)
            elif b <= cur.end <= e:
                cur.end = e
            elif b > cur.end:
                r.append(cur)
                cur = Interval(b, e)

        r.append(cur)

        return r

if __name__ == '__main__':
    s = Solution()
    printl(s.merge([Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)]))
    printl(s.merge([Interval(1,3)]))
    printl(s.merge([Interval(1,4), Interval(2,3)]))
