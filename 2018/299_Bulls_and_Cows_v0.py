#!/usr/bin/eni python
# encoding: utf-8

from collections import Counter


class Solution(object):
    def getHint(self, secret, guess):
        secret_c = Counter(secret)
        guess_c = Counter(guess)
        a = 0
        b = 0
        check_b = []
        for s_ch, g_ch in zip(secret, guess):
            if s_ch == g_ch:
                a += 1
                secret_c[g_ch] -= 1
            else:
                check_b.append(g_ch)

        for g_ch in check_b:
            if secret_c.get(g_ch, 0) > 0:
                b += 1
                secret_c[g_ch] -= 1

        return '{}A{}B'.format(a, b)


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                "1807",
                "7810"
            ),
            "1A3B"
        ),
        (
            (
                "1123",
                "0111"
            ),
            "1A1B"
        ),
        (
            (
                "1122",
                "1222"
            ),
            "3A0B"
        )
    ]
    f = s.getHint
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
