#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):

    def canCompleteCircuit(self, gas, cost):
        diffs = [g-c for (g, c) in zip(gas, cost)]
        if sum(diffs) < 0:
            return -1

        len_d = len(diffs)
        for i in xrange(len_d):

            if diffs[i] < 0:
                continue

            if is_valid(i, diffs):
                return i


def is_valid(start_i, diffs):
    s = 0
    len_d = len(diffs)
    for j in xrange(len_d):
        _i = (start_i + j) % len_d
        s += diffs[_i]
        if s < 0:
            return False

    return True


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                [1,2,3,4,5],
                [3,4,5,1,2]
            ),
            3
        ),
        (
            (
                [2,3,4],
                [3,4,3]
            ),
            -1
        ),
    ]
    f = s.canCompleteCircuit
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
