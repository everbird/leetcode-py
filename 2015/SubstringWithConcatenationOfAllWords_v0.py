#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        if len(words) == 1:
            word = words[0]
            lenw = len(word)
            r = []
            for i, c in enumerate(s[:-lenw + 1]):
                if word == s[i:i + lenw]:
                    r.append(i)

            return r

        positions = self.findSubstring(s, words[:-1])
        last_word = words[-1]
        pre_word = words[-2]
        lenlw = len(last_word)
        lenpw = len(pre_word)
        r = []
        for i in positions:
            if (last_word == s[i-lenlw:i]
                    or last_word == s[i+lenpw:i+lenpw+lenlw]):
                r.append(i)

        return r


if __name__ == '__main__':
    a = 'barfoothefoobarman'
    words = ["foo", "bar"]
    s = Solution()
    r = s.findSubstring(a, words)
    print r
