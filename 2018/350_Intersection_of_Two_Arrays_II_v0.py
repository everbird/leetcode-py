#!/usr/bin/eni python
# encoding: utf-8
from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        r = {}
        for k, cnt1 in c1.iteritems():
            if k in c2:
                cnt2 = c2[k]
                r[k] = min(cnt1, cnt2)
        return reduce(lambda x, y: x + y, [[k] * cnt for k, cnt in r.iteritems()], [])


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                [1, 2, 2, 1],
                [2, 2]
            ),
            [2, 2]
        ),
    ]
    f = s.intersect
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
