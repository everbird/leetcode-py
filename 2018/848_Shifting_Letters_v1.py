#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def shiftingLetters(self, S, shifts):
        len_s = len(S)
        r = [None] * len_s
        v = 0
        for i in range(len_s-1, -1, -1):
            shift = shifts[i]
            v += shift
            r[i] = v

        chars = [
            rotate_char(S[i], v) for i, v in enumerate(r)
        ]
        return ''.join(chars)


def rotate_char(char, n):
    base = ord('a')
    _n = ord(char) - base
    return chr(base + ((_n + n) % 26))


def main():
    s = Solution()
    tests = [
        (
            (
                "abc",
                [3,5,9]
            ),
            "rpl"
        ),
    ]
    for input_args, expected in tests:
        r = s.shiftingLetters(*input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)

if __name__ == '__main__':
    main()
