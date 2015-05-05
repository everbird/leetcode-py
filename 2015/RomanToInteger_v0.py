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
        maps = {y: x for x, y in d}
        r = 0
        p = len(s) - 1
        while p >= 0:
            ss = s[p - 1:p + 1]
            n = maps.get(ss)
            if n:
                r += n
                p -= 2
            else:
                r += maps.get(s[p])
                p -= 1

        return r


if __name__ == '__main__':
    a = 'CXXIII'
    s = Solution()
    r = s.romanToInt(a)
    print r
