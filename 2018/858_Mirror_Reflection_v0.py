#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def mirrorReflection(self, p, q):
        gcd_v = gcd(p, q)

        m = [
            (None, 0),
            (2, 1)
        ]
        x = (p / gcd_v) % 2
        y = (q / gcd_v) % 2
        return m[y][x]


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                2,
                1
            ),
            2
        ),
        (
            (
                4,
                2
            ),
            2
        )
    ]
    for input_args, expected in tests:
        r = s.mirrorReflection(*input_args)
        result = r == expected
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(result, input_args, r, expected)
