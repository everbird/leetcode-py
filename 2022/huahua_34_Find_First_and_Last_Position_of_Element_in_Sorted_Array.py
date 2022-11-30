#!/usr/bin/env python3

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bs_find(nums, target)
        right = bs_find(nums, target, first=False)
        return [left, right]


def bs_find(nums, target, first=True):
    s = 0
    e = len(nums)-1
    while s <= e:
        m = (s + e) // 2
        # move left
        if nums[m] > target:
            e = m - 1
        elif nums[m] < target:
            s = m + 1
        else:
            if first:
                if m == s or nums[m-1] != target:
                    return m
                e = m - 1
            else:
                if m == e or nums[m+1] != target:
                    return m

                s = m + 1

    return -1
