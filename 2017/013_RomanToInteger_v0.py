#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
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
        m = {s: n for n, s in d}
        i = 0
        len_s = len(s)
        r = 0
        while i < len_s:
            if i + 1 < len_s:
                step = 2 if m.get(s[i:i+2]) else 1
            else:
                step = 1

            r += m.get(s[i:i+step])
            i += step

        return r


if __name__ == '__main__':
    a = 'CXXIII'
    s = Solution()
    r = s.romanToInt(a)
    print r
