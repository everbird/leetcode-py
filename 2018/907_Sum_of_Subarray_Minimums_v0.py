#!/usr/bin/eni python
# encoding: utf-8

class Solution(object):
    def sumSubarrayMins(self, A):
        r = 0
        n = len(A)
        for start_i in xrange(n):
            min_v = float('inf')
            for j in xrange(start_i, n):
                min_v = min(min_v, A[j])
                r += min_v
        return r % (10**9 + 7)



if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [3,1,2,4],
            17
        ),
    ]
    f = s.sumSubarrayMins
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)

        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
