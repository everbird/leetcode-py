#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        m = ''
        n = ''
        min_l = len(s)
        min_m = ''
        for i, c in enumerate(s):
            if c in t and c not in n:
                n += c

            if c not in n:
                if m:
                    m += c
            else:
                m += c
                m = self.shorten(m, n, c)

            if n == t:
                if min_l >= len(m):
                    min_l = len(m)
                    min_m = m

        return min_m

    def shorten(self, m, n, c):
        for i, char in enumerate(m):
            if char in n and not self.is_contain(m[i+1:], n):
                return m[i:]

        return m

    def is_contain(self, s, t):
        for c in t:
            if c not in s:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    print s.minWindow('ADOBECODEBANC', 'ABC')
    print s.minWindow('ADOBECODEBANC', 'ABCZ')
    print s.minWindow('a', 'a')
    print s.minWindow('a', 'b')
    print s.minWindow('ab', 'A')
    print s.minWindow('ab', 'b')
    print s.minWindow('aa', 'aa')
