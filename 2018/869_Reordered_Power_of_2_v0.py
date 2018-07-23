#!/usr/bin/eni python
# encoding: utf-8


from collections import defaultdict


class Solution(object):
    def reorderedPowerOf2(self, N):
        good_counters = list(gen_counters())
        counter = count_digits(N)
        return counter in good_counters


def gen_counters(length=32):
    for i in range(length):
        x = 1 << i
        yield count_digits(x)


def count_digits(N):
    counter = defaultdict(int)
    while N:
        b = N % 10
        counter[b] += 1
        N = N // 10
    return tuple([counter[x] for x in range(10)])


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            1,
            True
        ),
        (
            10,
            False
        ),
        (
            16,
            True
        ),
        (
            24,
            False
        ),
        (
            46,
            True
        ),
        (
            635824465,
            True
        ),
    ]
    f = s.reorderedPowerOf2
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
