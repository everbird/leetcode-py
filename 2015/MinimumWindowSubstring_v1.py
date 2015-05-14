#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        lens = len(s)
        b = 0
        e = 0
        min_l = 2**31
        rb, re = -1, -1
        while e < lens:
            e += 1
            if self.is_contain(s[b:e+1], t):
                while b <= e and self.is_contain(s[b:e+1], t):
                    l = e - b
                    if l < min_l:
                        min_l = l
                        rb = b
                        re = e
                    b += 1

        return s[rb:re+1] if min_l != 2**31 else ''

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
