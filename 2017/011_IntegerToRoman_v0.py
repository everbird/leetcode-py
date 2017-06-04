#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} num
    # @return {string}

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

    def intToRoman(self, num):
        for n, s in self.d:
            if num >= n:
                return s + self.intToRoman(num - n)

        return ''

if __name__ == '__main__':
    a = 123
    s = Solution()
    r = s.intToRoman(a)
    print r
