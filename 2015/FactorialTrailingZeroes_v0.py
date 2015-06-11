#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        if not n:
            return 0

        c = n / 5
        n = n / 5
        return c + self.trailingZeroes(n)


if __name__ == '__main__':
    s = Solution()
    print s.trailingZeroes(10)
    print s.trailingZeroes(11)
    print s.trailingZeroes(4)
    print s.trailingZeroes(5)
    print s.trailingZeroes(1808548329)
    print s.trailingZeroes(30)
