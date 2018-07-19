#!/usr/bin/eni python
# encoding: utf-8


import math


class Solution(object):
    def primePalindrome(self, N):
        step = 1
        n = N
        while True:
            if is_palindrome(n):
                if is_prime(n):
                    return n
                n = next_palindrome(n)
            else:
                n += step


def is_palindrome(n):
    if n < 10:
        return True

    if n % 10 == 0:
        return False

    left = n
    right = 0
    while left >= right:
        right = right * 10 + left % 10
        left = left // 10
        # print '>>>', left, right
        if right == left or right == left // 10:
            return True

    return False


def n_length(n):
    if n == 0:
        return 1

    r = 0
    while n > 0:
        r += 1
        n = n // 10

    return r

def next_palindrome(p):
    if p < 10:
        return p+1

    length = n_length(p)
    right_length = length // 2
    left = p // (10**right_length)

    if length % 2 == 0 and left not in (9, 99, 999, 9999):
        l = m = (left + 1)
    else:
        m = left + 1
        l = m // 10

    while l > 0:
        m = m * 10 + l % 10
        l = l // 10

    return m


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
        ),
        (
            85709140,
            100030001
        )
    ]
    for input_args, expected in tests:
        r = s.primePalindrome(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
