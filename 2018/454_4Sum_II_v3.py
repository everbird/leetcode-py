#!/usr/bin/eni python
# encoding: utf-8


from collections import Counter


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        AB = Counter([a+b for a in A for b in B])
        return sum([AB[-(c+d)] for c in C for d in D])



if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                [1,2],
                [-2,-1],
                [-1,2],
                [0,2],
            ),
            2
        ),
        (
            (
                [0,1,-1],
                [-1,1,0],
                [0,0,1],
                [-1,1,1],
            ),
            17
        ),
        (
            (
                [1,1,-1,-1],
                [-1,-1,1,1],
                [1,-1,0,-1],
                [1,1,-1,1],
            ),
            76
        ),
    ]
    for input_args, expected in tests:
        r = s.fourSumCount(*input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
