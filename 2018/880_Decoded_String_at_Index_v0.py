#!/usr/bin/eni python
# encoding: utf-8

class Solution(object):
    def decodeAtIndex(self, S, K):
        N = 0
        for i, ch in enumerate(S):
            if ch in "23456789":
                N *= int(ch)
            else:
                N += 1

            if N >= K:
                break
        for j in xrange(i, -1, -1):
            ch = S[j]
            if ch in "23456789":
                N /= int(ch)
                K = K % N
            else:
                if K % N == 0:
                    return ch

                N -= 1



if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                "leet2code3",
                10
            ),
            "o"
        ),
        (
            (
                "ha22",
                5
            ),
            "h"
        ),
        (
            (
                "a2345678999999999999999",
                1
            ),
            "a"
        ),
        (
            (
                "vzpp636m8y",
                2920
            ),
            "z"
        ),
        (
            (
                "y959q969u3hb22odq595",
                222280369
            ),
            "y"
        ),
    ]
    f = s.decodeAtIndex
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
