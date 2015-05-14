#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        lens = len(s)
        if lens == 1:
            return s if t == s else ''

        b = 0
        e = lens - 1

        while b <= e and s[b] not in t:
            b += 1

        while b <= e and s[e] not in t:
            e -= 1

        last = ''
        if self.is_contain(s, t):
            last = s

        while b <= e:
            if self.is_contain(s[b+1:e+1], t):
                b += 1
                while s[b] not in t:
                    b += 1
                last = s[b:e+1]
            elif self.is_contain(s[b:e], t):
                e -= 1
                while s[e] not in t:
                    e -= 1
                last = s[b:e]
            else:
                break

        return last

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
