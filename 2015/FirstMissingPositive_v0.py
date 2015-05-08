#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        if not nums:
            return 1

        max_n = max(nums)
        d = {x: True for x in nums}
        for i in range(1, len(nums) + 1):
            if not d.get(i):
                return i

        return max_n + 1


if __name__ == '__main__':
    s = Solution()
    print s.firstMissingPositive([1,2,0])
    print s.firstMissingPositive([3,4,-1,1])
