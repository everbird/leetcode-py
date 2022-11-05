#!/usr/bin/env python
# encoding: utf-8

from collections import defaultdict


class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string

    def findLadders(self, beginWord, endWord, wordList):
        ans = []
        word_set = set(wordList)
        layer = defaultdict(list)
        layer[beginWord] = [[beginWord]]
        while layer:
            new_layer = defaultdict(list)
            for w, paths in layer.iteritems():
                if w == endWord:
                    return paths

                for next_word in gen_next_words(w, word_set):
                    new_layer[next_word].extend([p+[next_word] for p in paths])

            word_set -= set(new_layer.keys())
            layer = new_layer
        return ans


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
