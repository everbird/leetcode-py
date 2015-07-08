#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        count = 0
        m = 1

        while m <= n:
            left = n // (10*m)
            cur = n // m % 10
            right = n % m

            v = (left+1) * m
            if cur == 1:
                v -= (m - 1 - right)
            elif cur == 0:
                v -= m

            count += v
            m *= 10

        return count


if __name__ == '__main__':
    s = Solution()
    print s.countDigitOne(13)
    print s.countDigitOne(213)
    print s.countDigitOne(0)
    print s.countDigitOne(1)
    print s.countDigitOne(10)
