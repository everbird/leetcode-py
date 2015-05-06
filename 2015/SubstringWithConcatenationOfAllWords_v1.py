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
                    r.append((i, True))
                    r.append((i + lenw - 1, False))

            return r

        lenw = len(words[0])

        positions = self.findSubstring(s, words[:-1])
        last_word = words[-1]
        r = []
        for pos, left in positions:
            if left and last_word == s[pos - lenw:pos]:
                r.append((pos - lenw, left))
            elif not left and last_word == s[pos + 1: pos + lenw + 1]:
                r.append((pos + lenw + 1, left))

        return r


if __name__ == '__main__':
    a = 'barfoothefoobarman'
    #words = ["foo", "bar"]
    words = ["foo", ]
    s = Solution()
    r = s.findSubstring(a, words)
    print r
