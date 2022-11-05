#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):

    def canCompleteCircuit(self, gas, cost):
        if sum(cost) > sum(gas):
            return -1

        start = 0
        tank = 0
        len_n = len(cost)
        for i in xrange(len_n):
            v = gas[i] - cost[i]
            tank += v
            if tank < 0:
                start = i+1
                tank = 0
        return start


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
