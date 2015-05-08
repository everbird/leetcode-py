#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        candidates.sort()
        return combination(candidates, target)


def combination(candidates, target):
    if target < 0:
        return []

    if target == 0:
        return [[]]

    r = []
    for i, n in enumerate(candidates):
        items = combination(candidates[i:], target - n)
        for item in items:
            if not item or item[-1] <= n:
                item.append(n)
            else:
                item = [n] + item

            r.append(item)

    return r


if __name__ == '__main__':
    s = Solution()
    print s.combinationSum([2,3,6,7], 7)
    print s.combinationSum([8,7,4,3], 11)
    print s.combinationSum([3,2,6,7], 11)
