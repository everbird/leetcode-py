#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):

    def hIndex(self, citations):
        n = len(citations)
        return n - bisect_right(0, n, citations)


def bisect_right(b, e, citations):
    n = len(citations)
    while b < e:
        mid = (e + b) // 2
        num = n - mid
        if num > citations[mid]:
            b = mid + 1
        else:
            e = mid

    return b


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            [0,1,3,5,6],
            3
        ),
    ]
    f = s.hIndex
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
