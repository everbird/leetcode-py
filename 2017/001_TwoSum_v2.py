#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def twoSum(self, nums, target):
            expections = {}
            for i, a in enumerate(nums):
                b = target - a
                if expections.get(b):
                    expections[b].append(i)
                else:
                    expections[b] = [i, ]
                for j in expections.get(a, []):
                    if j < i:
                        return [j, i]


def main():
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    r = s.twoSum(nums, target)
    assert r == [0, 1]

    nums = [3, 2, 4]
    target = 6
    s = Solution()
    r = s.twoSum(nums, target)
    assert r == [1, 2]

if __name__ == '__main__':
    main()
