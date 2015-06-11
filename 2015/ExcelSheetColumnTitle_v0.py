#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        r = ''
        while n:
            x = (n-1) % 26
            r = chr(ord('A')+x) + r
            n = (n-1) / 26

        return r


if __name__ == '__main__':
    s = Solution()
    print s.convertToTitle(1)
    print s.convertToTitle(26)
    print s.convertToTitle(27)
    print s.convertToTitle(28)
    print s.convertToTitle(218)
