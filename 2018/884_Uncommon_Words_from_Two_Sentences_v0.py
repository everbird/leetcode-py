#!/usr/bin/eni python
# encoding: utf-8

from collections import Counter


class Solution(object):
    def uncommonFromSentences(self, A, B):
        ca = Counter(A.split())
        cb = Counter(B.split())
        c = ca + cb
        return [x for x, cnt in c.iteritems() if cnt == 1]


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                "this apple is sweet",
                "this apple is sour"
            ),
            ["sweet", "sour"]
        ),
        (
            (
                "apple apple",
                "banana"
            ),
            ["banana"]
        ),
    ]
    f = s.uncommonFromSentences
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
