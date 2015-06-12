#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        if not n or not m:
            return 0

        moves = 0
        while m!=n:
            m >>= 1
            n >>= 1
            moves += 1

        return m<<moves

if __name__ == '__main__':
    s = Solution()
    print s.rangeBitwiseAnd(5, 7)
