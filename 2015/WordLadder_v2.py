#!/usr/bin/env python
# encoding: utf-8

import string
import collections


class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordDict):
        bqueue = collections.deque([beginWord])
        equeue = collections.deque([endWord])
        bs = {beginWord}
        es = {endWord}
        wl = len(beginWord)
        lenb = 1
        lene = 1
        while bqueue and equeue:
            # left
            bl = len(bqueue)
            for _ in range(bl):
                w = bqueue.popleft()
                for i in range(wl):
                    for c in string.ascii_lowercase:
                        t = w[:i] + c + w[i+1:]
                        if t in es:
                            return lenb + lene
                        if t in wordDict and t not in bs:
                            bs.add(t)
                            bqueue.append(t)
            lenb += 1

            el = len(equeue)
            for _ in range(el):
                w = equeue.popleft()
                for i in range(wl):
                    for c in string.ascii_lowercase:
                        t = w[:i] + c + w[i+1:]
                        if t in bs:
                            return lenb + lene
                        if t in wordDict and t not in es:
                            es.add(t)
                            equeue.append(t)
            lene += 1

        return 0


if __name__ == '__main__':
    s = Solution()
    print s.ladderLength('hit', 'cog', set(["hot","dot","dog","lot","log"]))
    print s.ladderLength('hit', 'cog', set(["cig"]))
