#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        candidates.sort()
        return comination(candidates, target)


def comination(candidates, k):
    if k < 0:
        return []

    if k == 0:
        return [[]]

    r = []
    for i, n in enumerate(candidates):
        items = comination(candidates[i + 1:], k - n)
        for item in items:
            item = [n] + item
            if item not in r:
                r.append(item)

    return r


if __name__ == '__main__':
    s = Solution()
    print s.combinationSum2([10,1,2,7,6,1,5], 8)
