#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def binaryGap(self, N):
        max_length = 0
        cnt = 0
        cnt1 = 0
        while N % 2 == 0:
            N = N // 2

        while N > 0:
            b = N % 2
            if b == 1:
                max_length = max(max_length, cnt+1)
                cnt = 0
                cnt1 += 1
            else:
                cnt += 1
            N = N // 2
        return max_length if cnt1 > 1 else 0


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            22,
            2
        ),
        (
            5,
            2
        ),
        (
            6,
            1
        ),
        (
            8,
            0
        ),
    ]
    f = s.binaryGap
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
