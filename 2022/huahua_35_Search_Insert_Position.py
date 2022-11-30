#!/usr/bin/env python3

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return binary_search(nums, target)


def binary_search(nums, target):
    if not nums or nums[0] > target:
        return 0

    if nums[-1] < target:
        return len(nums)

    s = 0
    e = len(nums) - 1
    while s <= e:
        m = (s - e) // 2 + e
        if nums[m] > target:
            e = m - 1
        elif nums[m] < target:
            s = m + 1
        else:
            return m

    return s
