#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        if not nums:
            return []

        if len(nums) == 1:
            return [nums]

        r = []
        for i, n in enumerate(nums):
            _nums = nums[:]
            _nums.pop(i)

            items = self.permute(_nums)
            for item in items:
                item = [n] + item
                r.append(item)

        return r


if __name__ == '__main__':
    s = Solution()
    print s.permute([1,2,3])
