#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def reverseString(self, s):
        return s[::-1]


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            'hello',
            'olleh'
        ),
    ]
    f = s.reverseString
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
