#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):

    def fairCandySwap(self, A, B):
        a = sum(A)
        b = sum(B)
        _A = sorted(A)
        _B = sorted(B)
        t = (a + b) / 2
        diff_a = t - a
        ia = ib = 0
        while _A[ia] + diff_a != _B[ib]:
            if _A[ia] + diff_a > _B[ib]:
                ib += 1
            else:
                ia += 1
        return [_A[ia], _B[ib]]



if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                [1, 1],
                [2, 2]
            ),
            [1, 2]
        ),
        (
            (
                [1, 2],
                [2, 3]
            ),
            [1, 2]
        ),
        (
            (
                [2],
                [1, 3]
            ),
            [2, 3]
        ),
        (
            (
                [1, 2, 5],
                [2, 4]
            ),
            [5, 4]
        ),
    ]
    f = s.fairCandySwap
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
