#!/usr/bin/env python
# encoding: utf-8

from collections import defaultdict

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string

    def findLadders(self, beginWord, endWord, wordList):
        min_length = float('inf')
        result = []
        d = get_trasition_dict(wordList+[beginWord])
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


def get_trasition_dict(words):
    d = defaultdict(list)
    n = len(words)
    for i in range(n):
        for j in range(i+1, n):
            a = words[i]
            b = words[j]
            if is_next(a, b):
                d[a].append(b)
                d[b].append(a)
    return d


def is_next(a, b):
    n = len(a)
    cnt = 0
    for i in range(n):
        if a[i] != b[i]:
            cnt += 1
            if cnt > 1:
                return False
    return cnt == 1


if __name__ == '__main__':
    s = Solution()
    print s.findLadders('hit', 'cog', ["hot","dot","dog","lot","log", "cog"])
    print s.findLadders('hit', 'cog', ["hot","dot","dog","lot","log"])
    print s.findLadders('hot', 'dot', ["hot","dot","dog"])
