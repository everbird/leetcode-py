#!/usr/bin/env python
# encoding: utf-8


import collections
import copy


class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        if not words:
            return []

        wl = len(words[0])
        tl = len(words) * wl
        c = collections.Counter(words)
        r = []
        for i in range(wl):
            cc = copy.copy(c)
            j = i
            while j < len(s) - wl + 1:
                substr = s[j: j + wl]
                cc[substr] -= 1
                # i chase up to j and restore the cc along the way
                while cc[substr] < 0:
                    chase_str = s[i:i + wl]
                    cc[chase_str] += 1
                    i += wl

                j += wl

                if j - i == tl:
                    r.append(i)

        return r


if __name__ == '__main__':
    a = 'barfoothefoobarman'
    words = ["foo", "bar"]
    s = Solution()
    r = s.findSubstring(a, words)
    print r
