#!/usr/bin/eni python
# encoding: utf-8


from collections import defaultdict


class Solution(object):
    def firstUniqChar(self, s):
        d_dup = set([])
        d_appear = set([])
        for c in s:
            if c in d_appear:
                d_dup.add(c)
            d_appear.add(c)
        for i, c in enumerate(s):
            if c not in d_dup:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            'leetcode',
            0
        ),
        (
            'loveleetcode',
            2
        ),
    ]
    f = s.firstUniqChar
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
