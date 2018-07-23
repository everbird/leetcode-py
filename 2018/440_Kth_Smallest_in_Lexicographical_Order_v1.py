#!/usr/bin/eni python
# encoding: utf-8

class Solution(object):
    def findKthNumber(self, n, k):
        r = 1
        for i in range(k-1):
            r = transfer(r, n)

        return r


def transfer(x, n):
    if x*10 <= n:
        return x*10

    if x >= n:
        x //= 10

    x += 1
    while x % 10 == 0:
        x //= 10
    return x


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                13,
                2
            ),
            10
        ),
        (
            (
                10,
                3
            ),
            2
        ),
    ]
    f = s.findKthNumber
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
