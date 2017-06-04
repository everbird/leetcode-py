#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x == 0:
            return True
        elif x < 0:
            return False

        len_number = self.len_number(x)
        s = 0
        e = len_number - 1
        while s < e:
            tail = self.get_digit(x, s)
            s += 1

            head = self.get_digit(x, e)
            e -= 1

            if tail != head:
                return False

        return True

    def len_number(self, x):
        r = 1
        while x // (10 ** r) > 0:
            r += 1
        return r

    def get_digit(self, x, index):
        if 10 ** index >= x:
            return

        x = x % (10 ** (index + 1))
        return x // (10 ** index)


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

    a = 1000021
    s = Solution()
    r = s.isPalindrome(a)
    print r
