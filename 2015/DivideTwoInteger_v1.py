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

        a = abs(dividend)
        b = abs(divisor)
        r = 0
        while a >= b:
            shift = 0
            while ((b << shift) <= a):
                shift += 1

            r += 1 << (shift - 1)
            a -= b << (shift - 1)

        rr = -r if negative else r
        return min(max(MIN_INT, rr), MAX_INT)


if __name__ == '__main__':
    s = Solution()
    r = s.divide(-13, 5)
    print r
