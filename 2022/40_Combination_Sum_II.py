#!/usr/bin/env python3

from collections import Counter


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        c = Counter(candidates)
        keys = list(c.keys())
        rs = []
        n = len(keys)

        def backtrack(index, remain, items):
            if remain == 0:
                rs.append(items[:])
                return
            elif remain < 0:
                return

            for i in range(index, n):
                k = keys[i]
                if c[k] <= 0:
                    continue

                items.append(k)
                c[k] -= 1
                backtrack(i, remain-k, items)
                c[k] += 1
                items.pop()

        backtrack(0, target, [])
        return rs

# User counter to consume dup first to avoid dup answer
#

from collections import Counter


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        rs = []
        candidates.sort()
        n = len(candidates)

        def backtrack(index, remain, items):
            if remain == 0:
                rs.append(items[:])
                return
            elif remain < 0:
                return

            for i in range(index, n):
                if i > index and candidates[i] == candidates[i-1]:
                    continue

                if candidates[i] > remain:
                    break

                items.append(candidates[i])
                backtrack(i+1, remain-candidates[i], items)
                items.pop()

        backtrack(0, target, [])
        return rs

# Sort and only deal with the first dup element
