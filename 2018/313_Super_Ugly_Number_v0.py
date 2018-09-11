#!/usr/bin/eni python
# encoding: utf-8

import heapq


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        uglies = [1]
        def gen(prime):
            for ugly in uglies:
                yield ugly * prime

        gen_merged = heapq.merge(*map(gen, primes))
        while len(uglies) < n:
            ugly = next(gen_merged)
            if ugly != uglies[-1]:
                uglies.append(ugly)

        return uglies[-1]


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                12,
                [2,7,13,19]
            ),
            32
        ),
    ]
    f = s.nthSuperUglyNumber
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
