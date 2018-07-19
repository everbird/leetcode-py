#!/usr/bin/eni python
# encoding: utf-8


import math


class Solution(object):
    def primePalindrome(self, N):
        step = 2
        if N < 3:
            step = 1
        n = N if (N % 2 != 0 or N < 3) else N + 1
        while not is_palindrome(n) or not is_prime(n):
            if 10**7 < n < 10**8:
                n = 10**8+1
            else:
                n += step

        return n


def is_palindrome(n):
    if n < 10:
        return True

    left = n
    right = 0
    while left >= right:
        right = right * 10 + left % 10
        left = left // 10
        # print '>>>', left, right
        if right == left or right == left // 10:
            return True

    return False


def is_prime(n):
    if n == 1:
        return False

    if n in (2, 3):
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False

    return True


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            6,
            7
        ),
        (
            8,
            11
        ),
        (
            13,
            101
        ),
        (
            1,
            2
        ),
        (
            2,
            2
        ),
        (
            930,
            10301
        ),
        (
            9989900,
            100030001
        )
    ]
    for input_args, expected in tests:
        r = s.primePalindrome(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
