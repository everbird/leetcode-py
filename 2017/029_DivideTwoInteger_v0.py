#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        if (divisor == 0
            or not (MIN_INT <= dividend <= MAX_INT)
            or not (MIN_INT <= divisor <= MAX_INT)
        ):
            return MAX_INT

        negative = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        a = abs(dividend)
        b = abs(divisor)
        if a < b:
            return 0

        r = 0
        while a >= b:
            shift = 1
            while (a >= (b << shift)):
                shift += 1

            r += 1 << (shift - 1)
            a -= b << (shift - 1)

        return max(MIN_INT, -r) if negative else min(MAX_INT, r)


if __name__ == '__main__':
    s = Solution()
    r = s.divide(-13, 5)
    print r
    print '----------'
    r = s.divide(0, 1)
    print r
    print '----------'
    r = s.divide(-2147483648, -1)
    print r
