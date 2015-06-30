#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        candidates.sort()
        return comination(candidates, target, 0)


def comination(candidates, k, start):
    if k < 0:
        return []

    if k == 0:
        return [[]]

    r = []
    p = None
    for i in range(start, len(candidates)):
        n = candidates[i]
        if p and n == p:
            continue
        if n > k:
            break
        items = comination(candidates, k - n, i+1)
        for item in items:
            item = [n] + item
            r.append(item)
        p = n

    return r

if __name__ == '__main__':
    s = Solution()
    print s.combinationSum2([10,1,2,7,6,1,5], 8)
