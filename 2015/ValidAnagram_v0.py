#!/usr/bin/env python
# encoding: utf-8

from collections import defaultdict


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        lens = len(s)
        lent = len(t)
        if lens != lent:
            return False

        d = defaultdict(int)
        for i in range(lens):
            d[s[i]] -= 1
            d[t[i]] += 1

        return all(x == 0 for x in d.values())


if __name__ == '__main__':
    s = Solution()
    print s.isAnagram('anagram', 'nagaram')
    print s.isAnagram('rat', 'car')
