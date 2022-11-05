#!/usr/bin/eni python
# encoding: utf-8


from collections import defaultdict


class Solution(object):

    def findCircleNum(self, M):
        d = {}
        groups = defaultdict(set)
        N = len(M)
        for i in xrange(N):
            groups[i].add(i)
            d[i] = i

        for j in xrange(N):
            for i in xrange(j+1, N):
                if M[j][i] == 1:
                    if d[j] != d[i]:
                        _r = d[j]
                        for x in groups[d[j]]:
                            d[x] = d[i]

                        groups[d[i]] |= groups[_r]
                        del groups[_r]

        return len(groups)


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [
                [1,1,0],
                [1,1,1],
                [0,1,1]
            ],
            1
        ),
        (
            [
                [1,1,0],
                [1,1,0],
                [0,0,1]
            ],
            2
        ),
        (
            [
                [1,1,1],
                [1,1,1],
                [1,1,1]
            ],
            1
        ),
        (
            [
                [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                [0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],
                [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],
                [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
                [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
                [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
            ],
            8
        )
    ]
    f = s.findCircleNum
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
