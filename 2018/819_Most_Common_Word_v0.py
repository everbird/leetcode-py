#!/usr/bin/eni python
# encoding: utf-8

from collections import Counter


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        punctuations = "!?',;."
        for p in punctuations:
            paragraph = paragraph.replace(p, '')

        c = Counter(paragraph.lower().split())
        for b in banned:
            if b in c:
                del c[b]

        return c.most_common(1)[0][0]


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                "Bob hit a ball, the hit BALL flew far after it was hit.",
                ["hit"]
            ),
            "ball"
        ),
    ]
    f = s.mostCommonWord
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
