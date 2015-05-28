#!/usr/bin/env python
# encoding: utf-8

import collections
import string

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string

    parents_tracker = {}

    def findLadders(self, start, end, dict):
        self.parents_tracker.clear()
        dict.add(end)
        level_tracker = collections.defaultdict(set)
        items = {start}
        while items and end not in level_tracker:
            current = set([])
            for w in items:
                for nextw in self.gen_next_words(w, dict):
                    if nextw not in self.parents_tracker:
                        current.add(nextw)
                        level_tracker[nextw].add(w)

            self.parents_tracker.update(level_tracker)
            items = current

        return [] if not items else self.buildpath(start, end)

    def gen_next_words(self, word, dict):
        for i in range(len(word)):
            for c in string.ascii_lowercase:
                nextw = word[:i] + c + word[i+1:]
                if nextw in dict and nextw != word:
                    yield nextw

    def buildpath(self, start, end):
        r = [[end]]
        while r[-1][0] != start:
            rs = []
            for path in r:
                w = path[0]
                pre_words = self.parents_tracker[w]
                for pw in pre_words:
                    rs.append([pw] + path[:])

            r = rs

        return r


if __name__ == '__main__':
    s = Solution()
    print s.findLadders('hit', 'cog', set(["hot","dot","dog","lot","log"]))
    print s.findLadders('hot', 'dot', set(["hot","dot","dog"]))
