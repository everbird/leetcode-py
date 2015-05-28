#!/usr/bin/env python
# encoding: utf-8

import copy


class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordDict):
        if self.is_valid(beginWord, endWord):
            return 2

        if not wordDict:
            return 0

        r = []
        for d in wordDict:
            if self.is_valid(beginWord, d):
                x = copy.copy(wordDict)
                x.discard(d)
                r.append(self.ladderLength(d, endWord, x))
        return min(r)+1 if r else 0

    def is_valid(self, start, end):
        count = 0
        for i in range(len(start)):
            if start[i] != end[i]:
                count += 1
        return count == 1


if __name__ == '__main__':
    s = Solution()
    print s.ladderLength('hit', 'cog', set(["hot","dot","dog","lot","log"]))
    print s.ladderLength('hit', 'cog', set(["cig"]))
