#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        candidates.sort()
        return combination(candidates, target)


def combination(candidates, target):
    if target < 0:
        return []

    if target == 0:
        return [[]]

    r = []
    len_c = len(candidates)
    p = None
    for i, n in enumerate(candidates):
        if p == n:
            continue
        if n < target:
            break

        items = combination(candidates[i+1:], target - n)
        for item in items:
            if item and item[-1] <= n:
                item.append(n)
            else:
                item = [n] + item
            if item not in r:
                r.append(item)
    return r


if __name__ == '__main__':
    s = Solution()
    print s.combinationSum2([10,1,2,7,6,1,5], 8)
