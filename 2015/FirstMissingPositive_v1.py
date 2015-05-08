#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        if not nums:
            return 1

        lenn = len(nums)
        for i in range(lenn):
            while (lenn > nums[i] > 0
                   and nums[i] != (i + 1)
                   and nums[i] != nums[nums[i] - 1]):
                swap(nums, i, nums[i] - 1)

        for i, n in enumerate(nums):
            if n != i + 1:
                return i + 1

        return n + 1


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


if __name__ == '__main__':
    s = Solution()
    print s.firstMissingPositive([1,2,0])
    print s.firstMissingPositive([3,4,-1,1])
    print s.firstMissingPositive([1,1])
