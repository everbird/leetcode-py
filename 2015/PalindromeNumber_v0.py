#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        n = x
        m = 0
        while n > 0:
            m = m * 10 + (n % 10)
            n = n // 10

        return m == x


if __name__ == '__main__':
    a = 12321
    s = Solution()
    r = s.isPalindrome(a)
    print r

    a = 12322
    s = Solution()
    r = s.isPalindrome(a)
    print r
