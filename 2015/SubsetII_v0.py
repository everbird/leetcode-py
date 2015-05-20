#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        nums.sort()
        return self._subsets(nums)

    def _subsets(self, nums):
        if not nums:
            return [[]]

        n = nums[0]
        items = self.subsetsWithDup(nums[1:])
        r = items[:]
        for i in items:
            t = [n] + i
            if t not in r:
                r.append(t)

        return r


if __name__ == '__main__':
    s = Solution()
    print s.subsetsWithDup([1,2,2])
