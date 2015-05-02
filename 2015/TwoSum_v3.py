#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def twoSum(self, nums, target):
        requirements = {}
        for i, a in enumerate(nums):
            b = target - a
            if requirements.get(b):
                requirements[b].append(i)
            else:
                requirements[b] = [i, ]

        for j, a in enumerate(nums):
            ints = requirements.get(a)
            if ints:
                for i in ints:
                    if i < j:
                        return i+1, j+1


if __name__ == '__main__':
    input_nums = [0,4,3,0]
    target = 0
    s = Solution()
    x, y = s.twoSum(input_nums, target)
    print x, y
