#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):

    def combinationSum(self, candidates, target):
        ans = []
        return combination(candidates, 0, target)


def combination(candidates, index, target):
    if target < 0:
        return []

    if target == 0:
        return [[]]

    r = []
    for i, n in enumerate(candidates[index:]):
        items = combination(candidates, index+i, target-n)
        for item in items:
            r.append([n]+item)

    return r


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                [2,3,6,7],
                7
            ),
            [
                [7],
                [2, 2, 3]
            ]
        ),
        (
            (
                [2,3,5],
                8
            ),
            [
                [2,2,2,2],
                [2,3,3],
                [3,5],
            ]
        ),
    ]
    f = s.combinationSum
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
