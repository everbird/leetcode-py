#!/usr/bin/eni python
# encoding: utf-8

class Solution(object):
    def isAdditiveNumber(self, num):
        length = len(num)
        if length < 3:
            return False

        N = (length + 1) // 2
        for j in xrange(1, N):
            for i in xrange(1, N):
                if is_additive_number(i, j, num):
                    return True

        return False


def is_additive_number(first_len, second_len, num):
    length = len(num)
    a = (0, first_len)
    b = (first_len, first_len+second_len)
    while b[1] < length:
        a_s = num[a[0]:a[1]]
        b_s = num[b[0]:b[1]]
        if is_zero_prefixed_num(a_s) or is_zero_prefixed_num(b_s):
            return False

        an = int(num[a[0]:a[1]])
        bn = int(num[b[0]:b[1]])
        n = an + bn
        # print '>>', an, bn, n
        if not num[b[1]:].startswith(str(n)):
            return False

        a = b
        b = (a[1], a[1]+len(str(n)))

    # print '!!', a, b
    if b[1] == length:
        return True

    return a[1] == length


def is_zero_prefixed_num(num):
    if num == '0':
        return False

    return num.startswith('0')


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            "112358",
            True
        ),
        (
            "199100199",
            True
        ),
        (
            "10",
            False
        ),
        (
            "111",
            False
        ),
        (
            "123",
            True
        ),
        (
            "1023",
            False
        ),
        (
            "101",
            True
        )
    ]
    f = s.isAdditiveNumber
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
