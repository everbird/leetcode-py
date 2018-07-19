#!/usr/bin/eni python
# encoding: utf-8


from collections import Counter


class Solution(object):
    def longestSubstring(self, s, k):
        c = Counter(s)
        for x, cnt in c.iteritems():
            if cnt < k:
                items = s.split(x)
                return max([self.longestSubstring(i, k) for i in items])
        return len(s)


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                'aaabb',
                3
            ),
            3
        ),
    ]
    f = s.longestSubstring
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
