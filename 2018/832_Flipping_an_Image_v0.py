#!/usr/bin/eni python
# encoding: utf-8

class Solution(object):
    def flipAndInvertImage(self, A):
        N = len(A)
        for j in xrange(N):
            for i in xrange((N+1)//2):
                A[j][i], A[j][N-i-1] = (A[j][N-i-1]+1)%2, (A[j][i]+1)%2

        return A


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [[1,1,0],[1,0,1],[0,0,0]],
            [[1,0,0],[0,1,0],[1,1,1]]
        ),
        (
            [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]],
            [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
        ),

    ]
    f = s.flipAndInvertImage
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
