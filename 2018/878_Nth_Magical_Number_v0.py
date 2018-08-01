#!/usr/bin/eni python
# encoding: utf-8


class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        gcd_v = gcd(A, B)
        t = A*B//gcd_v
        j = t // A + t // B - 1
        m = N // j
        n = N % j
        array = get_array(t, A, B)
        r = m * t
        if n > 0:
            r += array[n-1]

        if r > 2**32-1:
            r = r % (10**9+7)
        return r


def get_array(t, A, B):
    a = t // A
    b = t // B
    r1 = [A*(i+1) for i in range(a)]
    r2 = [B*(i+1) for i in range(b)]
    return sorted(r1+r2)



def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)



if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            (
                1,
                2,
                3
            ),
            2
        ),
        (
            (
                4,
                2,
                3
            ),
            6
        ),
        (
            (
                5,
                2,
                4
            ),
            10
        ),
        (
            (
                3,
                6,
                4
            ),
            8
        ),
        (
            (
                1000000000,
                40000,
                40000,
            ),
            999720007
        ),
    ]
    f = s.nthMagicalNumber
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
