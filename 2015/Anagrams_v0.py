#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        d = {}
        r = []
        for s in strs:
            ids = ''.join(sorted(s))
            if ids in d:
                d[ids].append(s)
            else:
                d[ids] = [s]

        for k, v in d.iteritems():
            if len(v) > 1:
                r += v
        return r


if __name__ == '__main__':
    s = Solution()
    print s.anagrams(["ape","and","cat"])
    print s.anagrams([""])
