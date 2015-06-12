#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        lens = len(s)
        m = {}
        r = []
        t = 0
        for i in range(lens):
            c = s[i]
            n = (ord(c) - ord('A')) % 5
            t = (t << 2 & 0xfffff) | n
            if i >= 9:
                if m.get(t) == 1:
                    r.append(s[i-9:i+1])
                m[t] = m[t] + 1 if m.get(t) else 1

        return r

if __name__ == '__main__':
    s = Solution()
    print s.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')
    print s.findRepeatedDnaSequences('AAAAAAAAAAA')
    print s.findRepeatedDnaSequences('AAAAAAAAAAAA')
