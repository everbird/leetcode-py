#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x == 0:
            return True

        if x < 0 or x % 10 == 0:
            return False

        m = 0
        while m < x:
            m = m * 10 + (x % 10)
            x = x // 10

        return m == x or m // 10 == x


if __name__ == '__main__':
    a = 12321
    s = Solution()
    r = s.isPalindrome(a)
    print r

    a = 12322
    s = Solution()
    r = s.isPalindrome(a)
    print r

    a = 10
    s = Solution()
    r = s.isPalindrome(a)
    print r

    a = 0
    s = Solution()
    r = s.isPalindrome(a)
    print r
