#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        r = 0
        symbol = 1
        str = str.strip()
        if not str:
            return 0

        if str[0] == '-':
            symbol = -1
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]

        for i, c in enumerate(str):
            if c not in '1234567890':
                break

            r = r * 10 + (ord(c) - ord('0'))

        r *= symbol
        return max(min(r, INT_MAX), INT_MIN)


if __name__ == '__main__':
    a = '123456'
    s = Solution()
    i = s.myAtoi(a)
    print i

    a = '123456.789'
    s = Solution()
    i = s.myAtoi(a)
    print i

    a = '32e123456.789'
    s = Solution()
    i = s.myAtoi(a)
    print i

    a = '  +123456  '
    s = Solution()
    i = s.myAtoi(a)
    print i

    a = '-123456'
    s = Solution()
    i = s.myAtoi(a)
    print i

    a = '987654123456'
    s = Solution()
    i = s.myAtoi(a)
    print i

    a = '-987654123456'
    s = Solution()
    i = s.myAtoi(a)
    print i

    a = '-987a54123456'
    s = Solution()
    i = s.myAtoi(a)
    print i
