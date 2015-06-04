#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        if not s:
            return True

        b = 1
        lens = len(s)
        while b <= lens:
            if s[:b] in wordDict and self.wordBreak(s[b:], wordDict):
                return True
            b += 1

        return False


if __name__ == '__main__':
    s = Solution()
    print s.wordBreak('leetcode', ["leet", "code"])
    print s.wordBreak('aaaaaaa', ["aaaa","aaa"])
