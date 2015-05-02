#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def twoSum(self, nums, target):
        reqs = {}
        for i, a in enumerate(nums):
            b = target - a
            if reqs.get(b):
                reqs[b].append(i)
            else:
                reqs[b] = [i, ]

            for j in reqs.get(a, []):
                if j < i:
                    return j+1, i+1


if __name__ == '__main__':
    input_nums = [0,4,3,0]
    target = 0
    s = Solution()
    x, y = s.twoSum(input_nums, target)
    print x, y
