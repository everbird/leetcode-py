#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        if not s:
            return [[]]

        b = 1
        lens = len(s)
        r = []
        while b <= lens:
            if s[:b] in wordDict:
                items = self.wordBreak(s[b:], wordDict)
                for i in items:
                    r.append([s[:b]] + i)

            b += 1

        return r


if __name__ == '__main__':
    s = Solution()
    print s.wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"])
