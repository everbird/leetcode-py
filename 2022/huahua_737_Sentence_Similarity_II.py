#!/usr/bin/env python3

class UnionFindSet:

    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
        elif self.ranks[px] < self.ranks[py]:
            self.parents[px] = py
        else:
            self.parents[px] = py
            self.ranks[py] += 1

        return True


class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        lenp = len(similarPairs)
        lens = len(sentence1)
        if lens != len(sentence2):
            return False
            
        u = UnionFindSet((lens+lenp)*2)

        index_map = {}
        index = 0
        def _get_index(w):
            nonlocal index, index_map
            if w not in index_map:
                index_map[w] = index
                index += 1

            return index_map[w]
        
        for w1, w2 in similarPairs:
            i1 = _get_index(w1)
            i2 = _get_index(w2)
            u.union(i1, i2)

        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2:
                continue
            i1 = _get_index(w1)
            i2 = _get_index(w2)
            if u.find(i1) != u.find(i2):
                return False

        return True
