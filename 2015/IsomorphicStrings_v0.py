#!/usr/bin/env python
# encoding: utf-8


import string

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        visited = set([])
        m = {}
        lens = len(s)
        lent = len(t)
        if lens != lent:
            return False

        for i in range(lens):
            c1 = s[i]
            c2 = t[i]
            r = m.get(c1)
            if not r and c2 not in visited:
                m[c1] = c2
                visited.add(c2)
            elif r != c2:
                return False

        return True



if __name__ == '__main__':
    s = Solution()
    print s.isIsomorphic('egg', 'add')
    print s.isIsomorphic('foo', 'bar')
    print s.isIsomorphic('paper', 'title')
    print s.isIsomorphic('ab', 'aa')
    print s.isIsomorphic('13', '42')
