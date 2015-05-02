#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def twoSum(self, nums, target):
        requirements = {}
        for i, a in enumerate(nums):
            b = target - a
            requirements[b] = i

        for j, a in enumerate(nums):
            i = requirements.get(a)
            if i and i < j:
                return i+1, j+1

        return 0, 0


if __name__ == '__main__':
    input_nums = [3,2,4]
    target = 6
    s = Solution()
    x, y = s.twoSum(input_nums, target)
    print x, y
