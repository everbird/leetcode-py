#!/usr/bin/env python
# encoding: utf-8


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        r = []
        f = True
        if not intervals:
            return [newInterval]

        if intervals[0].start > newInterval.end:
            return [newInterval] + intervals
        elif intervals[-1].end < newInterval.start:
            return intervals + [newInterval]

        for n in intervals:
            if newInterval.start >= n.start and newInterval.end <= n.end:
                return intervals

            elif n.end < newInterval.start:
                r.append(n)

            elif n.start > newInterval.end:
                if f:
                    r.append(newInterval)
                    f = False
                r.append(n)

            elif n.start <= newInterval.start and newInterval.end > n.end:
                newInterval = Interval(n.start, newInterval.end)
            elif newInterval.end <= n.end and newInterval.start < n.start:
                newInterval = Interval(newInterval.start, n.end)

        if f:
            r.append(newInterval)

        return r


def printl(items):
    for i in items:
        print i.start, i.end, '|',

    print '<<<'


if __name__ == '__main__':
    s = Solution()
    printl( s.insert([Interval(1,3), Interval(6,9)], Interval(2,5)) )
    printl( s.insert([Interval(1,2), Interval(3,5), Interval(6,7), Interval(8,10), Interval(12,16)], Interval(4,9)) )
    printl( s.insert([Interval(1,5)], Interval(2,3)) )
    printl( s.insert([Interval(1,5)], Interval(6,8)) )
    printl( s.insert([Interval(0,2), Interval(3,5), Interval(6,8), Interval(10,12), Interval(13,15)], Interval(4,7)) )
    printl( s.insert([Interval(1,5)], Interval(0,6)) )
    printl( s.insert([Interval(0,5), Interval(9,12)], Interval(7,16)) )
    printl( s.insert([Interval(3,5), Interval(12,15)], Interval(6,6)) )
