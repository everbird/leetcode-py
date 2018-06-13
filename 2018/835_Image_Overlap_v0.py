#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    # Time Limit Exceeded
    def largestOverlapx(self, A, B):
        if not A or not B:
            return 0

        N = len(A)
        shifts = range(-N+1, N)
        max_cnt = 0
        for j in shifts:
            for i in shifts:
                cnt = 0
                for jj in range(N):
                    for ii in range(N):
                        _j = jj + j
                        _i = ii + i
                        if 0 <= _j < N and 0 <= _i < N:
                            if A[_j][_i] and B[jj][ii]:
                                cnt += 1
                max_cnt = max(max_cnt, cnt)
        return max_cnt

    def largestOverlap(self, A, B):
        N = len(A)
        shifts = range(-N+1, N)
        max_cnt = 0
        for j in shifts:
            for i in shifts:
                cnt = 0
                for jj in range(N):
                    for ii in range(N):
                        if B[jj][ii] and 0 <= (jj + j) < N and 0 <= (ii + i) < N and A[jj + j][ii + i]:
                            cnt += 1
                max_cnt = max(max_cnt, cnt)
        return max_cnt


def main():
    s = Solution()
    tests = [
        (
            (
                [[1,1,0],
                 [0,1,0],
                 [0,1,0]],
                [[0,0,0],
                 [0,1,1],
                 [0,0,1]]
            ),
            3
        ),
        (
            (
                [[0,1],[1,1]],
                [[1,1],[1,0]]
            ),
            2
        )
    ]
    for input_args, expected in tests:
        r = s.largestOverlap(*input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)

if __name__ == '__main__':
    main()
