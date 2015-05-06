#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        MAX_INT = 2**31 - 1
        MIN_INT = - MAX_INT - 1
        if not divisor:
            return MAX_INT

        negative = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        a = b = 0
        for n in reversed(list(popbits(dividend))):
            a = (a << 1) + n
            b = b << 1
            if a >= divisor:
                b += 1
                a -= divisor

        r = -b if negative else b
        return min(max(MIN_INT, r), MAX_INT)


def popbits(n):
    while n:
        t = n >> 1
        yield int(n != (t + t))
        n = t
    raise StopIteration()


if __name__ == '__main__':
    s = Solution()
    r = s.divide(-13, 5)
    print r
