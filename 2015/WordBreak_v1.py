#!/usr/bin/env python
# encoding: utf-8


d = {}


def cache(f):
    def _(inst, s, wordDict):
        r = d.get(s)
        if not r:
            r = f(inst, s, wordDict)
            d[s] = r
        return r
    return _


def clean_cache():
    d.clear()


class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        clean_cache()
        return self._wordBreak(s, wordDict)

    @cache
    def _wordBreak(self, s, wordDict):
        if not s:
            return True

        b = 1
        lens = len(s)
        while b <= lens:
            if s[:b] in wordDict and self._wordBreak(s[b:], wordDict):
                return True
            b += 1

        return False


if __name__ == '__main__':
    s = Solution()
    print s.wordBreak('leetcode', ["leet", "code"])
    print s.wordBreak('aaaaaaa', ["aaaa","aaa"])
    print s.wordBreak('a', ["b"])
