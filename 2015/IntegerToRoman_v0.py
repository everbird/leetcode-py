#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        d = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        ]
        r = ''
        for i, c in d:
            while num >= i:
                num -= i
                r += c
        return r


if __name__ == '__main__':
    a = 123
    s = Solution()
    r = s.intToRoman(a)
    print r
