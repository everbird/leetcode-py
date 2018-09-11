#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def isMonotonic(self, A):
        n = len(A)
        direction = 0
        for i in xrange(n-1):

            if A[i] > A[i+1]:
                if direction == 1:
                    return False
                d = -1
            elif A[i] < A[i+1]:
                d = 1
                if direction == -1:
                    return False
            else:
                d = 0

            if d != 0:
                direction = d

        return True



if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [1,2,2,3],
            True
        ),
        (
            [6,5,4,4],
            True
        ),
        (
            [1,3,2],
            False
        ),
        (
            [1,2,4,5],
            True
        ),
        (
            [1,1,1],
            True
        )
    ]
    f = s.isMonotonic
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
