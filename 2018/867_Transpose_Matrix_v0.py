#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    def transpose(self, A):
        if not A:
            return []
        len_y = len(A)
        len_x = len(A[0])
        r = []
        for i in range(len_x):
            tmp = []
            for j in range(len_y):
                tmp.append(A[j][i])
            r.append(tmp)

        return r


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [[1,2,3],[4,5,6],[7,8,9]],
            [[1,4,7],[2,5,8],[3,6,9]]
        ),
        (
            [[1,2,3],[4,5,6]],
            [[1,4],[2,5],[3,6]]
        ),
    ]
    for input_args, expected in tests:
        r = s.transpose(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
