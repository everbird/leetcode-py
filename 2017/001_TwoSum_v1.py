#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def twoSum(self, nums, target):
        pos_map = self.get_position_map(nums)
        index_start = 0
        index_end = len(nums) - 1
        _nums = sorted(nums)
        while index_start < index_end:
            if _nums[index_start] + _nums[index_end] > target:
                index_end = index_end - 1
            elif _nums[index_start] + _nums[index_end] < target:
                index_start = index_start + 1
            else:
                return [pos_map[_nums[index_start]], pos_map[_nums[index_end]]]

    def get_position_map(self, nums):
        r = {}
        for i, n in enumerate(nums):
            r[n] = i
        return r


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
