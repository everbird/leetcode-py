#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        r = 0
        while s:
            c = s[0]
            r = r * 26 + (ord(c) - ord('A') + 1)
            s = s[1:]
        return r

if __name__ == '__main__':
    s = Solution()
    print s.titleToNumber('A')
    print s.titleToNumber('Z')
    print s.titleToNumber('AA')
    print s.titleToNumber('AB')
    print s.titleToNumber('HJ')
