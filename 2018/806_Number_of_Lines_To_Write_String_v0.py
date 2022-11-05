#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):

    def numberOfLines(self, widths, S):
        num = 0
        lines = 1
        for ch in S:
            w = widths[ord(ch) - ord('a')]
            if num + w > 100:
                num = w
                lines += 1
            else:
                num += w

        return [lines, num]


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
                "abcdefghijklmnopqrstuvwxyz"
            ),
            [3, 60]
        ),
        (
            (
                [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
                "bbbcccdddaaa"
            ),
            [2, 4]
        ),
    ]
    f = s.numberOfLines
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
