#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):

    def integerBreak(self, n):
        k = 2
        max_v = 0

        def f(k):
            x = n // k
            mod = n % k
            r = [x] * k
            for i in xrange(mod):
                r[i] += 1

            return r

        pre = 0
        while k <= n:
            v = reduce(lambda x,y: x*y, f(k), 1)
            if pre >= v:
                break

            pre = v
            max_v = max(max_v, v)
            k += 1

        return int(max_v)


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            2,
            1
        ),
        (
            10,
            36
        ),
        (
            0,
            0
        ),
        (
            8,
            18
        ),
        (
            14,
            162
        )
    ]
    f = s.integerBreak
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
