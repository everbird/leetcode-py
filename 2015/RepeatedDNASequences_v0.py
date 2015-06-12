#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        lens = len(s)
        m = {}
        r = []
        for i in range(lens - 10 + 1):
            w = s[i:i+10]
            if m.get(w) and w not in r:
                r.append(w)
                continue

            m[w] = True

        return r

if __name__ == '__main__':
    s = Solution()
    print s.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')
    print s.findRepeatedDnaSequences('AAAAAAAAAAA')
    print s.findRepeatedDnaSequences('AAAAAAAAAAAA')
