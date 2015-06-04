#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        lens = len(s)
        r = [False] * (lens + 1)
        r[0] = True
        for i in range(1, lens+1):
            for j in range(i):
                if r[j] and s[j:i] in wordDict:
                    r[i] = True

        return r[-1]


if __name__ == '__main__':
    s = Solution()
    print s.wordBreak('leetcode', ["leet", "code"])
    print s.wordBreak('aaaaaaa', ["aaaa","aaa"])
    print s.wordBreak('a', ["b"])
