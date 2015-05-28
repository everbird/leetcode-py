#!/usr/bin/env python
# encoding: utf-8

import collections
import string


class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordDict):
        if not wordDict:
            return 0

        d = collections.defaultdict(set)
        wl = len(beginWord)
        queue = [beginWord]
        s = set([])
        while queue:
            w = queue.pop()
            s.add(w)
            for i in range(wl):
                for c in string.ascii_lowercase:
                    t = w[:i] + c + w[i+1:]
                    if t in (wordDict - s) and c != w[i]:
                        d[w].add(t)
                        queue = [t] + queue

        for w, v in d.iteritems():
            for i in range(wl):
                for c in string.ascii_lowercase:
                    t = w[:i] + c + w[i+1:]
                    if t == endWord:
                        v.add(t)

        return self.find(d, beginWord, endWord)

    def find(self, d, beginWord, endWord):
        t = d.get(beginWord)
        if not t:
            return 0

        if endWord in t:
            return 2

        r = []
        for s in t:
            c = self.find(d, s, endWord)
            if c:
                r.append(c)

        return min(r)+1 if r else 0


if __name__ == '__main__':
    s = Solution()
    print s.ladderLength('hit', 'cog', set(["hot","dot","dog","lot","log"]))
    print s.ladderLength('hit', 'cog', set(["cig"]))
