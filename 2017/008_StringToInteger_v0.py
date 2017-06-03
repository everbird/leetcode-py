#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        r = 0

        str = str.strip()
        if not len(str):
            return 0

        first_c = str[0]
        if first_c == '-':
            flag = -1
        elif first_c == '+':
            flag = 1
        elif first_c in '0123456789':
            flag = 1
            r = int(first_c)
        else:
            return 0

        for c in str[1:]:
            if c in '0123456789':
                r = r * 10 + int(c)
            else:
                break

        return max(INT_MIN, min(INT_MAX, flag * r))


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
