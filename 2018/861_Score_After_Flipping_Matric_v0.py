#!/usr/bin/env python
# encoding: utf-8



class Solution(object):

    def matrixScore(self, A):
        if not A:
            return 0

        len_y = len(A)
        len_x = len(A[0])
        # Highest left all -> 1
        for j in range(len_y):
            if A[j][0] == 0:
                toggle_h(A, j)

        # Check each columns to make sure it has most 1
        for i in range(1, len_x):
            cnt = 0
            for j in range(len_y):
                if A[j][i] == 1:
                    cnt += 1

            if cnt <= (len_y // 2):
                toggle_v(A, i)

        return sum([iterpret(row) for row in A])


def iterpret(row):
    len_n = len(row)
    r = 0
    for i in range(len_n):
        if row[i] == 1:
            r += 1 << (len_n - i - 1)
    return r


def toggle_v(A, x):
    for row in A:
        v = row[x]
        row[x] = 0 if v == 1 else 1


def toggle_h(A, y):
    row = A[y]
    for i, item in enumerate(row):
        row[i] = 0 if item == 1 else 1






if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [[0,0,1,1],[1,0,1,0],[1,1,0,0]],
            39
        ),
    ]
    for input_args, expected in tests:
        r = s.matrixScore(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
