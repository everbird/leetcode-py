#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        nums.sort()
        return self._subsets(nums)

    def _subsets(self, nums):
        if len(nums) == 1:
            return [nums, []]

        last = nums[-1]
        items = self._subsets(nums[:-1])
        r = items[:]
        for item in items:
            r.append(item + [last])
        return r


if __name__ == '__main__':
    s = Solution()
    print s.subsets([1,2,3])
