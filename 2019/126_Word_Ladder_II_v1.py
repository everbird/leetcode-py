#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string

    def findLadders(self, beginWord, endWord, wordList):
        min_length = float('inf')
        result = []
        words = wordList+[beginWord]
        word_set = set(words)
        d = {}
        for word in words:
            d[word] = list(gen_next_words(word, word_set))

        q = [(beginWord, [beginWord], {beginWord})]
        while q:
            w, rs, visited = q.pop()
            if w not in d:
                continue
            next_words = d[w]
            for next_word in next_words:
                if next_word in visited:
                    continue

                new_rs = rs[:] + [next_word]
                new_visited = visited.copy()
                new_visited.add(next_word)
                visited.add(next_word)
                if next_word == endWord:
                    if len(new_rs) < min_length:
                        min_length = len(new_rs)
                        result = [new_rs]
                    elif len(new_rs) == min_length:
                        result.append(new_rs)
                else:
                    q.insert(0, (next_word, new_rs, new_visited))

        return result


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
