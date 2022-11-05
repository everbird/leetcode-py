#!/usr/bin/env python
# encoding: utf-8

from collections import defaultdict


class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string

    def findLadders(self, beginWord, endWord, wordList):
        word_set = set(wordList)
        d = defaultdict(list)
        q = {beginWord}
        visited = set([])
        while q and endWord not in q:
            tmp = set()
            for word in q:
                if word in visited:
                    continue

                for next_word in gen_next_words(word, word_set):
                    d[next_word].append(word)
                    tmp.add(next_word)

                visited.add(word)

            q = tmp

        return build_path(beginWord, endWord, d)


def build_path(start, end, d):
    terminal = False
    paths = [[end]]
    while paths and not terminal:
        tmp = []
        for path in paths:
            w = path[0]
            pre_words = d[w]
            for pre_word in pre_words:
                if pre_word == start:
                    terminal = True

                if pre_word not in path:
                    tmp.append([pre_word]+path)

        paths = tmp
        if terminal:
            paths = [x for x in paths if x[0] == start]

    return paths


letters = set([
    chr(ord('a') + i) for i in range(26)
])

def gen_next_words(word, word_set):
    n = len(word)
    for i in range(n):
        for x in letters:
            new_word = word[:i] + x + word[i+1:]
            if new_word != word and new_word in word_set:
                yield new_word


if __name__ == '__main__':
    s = Solution()
    print s.findLadders('hit', 'cog', ["hot","dot","dog","lot","log", "cog"])
    print s.findLadders('hit', 'cog', ["hot","dot","dog","lot","log"])
    print s.findLadders('hot', 'dot', ["hot","dot","dog"])
